import json
import os
import threading

import keyboard
from fuzzywuzzy import fuzz
from win32com.client import Dispatch

import stt
from module import cfg, tts

path = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"


def read_json():
    """
    Метод читает файл json
    :return: возвращает путь объекта
    """
    with open('config_.json', 'r', encoding='utf-8') as file:
        stock = json.load(file)
        print(json.dumps(stock,
                         sort_keys=False,
                         indent=4,
                         ensure_ascii=False,
                         separators=(',', ': ')))

    # Find_Photoshop("C:\Program Files")


def subprocess_setup(process: str):
    try:
        app = Dispatch(process)
        return app
    except Exception as e:
        print(e)


def va_respond(voice: str):
    print(voice)
    if voice.startswith(cfg.Pak_allias):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in cfg.Pak_commandlist.keys():
            tts.va_speak("")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in cfg.Pak_allias:
        cmd = cmd.replace(x, "").strip()

    for x in cfg.VAP_TBR:
        cmd = cmd.replace(x, "").strip()
    print(cmd, 'cmd')
    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in cfg.Pak_commandlist.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd: str):
    if cmd == 'help':
        text = "Я умею: ..."
        text += "открывать фотошоп ..."
        text += "создавать холсты ..."
        text += "и слои"
        text += "а также отменять действия"
        threading.Thread(target=tts.va_speak(text))

    elif cmd == 'openPS':
        speak = 'Открыла'

        threading.Thread(target=(os.startfile(path)))

        tts.va_speak(speak)

    elif cmd == 'holst':
        keyboard.send('ctrl+n')
    elif cmd == 'New_Layer':
        app = subprocess_setup("Photoshop.Application")

        docRef = app.Application.ActiveDocument
        layerRef = docRef.ArtLayers.Add()

    elif cmd == 'CTRLC':
        threading.Thread(target=keyboard.send('ctrl+c'))

    elif cmd == 'TextLayer':
        app = subprocess_setup("Photoshop.Application")

        app.Preferences.RulerUnits = 2
        app.Preferences.TypeUnits = 5

        app.displayDialogs = 3
        newTextLayer = app.Application.ActiveDocument.ArtLayers.Add()
        newTextLayer.Kind = 2
        newTextLayer.TextItem.Contents = "Your Text!"
        newTextLayer.TextItem.Contents = "Hello, World!"
    elif cmd == 'ctrlz':
        keyboard.send('ctrl+alt+z')
    elif cmd == 'Return':
        keyboard.send('ctrl+shift+z')
    elif cmd == 'CTRLV':
        keyboard.send('ctrl+v')
    elif cmd == 'CUT':
        keyboard.send('f2')
    elif cmd == 'open_file':
        keyboard.send('ctrl+o')
    elif cmd == 'increase':
        keyboard.send('ctrl,+')
    elif cmd == 'decrease':
        keyboard.send('ctrl+-')
    elif cmd == 'display':
        keyboard.send('ctrl+alt+0')
    elif cmd == 'scale':
        keyboard.send('z')
    elif cmd == 'layers_panel':
        keyboard.send('f7')
    elif cmd == 'copy_layer':
        keyboard.send('ctrl+j')
    elif cmd == 'group_layer':
        keyboard.send('ctrl+g')
    elif cmd == 'disgroup':
        keyboard.send('ctrl+shift+g')
    elif cmd == 'select_layer':
        keyboard.send('ctrl+alt+a')
    elif cmd == 'scale':
        keyboard.send('z')
    elif cmd == 'scale':
        keyboard.send('z')
    elif cmd == 'scale':
        keyboard.send('z')
    elif cmd == 'scale':
        keyboard.send('z')


if __name__ == "__main__":
    read_json()
    # print(*passage('photoshop.exe', 'C:\Program Files'))
    print(f'Голосовой помощник{cfg.VAP_name} версии {cfg.VAP_ver} готов нести службу\n',
          "чтобы выйти нажмите Ctrl+Q")
    threading.Thread(target=stt.va_listen(va_respond))

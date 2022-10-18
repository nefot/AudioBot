import json
import os
import threading

import keyboard
from fuzzywuzzy import fuzz
from win32com.client import Dispatch

import stt
from module.tts import TTSpeaker

path = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe"
stocks = {}


def read_json():
    with open('config_.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def subprocess_setup(process: str) :
    """
    Метод производит запуск приложения в отдельном потоке
    @return Результат выполнения
    ---------------------------------------------------------
                 ВНИМАНЕ МЕТОД НЕ ДОПИСАН И НЕ РАБОТАЕТ (ИДУТ СТРОИТЕЛЬНЫЕ РАБОТЫ)
                            НЕ ПЫТАЙТЕСЬ ЕГО ВЫЗВАТЬ ИЛИ УДАЛИТЬ
    ---------------------------------------------------------------
    """
    try:
        app = Dispatch(process)
        return app
    except Exception as e:
        print(e)


def va_respond(voice: str):
    print(voice)
    if voice.startswith(tuple(stocks["other"]["pack_atlas"])):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in stocks["pack_command-list"].keys():
            model.load_bath("")
        else:
            execute_cmd(cmd['cmd'])


def filter_cmd(raw_voice: str):
    cmd = raw_voice
    for x in stocks["other"]["pack_atlas"]:
        cmd = cmd.replace(x, "").strip()  # форматирует строку

    for x in stocks["other"]["var_tbr"]:  # cfg.VAP_TBR:
        cmd = cmd.replace(x, "").strip()
    return cmd


def recognize_cmd(cmd: str):
    """
    на вход подается
    распознает команду(к примеру, если есть отличие на пару букв или если это другая форма одного слова)
    """
    DICTIONARY_SIM = {'cmd': '', 'percent': 0}
    for CMD, v in stocks["pack_command-list"].items():
        for x in v:
            SIMILARITY = fuzz.ratio(cmd, x)  # сравнивается команда с командой в файле
            if SIMILARITY > DICTIONARY_SIM['percent']:  # если сравнение больше 0 то
                # дальше в словарь записываются данные: КАКАЯ КОМАНДА И НА СКОЛЬКО ПОХОЖА
                DICTIONARY_SIM['cmd'] = CMD
                DICTIONARY_SIM['percent'] = SIMILARITY

    return DICTIONARY_SIM


def execute_cmd(cmd: str):
    if cmd == 'help':
        text = "Йа умею: ..." + \
               "аткрыв+ать фотош+оп ..." + \
               "саздав+ать холст+ы ..." + "и  сла и ..." + \
               "а т++акже отменйать действийа"

        threading.Thread(target=model.load_bath(text))
        threading.Thread(target=(model.va_speak()))

    elif cmd == 'open_ps':
        speak = 'аткрыл'
        threading.Thread(target=(os.startfile(path)))
        model.load_bath(speak)
        threading.Thread(target=(model.va_speak()))

    elif cmd == 'holst':
        keyboard.send('ctrl+n')

    elif cmd == 'new_layer':
        speak = 'саздал'
        model.load_bath(speak)
        threading.Thread(target=(model.va_speak()))
        subprocess_setup("Photoshop.Application")

    elif cmd == 'CTRLC':
        threading.Thread(target=keyboard.send('ctrl+c'))

    elif cmd == 'text_layer':
        try:
            app = subprocess_setup("Photoshop.Application")
            # pywintypes.com_error: (-2147417846, 'Фильтр сообщений выдал диагностику о занятости приложения.', None, None)
            app.Preferences.TypeUnits = 5
            app.displayDialogs = 3
            newTextLayer = app.Application.ActiveDocument.ArtLayers.Add()
            newTextLayer.Kind = 2
            newTextLayer.TextItem.Contents = "Your Text!"
            newTextLayer.TextItem.Contents = "Hello, World!"
        except Exception as e:
            print(e, "ПРОВЕРЬ ДИРЕКТОРИЮ ФОТОШОПА")

    elif cmd == 'ctrlz':
        try:
            keyboard.send('ctrl+alt+z')
        except Exception as e:
            print(e)
    elif cmd == 'return':
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


if __name__ == "__main__":
    stocks = read_json()
    model = TTSpeaker()
    model.load_bath(stt.va_listen(va_respond))
    model.va_speak()

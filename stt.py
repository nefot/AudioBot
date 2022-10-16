import keyboard
import vosk
import sys
import sounddevice as sd
import queue
import json

model = vosk.Model("small_model")
samplerate = 16000
device = 1

q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=800, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()

            if keyboard.is_pressed('Ctrl + Q'):
                quit()
            elif rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])

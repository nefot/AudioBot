import json5
import os.path
import queue
import sys
import sounddevice as sd
import vosk


def Find_Model():
    if os.path.exists("small_model"):
        print("small_model is successfully")
        return "small_model"
    elif os.path.exists("large_model"):
        print("large_model is successfully")
        return "large_model"
    elif os.path.exists("tiny_model"):
        print("tiny_model is successfully")
        return "tiny_model"
    elif os.path.exists('model'):
        print("model is successfully")
        return "model"


model = vosk.Model(Find_Model())
samplerate = 16000
device = 1
q = queue.Queue()


def q_callback(indata, frames, time, status):
    if status:
        print(status,
              file=sys.stderr)
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate,
                           blocksize=800,
                           device=device,
                           dtype='int16',
                           channels=1,
                           callback=q_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json5.loads(rec.Result())["text"])

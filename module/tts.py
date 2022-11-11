import json
import torch
import sounddevice as sd
import time

language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000  # 48000
speaker = 'aidar'  # aidar, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu')  # cpu или gpu
model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)


def read_json():
    with open('config_.json', 'r', encoding='utf-8') as file:
        return json.load(file)


class TTSpeaker:
    def __init__(self):
        read_json()
        self._example_batch = 'привет ... меня  завут  п+око ... Йа тв+ой галсов+ой пам+ошник'
        self.stocks =  read_json()
        print(f'Голосовой помощник версии {self.stocks["version"]} готов нести службу\n')

    def load_bath(self, batch):
        self._example_batch = batch

    def va_speak(self):
        audio = model.apply_tts(text=self._example_batch + "...",
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo)
        sd.play(audio, sample_rate * 1.05)
        time.sleep((len(audio) / sample_rate) + 0.5)
        sd.stop()

# if __name__ == "__main__":
#     poko = TTSpeaker()
#     poko.va_speak()

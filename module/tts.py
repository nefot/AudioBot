import torch
import sounddevice as sd
import time

from module import cfg

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


class TTSpeaker:
    def __init__(self):
        self._example_batch = 'привет ... меня  завут  п+око ... Йа тв+ой галсов+ой пам+ошник'
        print(f'Голосовой помощник{cfg.VAP_name} версии {cfg.VAP_ver} готов нести службу\n')

    def load_bath(self, batch):
        self._example_batch = batch
        # for let in batch:
        #     if let in "1234567890":
        #         self._example_batch = "цифры исключенны"
        #         break

    def va_speak(self):
        audio = model.apply_tts(text=self._example_batch+"...",
                                speaker=speaker,
                                sample_rate=sample_rate,
                                put_accent=put_accent,
                                put_yo=put_yo)

        sd.play(audio, sample_rate * 1.05)
        time.sleep((len(audio) / sample_rate) + 0.5)
        sd.stop()

if __name__ == "__main__":
    poko = TTSpeaker()
    poko.va_speak()

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
import main
import time

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')


class MyApp(App):
    def build(self):
        return Button(text="Нажми, чтобы запустить помощника!!",
                      font_size=30,
                      on_press=self.btn_press,
                      background_color=[0, 0.8, 1, 2],
                      background_normal='')

    def btn_press(self, instance):
        instance.text = 'work'
        while True:
            main.start()


if __name__ == "__main__":
    MyApp().run()

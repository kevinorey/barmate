from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

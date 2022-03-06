from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder

# Builder.load_file('design.kv')

class TestApp(App):
    def build(self):
        return Button(text='Hello World')


TestApp().run()

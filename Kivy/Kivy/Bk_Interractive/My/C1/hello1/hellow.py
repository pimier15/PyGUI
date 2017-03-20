import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label

class HelloApp(App):
    def build(self):
        return Label (text = 'Hellw World')

if __name__ == '__main__':
    HelloApp().run()




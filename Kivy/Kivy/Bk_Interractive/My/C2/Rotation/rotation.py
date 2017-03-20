import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class RotationCanvas(RelativeLayout):
    pass

class RotationApp(App):
    def build(self):
        return RotationCanvas()

if __name__ == '__main__':
    RotationApp().run()


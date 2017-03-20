import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class StructureDraw(RelativeLayout):
    pass

class StructureApp(App):
    def build(self):
        return StructureDraw()

if __name__ == '__main__':
    StructureApp().run()

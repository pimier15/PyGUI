from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class ImageDraw(RelativeLayout):
    pass

class ImageApp(App):
    def build(self):
        return ImageDraw()

if __name__ == '__main__':
    ImageApp().run()






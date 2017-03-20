# File name: pagelayout.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class MyPageLayout(PageLayout):
    pass

class PageLayoutApp(App):
    def build(self):
        return MyPageLayout()

if __name__=="__main__":
    PageLayoutApp().run()

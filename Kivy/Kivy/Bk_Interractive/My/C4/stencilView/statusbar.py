import kivy
kivy.require('1.9.1')

# File name: statusbar.py
import kivy
kivy.require('1.9.1')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty

class StatusBar(BoxLayout):
    counter = NumericProperty(0)
    previous_counter = 0

    def on_counter(self, instnace, value):
        if value == 0:
            self.msg_text = 'drawing space cleared'
        elif value - 1 == self.__class__.previous_counter:
            self.msg_text = 'widger added'
        elif value + 1 == StatusBar.previous_counter:
            self.msg_text = 'widget removed'
        self.__class__.previous_counter = value




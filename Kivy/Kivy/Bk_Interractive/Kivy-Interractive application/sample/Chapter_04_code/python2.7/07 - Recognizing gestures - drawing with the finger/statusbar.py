# File name: statusbar.py
import kivy
kivy.require('1.9.0')
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class StatusBar(ButtonBehavior,BoxLayout):
    counter = NumericProperty(0)
    previous_counter = 0

    def on_counter(self, instance, value):
        if value == 0:
            self.msg_text = "Drawing space cleared"
        elif value - 1 == self.__class__.previous_counter:
            self.msg_text = "Widget added"
        elif value + 1 == StatusBar.previous_counter:
            self.msg_text = "Widget removed"
        self.previous_counter = value


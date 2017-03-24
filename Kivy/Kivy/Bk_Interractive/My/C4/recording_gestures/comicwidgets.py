# File name: comicwidgets.py
import kivy
kivy.require('1.9.0')
from kivy.uix.scatter import Scatter
from kivy.graphics import Line

class DraggableWidget(Scatter):
    def __init__(self,  **kwargs):
        self.selected = None
        self.touched = False
        super(DraggableWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.touched = True
            self.select()
            super(DraggableWidget, self).on_touch_down(touch)
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def select(self):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0,0,self.width,self.height), dash_offset=2)

    def on_pos(self,instance,calue):
            if self.selected and self.touched:
                go = self.parent.general_options
                go.translation = (self.center_x - self.ix, self.center_y - self.iy)
                self.ix = self.center_x
                self.iy = self.center_y

    def on_rotation(self,instance,value):
        for child in self.drawing_space.children:
           if child.selected and not cild.touched:
               child.rotaton = value

    def on_scale(self,instance,value):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
               child.scale = value

    def on_translate(self, x, y):
        for child in self.drawing_space.children:
            if child.selected and not child.touched:
                child.translate(*self.translation)

    def on_touch_up(self, touch):
        self.touched = False
        if self.selected:
            if not self.parent.general_options.group_mode:
                self.unselect()
        return super(DraggableWidget, self).on_touch_up(touch)

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected = None

class StickMan(DraggableWidget):
    pass

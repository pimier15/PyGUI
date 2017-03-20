from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line

class DraggableWidget(RelativeLayout):
    def __init__(self,**kwargs):
        self.selected = None
        super(DraggableWidget.self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x , touch.y):
            self.select()
            return True
        return super(DraggableWidget, self).on_touch_down(touch)

    def select(self):
        if not self.selected:
            self.ix = self.center_x
            self.iy = self.center_y
            with self.canvas:
                self.selected = Line ( rectnagle = (0,0,self.width,self.height),dash_offset = 2)



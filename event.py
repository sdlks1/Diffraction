from vpython import *


class Label:
    def __init__(self, txt):
        self.label = wtext(text=txt)
    def modify(self, txt):
        self.label.text = txt

class Slider:
    def __init__(self, min, max, step, length, bind):
        self.slider_ = slider(min=min, max=max, step=step, length=length, bind=bind)
    def modify(self, txt):
        self.slider_.value = txt
    def value(self):
        return self.slider_.value

class Event:
    def __init__(self):
        self.events = []
        self.buffer = []
    def push_N(self):
        self.events.append('N')
    def push_S(self):
        self.events.append('S')
    def push_Lambda(self):
        self.events.append('L')
    def push_D(self):
        self.events.append('D')
    def push_Sim(self):
        self.events.append("sim")

    def push_L_input(self):
        self.events.append("L in")
    def push_D_input(self):
        self.events.append("D in")
    
    def pop(self):
        self.buffer.append(self.events[0])
        del self.events[0]

event = Event()

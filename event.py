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
        self.events.append('N')  # Slit Number
    def push_S(self):
        self.events.append('S')  # Slit Spacing
    def push_L(self):
        self.events.append('L')  # Wavelength (Lambda)
    def push_D(self):
        self.events.append('D')  # Distance between slit and image
    def push_Sim(self):
        self.events.append("sim")  # Status Label
    
    def pop(self):
        self.buffer.append(self.events[0])
        del self.events[0]

event = Event()

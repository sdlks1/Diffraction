from vpython import *
import colour
import numpy as np

class Pixel:
    def __init__(self, pos: cyvector.vector, color_: cyvector.vector, image_res: int) -> None:
        self.pixel = box(pos=pos, color=color_, height=10, width=.5, length=image_res)
        self.color = color_
        self.illumination = vec(0, 0, 0)

class Slit:
    def __init__(self, pos: cyvector.vector) -> None:
        self.slit = sphere(pos=pos, color=color.red, radius=.5, visible=False)

class Renderer:
    def __init__(self, image_res: int) -> None:
        # Attributes
        self.attributes = {
            'N': 0,  # Slit Number
            'S': 0,  # Slit Spacing
            'L': 0,  # Wave Length
            'D': 0   # Distance from Slit to Image Plane
        }

        self.IMAGE_RES = image_res
        self.pixels = []
        self.slits = []
    
    def set_(self, attribute: str, value: int) -> None:
        self.attributes[attribute] = value
    
    def get_(self, attribute: str) -> int:
        return self.attributes[attribute]

    def wv_to_rgb(self) -> cyvector.vector:
        wavelength = float(self.get_('L'))

        if wavelength >= 380 and wavelength <= 440:
            attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
            R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
            G = 0.0
            B = (1.0 * attenuation) ** gamma
        elif wavelength >= 440 and wavelength <= 490:
            R = 0.0
            G = ((wavelength - 440) / (490 - 440)) ** gamma
            B = 1.0
        elif wavelength >= 490 and wavelength <= 510:
            R = 0.0
            G = 1.0
            B = (-(wavelength - 510) / (510 - 490)) ** gamma
        elif wavelength >= 510 and wavelength <= 580:
            R = ((wavelength - 510) / (580 - 510)) ** gamma
            G = 1.0
            B = 0.0
        elif wavelength >= 580 and wavelength <= 645:
            R = 1.0
            G = (-(wavelength - 645) / (645 - 580)) ** gamma
            B = 0.0
        elif wavelength >= 645 and wavelength <= 750:
            attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
            R = (1.0 * attenuation) ** gamma
            G = 0.0
            B = 0.0
        else:
            R = 0.0
            G = 0.0
            B = 0.0

        return vec(int(R), int(G), int(B))
    
    def render(self) -> None:
        self.pixels.clear()
        p0 = -30 + self.IMAGE_RES / 2
        for cnt in range(60 // self.IMAGE_RES):
            self.pixels.append(Pixel(vec(p0 + cnt * self.IMAGE_RES, 0, 0), self.wv_to_rgb(), self.IMAGE_RES))
        
        self.slits.clear()
        p0 = (1 - self.get_('N')) * self.get_('S') / 2
        for cnt in range(self.get_('N')):
            self.slits.append(Slit(vec(p0 + cnt * self.get_('S'), 0, self.get_('D'))))
    
    def simulate(self) -> None:
        self.render()

        for slit in self.slits:
            for pixel in self.pixels:
                length = mag(slit.slit.pos - pixel.pixel.pos)
                c = cos((length / self.get_('L')) * 2 * pi)
                s = sin((length / self.get_('L')) * 2 * pi)
                pixel.illumination += vec(c, s, 0)
        
        for pixel in self.pixels:
            illumination = mag(pixel.illumination) / self.get_('N')
            c = pixel.color * illumination
            pixel.pixel.color = vec(c, c, c)
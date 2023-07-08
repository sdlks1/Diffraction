from vpython import *
import colour
import numpy as np

class Pixel:
    def __init__(self, pos, color_, image_res: int) -> None:
        self.pixel = box(pos=pos, color=color_, height=10, width=.5, length=image_res)
        self.color = color_
        self.illumination = vec(0, 0, 0)

class Slit:
    def __init__(self, pos) -> None:
        self.slit = sphere(pos=pos, color=color.red, radius=.5, visible=False)

class Renderer:
    def __init__(self, image_res: int) -> None:
        # Attributes
        self.attributes = {
            'N': 2,  # Slit Number
            'S': 1,  # Slit Spacing
            'L': 380,  # Wave Length
            'D': 100   # Distance from Slit to Image Plane
        }

        self.IMAGE_RES = image_res
        self.pixels = []
        self.slits = []
    
    def set_(self, attribute: str, value: int) -> None:
        self.attributes[attribute] = value
    
    def get_(self, attribute: str) -> int:
        return self.attributes[attribute]

    def wv_to_rgb(self):
        wavelength = float(self.get_('L'))

        illuminant_XYZ = np.array([0.34570, 0.35850])
        illuminant_RGB = np.array([0.31270, 0.32900])
        chromatic_adaptation_transform = "Bradford"
        matrix_XYZ_to_RGB = np.array(
            [
                [3.24062548, -1.53720797, -0.49862860],
                [-0.96893071, 1.87575606, 0.04151752],
                [0.05571012, -0.20402105, 1.05699594]
            ]
        )

        RGB = colour.XYZ_to_RGB(
            colour.wavelength_to_XYZ(wavelength),
            illuminant_XYZ,
            illuminant_RGB,
            matrix_XYZ_to_RGB,
            chromatic_adaptation_transform
        )  

        return [RGB[0], RGB[1], RGB[2]]
    
    def render(self) -> None:
        self.pixels.clear()
        p0 = -30 + self.IMAGE_RES / 2
        for cnt in range(int(60 / self.IMAGE_RES)):
            self.pixels.append(Pixel(vec(p0 + cnt * self.IMAGE_RES, 0, 0), color.black, self.IMAGE_RES))
        
        self.slits.clear()
        p0 = (1 - self.get_('N')) * self.get_('S') / 2
        for cnt in range(self.get_('N')):
            self.slits.append(Slit(vec(p0 + cnt * self.get_('S'), 0, self.get_('D'))))
    
    def simulate(self) -> None:
        self.render()

        rgb = self.wv_to_rgb()
        print(rgb[0])

        for slit in self.slits:
            for pixel in self.pixels:
                length = mag(slit.slit.pos - pixel.pixel.pos)
                c = cos((length / self.get_('L')) * 2 * pi)
                s = sin((length / self.get_('L')) * 2 * pi)
                pixel.illumination += vec(c, s, 0)
        
        for pixel in self.pixels:
            pixel.color = rgb

            illumination = mag(pixel.illumination) / self.get_('N')
            pixel.pixel.color = vec(rgb[0]*illumination, rgb[1]*illumination, rgb[2]*illumination)
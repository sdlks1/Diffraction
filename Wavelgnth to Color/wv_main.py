from vpython import *
import colour
import numpy as np

scene = canvas(width=1024, height=768, background=color.black)

illuminant_XYZ = np.array([0.34570, 0.35850])
illuminant_RGB = np.array([0.31270, 0.32900])
chromatic_adaptation_transform = "Bradford"
matrix_XYZ_to_RGB = np.array(
    [
        [3.24062548, -1.53720797, -0.49862860],
        [-0.96893071, 1.87575606, 0.04151752],
        [0.05571012, -0.20402105, 1.05699594],
    ]
)
RGB = colour.XYZ_to_RGB(
    colour.wavelength_to_XYZ(560.0),
    illuminant_XYZ,
    illuminant_RGB,
    matrix_XYZ_to_RGB,
    chromatic_adaptation_transform,
)  
print(RGB)

b = box(color=vec(RGB[0]*0.01, RGB[1]*.01, RGB[2]*.01), pos=vec(0,0,0))

# print(colour.XYZ_to_RGB(colour.wavelength_to_XYZ(380.0)))
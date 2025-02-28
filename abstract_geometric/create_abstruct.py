# https://hub.2i2c.mybinder.org/user/sepandhaghighi-samila-8ihk2b99/lab/tree/examples/demo.ipynb

import math
import random

from samila import GenerativeImage, Projection, Marker, GenerateMode


def f1_1(x, y):
    result = random.gauss(0, 1) * math.sin(y) + (x + y) * random.uniform(-1, 1)
    return result


def f2_1(x, y):
    result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1)
    return result


def f1_2(x, y):
    result = random.uniform(-1, 1) * x ** 2 - math.sin(y ** 2) + abs(y - x)
    return result


def f2_2(x, y):
    result = random.uniform(-1, 1) * y ** 3 - math.cos(x ** 2) + 2 * x
    return result


# Generation Mode: F1_VS_F2, F2_VS_F1, F1_VS_INDEX, F2_VS_INDEX, INDEX_VS_F1, INDEX_VS_F2, F1_VS_X1, F1_VS_X2, F2_VS_X1,
# F2_VS_X2, X1_VS_F1, X1_VS_F2, X2_VS_F1, X2_VS_F2, F1F2_VS_F1, F1F2_VS_F2 and RANDOM

# Projection: RECTILINEAR, POLAR, AITOFF, HAMMER, LAMBERT, MOLLWEIDE and RANDOM

# Marker: POINT, PIXEL, CIRCLE, TRIANGLE_DOWN, TRIANGLE_UP, TRIANGLE_LEFT, TRIANGLE_RIGHT, TRI_DOWN, TRI_UP, TRI_LEFT,
# TRI_RIGHT, OCTAGON, SQUARE, PENTAGON, PLUS, PLUS_FILLED, STAR, HEXAGON_VERTICAL, HEXAGON_HORIZONTAL, X, X_FILLED,
# DIAMOND, DIAMON_THIN, VLINE, HLINE and RANDOM

# Rotation
# Range
# Color

g = GenerativeImage(f1_1, f2_1)
g.generate()
g.plot(color="white", bgcolor="black", projection=Projection.POLAR)
g.save_image(file_adr="test.png")

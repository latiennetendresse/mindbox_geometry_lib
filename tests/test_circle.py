from geometry.figures.circle import Circle
import math

def test_circle_area():
    c = Circle(2)
    assert round(c.area(), 5) == round(math.pi * 4, 5)

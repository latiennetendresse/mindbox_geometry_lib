from geometry.factory import create_shape
from geometry.figures.circle import Circle
from geometry.figures.triangle import Triangle

def test_create_circle():
    shape = create_shape(3)
    assert isinstance(shape, Circle)
    assert round(shape.area(), 2) > 0

def test_create_triangle():
    shape = create_shape(3, 4, 5)
    assert isinstance(shape, Triangle)
    assert round(shape.area(), 2) == 6.00

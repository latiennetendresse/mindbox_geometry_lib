from geometry.figures.triangle import Triangle

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert round(t.area(), 2) == 6.00

def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_triangle_not_right():
    t = Triangle(5, 5, 6)
    assert not t.is_right()

from geometry.figures.circle import Circle
from geometry.figures.triangle import Triangle
from geometry.base import Shape

def create_shape(*args) -> Shape:
    if len(args) == 1:
        return Circle(*args)
    elif len(args) == 3:
        return Triangle(*args)
    else:
        raise ValueError("Unsupported number of arguments")

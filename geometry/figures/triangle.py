import math
from geometry.base import Shape
from geometry.utils import is_right_triangle

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides.")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        return is_right_triangle(self.a, self.b, self.c)

    @staticmethod
    def _is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

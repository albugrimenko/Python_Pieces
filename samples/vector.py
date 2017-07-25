"""
    A simple two-dimentional vector representation
    with basic math operations defined
"""

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        """ Return the Euclidean norm, sqrt(x*x + y*y).
            This is the length of the vector from the origin to point (x, y).
        """
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)


def ttest_basic():
    """ basic tests """
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print("v1: ", v1)
    print("v2: ", v2)
    print("v1 + v2 = ", v1 + v2)
    print("abs(v1) = ", abs(v1))
    print("bool(v1) = ", bool(v1))
    print("v1 * 3 = ", v1 * 3)


if __name__ == "__main__":
    ttest_basic()

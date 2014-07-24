"""
Basic operations:

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
    >>> bool(v)
    True
    >>> bool(Vector(0,0))
    False

Supported:

    >>> 3 * v
    Vector(9, 12)

Solve the problem in vector2d v.0.2 by explicitly disallowing the use
of * with two vectors:

    >>> Vector(1, 2) * Vector(3, 4)
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for *: 'Vector' and 'Vector'

"""


from math import hypot
from numbers import Real

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        if isinstance(scalar, Real):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar


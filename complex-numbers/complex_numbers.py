import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f'({self.real}, {self.imaginary})'

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return (self.real == other.real and
                    self.imaginary == other.imaginary)
        return False

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real -
                             self.imaginary * other.imaginary,
                             self.imaginary * other.real +
                             self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber((self.real * other.real +
                             self.imaginary * other.imaginary) /
                             (other.real ** 2 + other.imaginary ** 2),
                             (self.imaginary * other.real -
                             self.real * other.imaginary) /
                             (other.real ** 2 + other.imaginary ** 2))

    def __abs__(self):
        return (self.real * self.real +
                self.imaginary * self.imaginary) ** (1/2)

    def conjugate(self):
        return ComplexNumber(self.real, self.imaginary * -1)

    def exp(self):
        return ComplexNumber(math.exp(self.real) * math.cos(self.imaginary),
                             math.sin(self.imaginary))

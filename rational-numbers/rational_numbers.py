from __future__ import division

class Rational(object):
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    def __init__(self, a, b):
        if b == 0:
            raise Exception("Denominator cannot be zero")
        else:
            g = self.gcd(a, b)
            self.numer = a / g
            self.denom = b / g
     
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, 
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, 
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
    
    
    
    



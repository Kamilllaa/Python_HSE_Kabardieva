class Complex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def __str__(self):
        if self.im < 0:
            return f"{self.re} - {abs(self.im)}i"
        return f"{self.re} + {self.im}i"

    def __eq__(self, c):
        return self.re == c.re and self.im == c.im

    def add(self, c):
        return Complex(self.re + c.re, self.im + c.im)

    def sub(self, c):
        return Complex(self.re - c.re, self.im - c.im)

    def mul(self, c):
        return Complex(self.re * c.re - self.im * c.im, self.re * c.im + self.im * c.re)

    def div(self, c):
        if c.re != 0 or c.im != 0:
            denom = Complex(c.re, -c.im)
            new_denom = c.mul(denom)
            new_num = self.mul(denom)
            return Complex(new_num.re / new_denom.re, new_num.im / new_denom.re)

    def abs(self):
        return (self.re * self.re + self.im * self.im)**0.5

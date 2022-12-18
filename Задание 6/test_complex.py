import unittest
from complex import Complex

class TestComplex(unittest.TestCase):
    def test_add(self):
        a = Complex(5, -2)
        b = Complex(4, -2)
        result = Complex(9, -4)
        self.assertEqual(a.add(b), result)

    def test_sub(self):
        a = Complex(9, -7)
        b = Complex(1, 5)
        result = Complex(8, -12)
        self.assertEqual(a.sub(b), result)

    def test_mul(self):
        a = Complex(1, 1)
        b = Complex(1, -1)
        result = Complex(2, 0)
        self.assertEqual(a.mul(b), result)

    def test_div(self):
        a = Complex(4, 5)
        b = Complex(0, 1)
        result = Complex(5, -4)
        self.assertEqual(a.div(b), result)

    def test_abs(self):
        c = Complex(3, 4)
        self.assertEqual(c.abs(), 5)

if __name__ == "__main__":
    unittest.main()

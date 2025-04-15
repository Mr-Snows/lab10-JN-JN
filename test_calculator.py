# https://github.com/Mr-Snows/lab10-JN-JN
# Partner 1: Jayci Nieves
# Partner 2: Jayci Nieves

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

def test_add(self):
    self.assertEqual(add(10, 5), 15)
    self.assertEqual(add(-1, -4), -5)

def test_subtract(self):
    self.assertEqual(subtract(7, 2), 5)
    self.assertEqual(subtract(2, 7), -5)

def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        divide(5, 0)

def test_logarithm(self):
    self.assertEqual(logarithm(2, 8), 3)

def test_log_invalid_base(self):
    with self.assertRaises(ValueError):
        logarithm(-2, 5)
    with self.assertRaises(ValueError):
        logarithm(1, 5)

def test_multiply(self):
    self.assertEqual(multiply(1, 5), 5)
    self.assertEqual(multiply(-1, 5), -5)

def test_divide(self):
    self.assertEqual(divide(5, 1), 5)
    self.assertEqual(divide(-15, 5), -3)

def test_log_invalid_argument(self):
    with self.assertRaises(ZeroDivisionError):
        logarithm(2,-5)

def test_hypotenuse(self):
    self.assertEqual(hypotenuse(3, 4), 5)
    self.assertEqual(hypotenuse(3, 8), 10)

def test_sqrt(self):
    self.assertEqual(square_root(4), 2)
    with self.assertRaises(ValueError):
        square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

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
        divide(0, 5)

def test_logarithm(self):
    self.assertEqual(logarithm(2, 8), 3)

def test_log_invalid_base(self):
    self.assertFalse(logarithm(-2, 5) is None)
    self.assertFalse(logarithm(1, 5) is None)

def test_multiply(self):
    self.assertEqual(multiply(1, 5), 5)
    self.assertEqual(multiply(-1, 5), -5)

def test_divide(self):
    self.assertEqual(divide(1, 5), 5)
    self.assertEqual(divide(-5, 15), -3)

def test_log_invalid_argument(self):
    with self.assertRaises(ZeroDivisionError):
        logarithm(2,-5)

def test_hypotenuse(self):
    self.assertEqual(hypotenuse(3, 4), 5)

def test_sqrt(self):
    self.assertEqual(square_root(4), 2)
   self.assertFalse(square_root(-4) is None)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

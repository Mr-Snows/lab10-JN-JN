# https://github.com/Mr-Snows/lab10-JN-JN
# Partner 1: Jayci Nieves
# Partner 2: Jayci Nieves

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-10, -5), -15)
        self.assertEqual(calculator.add(-5, 5), 0)
        self.assertEqual(calculator.add(2.5, 2.5), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-10, -5), 5)
        self.assertEqual(calculator.subtract(-5, 5), -10)
        self.assertEqual(calculator.subtract(2.5, 2.5), 0)
    
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, calculator.divide, 0, 10)
    
    def test_logarithm(self):
         self.assertEqual(calculator.logarithm(2, 8)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, calculator.logarithm, -1, 1)
        self.assertRaises(ValueError, calculator.logarithm,  0, 1)
        self.assertRaises(ValueError, calculator.logarithm, 1, 1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1, 5), 5)
        self.assertEqual(calculator.multiply(0, 5), 0)
        self.assertEqual(calculator.multiply(-1, 5), -5)
        self.assertEqual(calculator.multiply(10, 2), 20)

    def test_divide(self):
        self.assertEqual(calculator.divide(1, 5), 5)
        self.assertEqual(calculator.divide(0, 5), 0)
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertEqual(calculator.divide(-1, 5), -5)

    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, calculator.logarithm, 2, 0)
        self.assertRaises(ValueError, calculator.logarithm, 2, -1)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(-5), 5)


    def test_sqrt(self):
        self.assertEqual(calculator.square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()

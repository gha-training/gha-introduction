import unittest
import mathlib

class TestMathLib(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mathlib.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(mathlib.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(mathlib.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(mathlib.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            mathlib.divide(5, 0)

if __name__ == '__main__':
    unittest.main()

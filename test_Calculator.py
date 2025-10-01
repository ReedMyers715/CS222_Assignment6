import unittest
from Calculator import Calculator
class test_Calculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()
    def test_Add(self):
        self.assertEqual(self.c.add(2, 3), 5)
    def test_Subtract(self):
        self.assertEqual(self.c.subtract(10, 3), 7)
    def test_Multiply(self):
        self.assertEqual(self.c.multiply(10, 9), 90)
    def test_Divide(self):
        self.assertEqual(self.c.divide(27, 3), 9)
    def test_DivideByZero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.c.divide(10, 0))

if __name__ == '__main__':
    unittest.main()
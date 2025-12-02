import unittest
from calcolator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_add_positive_numbers(self):
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_add_negative_numbers(self):
        result = self.calc.add(-10, 5)
        self.assertEqual(result, -5)

    def test_subtract(self):
        result = self.calc.subtract(20, 7)
        self.assertEqual(result, 13)

    def test_multiply(self):
        result = self.calc.multiply(4, 8)
        self.assertEqual(result, 32)
        
    def test_divide_normal(self):
        result = self.calc.divide(100, 10)
        self.assertEqual(result, 10)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        
if __name__ == '__main__':
    unittest.main()
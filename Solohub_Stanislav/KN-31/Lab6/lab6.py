import unittest
from lab5 import get_discount

class TestDiscountSystem(unittest.TestCase):

    def test_high_price(self):
        result = get_discount(1500)
        expected = 150.0
        self.assertEqual(result, expected, "Знижка має бути 150 для ціни 1500")

    def test_low_price(self):
        result = get_discount(500)
        expected = 0
        self.assertEqual(result, expected, "Знижка має бути 0 для ціни 500")

    def test_boundary_price(self):
        result = get_discount(1000)
        expected = 0
        self.assertEqual(result, expected, "Знижка має бути 0 для ціни 1000")

if __name__ == '__main__':
    unittest.main()
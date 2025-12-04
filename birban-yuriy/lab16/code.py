def add(a, b):
    return a + b

import unittest
from my_module import add

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()
import unittest
from my_functions import add

class TestAddFunction(unittest.TestCase):
    """Клас для тестування функції 'add'."""

    def test_add_positive_numbers(self):
        """Перевірка додавання двох позитивних чисел (3 + 5 = 8)."""
        expected_result = 8
        actual_result = add(3, 5)
        self.assertEqual(actual_result, expected_result)

    def test_add_negative_numbers(self):
        """Перевірка додавання двох від'ємних чисел (-1 + -4 = -5)."""
        expected_result = -5
        actual_result = add(-1, -4)
        self.assertEqual(actual_result, expected_result)
        
    def test_add_zero_and_positive(self):
        """Перевірка додавання нуля (0 + 10 = 10)."""
        self.assertEqual(add(0, 10), 10)

if __name__ == '__main__':
    unittest.main()
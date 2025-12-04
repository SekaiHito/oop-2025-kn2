import unittest
import math_operations

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        #+
        self.assertEqual(math_operations.add(10, 5), 15)
        self.assertEqual(math_operations.add(-1, 1), 0)
        self.assertEqual(math_operations.add(-5, -5), -10)

    def test_subtract(self):
        #-
        self.assertEqual(math_operations.subtract(10, 5), 5)
        self.assertEqual(math_operations.subtract(-1, 1), -2)

    def test_multiply(self):
        #*
        self.assertEqual(math_operations.multiply(10, 5), 50)
        self.assertEqual(math_operations.multiply(10, 0), 0)

    def test_divide(self):
        #/
        self.assertEqual(math_operations.divide(10, 5), 2)
        self.assertEqual(math_operations.divide(5, 2), 2.5)

        #/0
        #edge cases - граничних випадків
        with self.assertRaises(ValueError):
            math_operations.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
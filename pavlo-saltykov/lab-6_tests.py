import unittest
from lab-6 import add, subtract, multiply, divide

class Tests(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(14, 32), 46)
        self.assertEqual(add(-11, 11), 0)
        
    def test_subtract(self):
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(0, 5), -5)
        
    def test_multiply(self):
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(-2, 3), -6)
        
    def test_divide(self):
        self.assertEqual(divide(100, 2), 50)
        self.assertRaises(ValueError, divide, 100, 0)

if __name__ == "__main__":
    unittest.main()

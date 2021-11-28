import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calc.subtract(5, 5)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = calc.multiply(10, 10)
        self.assertEqual(result, 100)

    def test_divide(self):
        result = calc.divide(5, 1)
        self.assertEqual(result, 5)
        
if __name__ == '__main__':
    unittest.main()

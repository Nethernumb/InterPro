#Mason Shaw
import unittest
from calc2 import *

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.result = Calculator(get_user_input(),get_user_input())

    def test_add(self):
        self.assertEqual(self.result.add(), 10)

    def test_subtract(self):
        self.assertEqual(self.result.subtract(), 0)

    def test_multiply(self):
        self.assertEqual(self.result.multiply(), 25)

    def test_divide(self):
        self.assertEqual(self.result.divide(), 10)

    def test_to_the_power_of(self):
        self.assertEqual(self.result.add(), 10)




if __name__ == "__main__":
    unittest.main()
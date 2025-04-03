#Mason Shaw
import unittest
from unittest import mock
from calc2 import *

class TestCalc(unittest.TestCase):
    @mock.patch("builtins.input", side_effect=['5', '5'])       #what mock does is simulate user input, so where input is, the 5, 5 is the input being simulated
    def setUp(self, mock_input):
        self.test_values = (get_user_input(), get_user_input()) ###right here
        self.result = Calculator(*self.test_values)

    def test_add(self):
        self.assertEqual(self.result.add(), 10)

    def test_subtract(self):
        self.assertEqual(self.result.subtract(), 0)

    def test_multiply(self):
        self.assertEqual(self.result.multiply(), 25)

    def test_divide(self):
        self.assertEqual(self.result.divide(), 1)

    def test_to_the_power_of(self):
        self.assertEqual(self.result.add(), 10)




if __name__ == "__main__":
    unittest.main()
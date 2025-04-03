import unittest
import calc
#-------------------------------------------------------------------------------------------#
# Intermediate Programming
# Unit Test - Part 1 
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
# First, you will need to complete the functions from the calc file.
# This can be simple input validation or exceptions, but make sure it "works as intended."
# Make sure to test the functions, you can do this under the if name-main section.
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
# Next, you will need to import the unittest module and import your functions from your
# calc file. Afterwards, write unit tests that test the validation. Make sure that this 
# covers edge cases too (e.g., strings, incorrect values, etc.)
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
# Lastly, review.
# What happens if a test fails? How do you debug it?
# Pair up with someone else and review each others test cases.
#-------------------------------------------------------------------------------------------#

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5,5), 10)
        self.assertEqual(calc.add(7,19), 26)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5,5), 0)
        self.assertEqual(calc.subtract(5,6), -1)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5,5), 25)
        self.assertEqual(calc.multiply(5,10), 50)
        self.assertEqual(calc.multiply(-5,-5), 25)

    def test_divide(self):
        self.assertEqual(calc.divide(5,5), 1)
        self.assertRaises(ZeroDivisionError, calc.divide, 5, 0)

    def test_to_the_power_of(self):
        self.assertEqual(calc.to_the_power_of(5,5), 3125)
        self.assertNotEqual(calc.to_the_power_of(5,5), 25)

    def test_square_root(self):
        self.assertEqual(calc.square_root(25), 5)



if __name__ == "__main__":
    unittest.main()
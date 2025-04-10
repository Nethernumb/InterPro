
import unittest
from unittest import mock
from shapecalc.shapes import *

class TestShape(unittest.TestCase):

    def test_circlearea(self):
        mycirc = Circle("Circle", 5)
        self.assertAlmostEqual(mycirc.circarea(), 78.5)
        
    def test_rectarea(self):
        myrec = Rectangle("rectangle", 5,5)
        self.assertEqual(myrec.recarea(), 25)

    def test_tri(self):
        mytri = Triangle("Triangle", 5, 5)
        self.assertEqual(mytri.triarea(), 12.5)

    def test_trap(self):
        mytrap = Trapezoid("Trapezoid", 5, 5, 5)
        self.assertEqual(mytrap.traparea(), 25)

if __name__ == "__main__":
    unittest.main(exit=False)   #This exit=False was because I was getting system exit errors from my tests not running correctly. 
                                #I can remove it, it doesn't really do anything. 
                                #Honestly, Im leaving this as is. I'm over it for today I don't ever want to see unit testing again in my life.
                                #Thank you for all your help Tom, I genuinely have no idea why the solution went right over my head but I really appreciate your help.
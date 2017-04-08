"""
B8IT105 Programming for Big Data
Assignment 1 - A 10 Function Calculator

Submitted by:
Deirdre Flaherty (10349680)
"""

import unittest
import calculator
import math

#Note: the functions have to start with 'test'
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = calculator.Calculator()
    
    #test to ensure 2+2=4, 5+3=8, 4+0=4, strings are handled
    def testAdd(self):
        self.assertEqual(self.calc.add(2,2),4)
        self.assertEqual(self.calc.add(5,3),8)
        self.assertEqual(self.calc.add(4,0),4)
        self.assertEqual(self.calc.add('fred',0),'error')
        self.assertEqual(self.calc.add('fred','mary'),'error')
        self.assertEqual(self.calc.add(0,'mary'),'error')
        
    #test to ensure 2-2=0, 5-3=2, 4-0=4, 3-4=-1, strings are handled
    def testSubract(self):
        self.assertEqual(self.calc.subtract(2,2),0)
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(4,0),4)
        self.assertEqual(self.calc.subtract(3,4),-1)
        self.assertEqual(self.calc.subtract('fred',0),'error')
        self.assertEqual(self.calc.subtract('fred','mary'),'error')
        self.assertEqual(self.calc.subtract(0,'mary'),'error')
        
    #test to ensure 2*2=4, 5*3=15, 4*0=4, 3*-4=-12, strings are handled
    def testMultiply(self):
        self.assertEqual(self.calc.multiply(2,2),4)
        self.assertEqual(self.calc.multiply(5,3),15)
        self.assertEqual(self.calc.multiply(4,0),0)
        self.assertEqual(self.calc.multiply(3,-4),-12)
        self.assertEqual(self.calc.multiply('fred',0),'error')
        self.assertEqual(self.calc.multiply('fred','mary'),'error')
        self.assertEqual(self.calc.multiply(0,'mary'),'error')
        
    #test to ensure 2/2=1, 5/3.0=1.6, 4/1=4, 4/0='undefined', strings are handled
    def testDivide(self):
        self.assertEqual(self.calc.divide(2,2),1)
        self.assertEqual(self.calc.divide(5,3.0),1.6666666666666667)
        self.assertEqual(self.calc.divide(4,1),4)
        self.assertEqual(self.calc.divide(4,0),'undefined')
        self.assertEqual(self.calc.divide('fred',0),'error')
        self.assertEqual(self.calc.divide('fred','mary'),'error')
        self.assertEqual(self.calc.divide(0,'mary'),'error')
        
    #test to ensure 2**2=4, 5**3=125, 4**1=4, 4**0=1, 2**-2=0.25, strings are handled
    def testExponent(self):
        self.assertEqual(self.calc.exponent(2,2),4)
        self.assertEqual(self.calc.exponent(5,3),125)
        self.assertEqual(self.calc.exponent(4,1),4)
        self.assertEqual(self.calc.exponent(4,0),1)
        self.assertEqual(self.calc.exponent(2,-2),0.25)
        self.assertEqual(self.calc.exponent('fred',0),'error')
        self.assertEqual(self.calc.exponent('fred','mary'),'error')
        self.assertEqual(self.calc.exponent(0,'mary'),'error')
        
    #test to ensure 2**2=4, 5**2=25, 4**2=16, -2**2=4, strings are handled
    def testSquare(self):
        self.assertEqual(self.calc.square(2),4)
        self.assertEqual(self.calc.square(5),25)
        self.assertEqual(self.calc.square(4),16)
        self.assertEqual(self.calc.square(-2),4)
        self.assertEqual(self.calc.square('fred'),'error')
        
    #test to ensure 2**3=8, 5**3=125, 4**3=64, -2**3=-8, strings are handled
    def testCube(self):
        self.assertEqual(self.calc.cube(2),8)
        self.assertEqual(self.calc.cube(5),125)
        self.assertEqual(self.calc.cube(4),64)
        self.assertEqual(self.calc.cube(-2),-8)
        self.assertEqual(self.calc.cube('fred'),'error')
        
        #test to ensure 4**0.5=2, 25**0.5=5, 5**0.5=2.23606797749979, negative numbers & strings are handled
    def testSquareRoot(self):
        self.assertEqual(self.calc.squareroot(4),2)
        self.assertEqual(self.calc.squareroot(25),5)
        self.assertEqual(self.calc.squareroot(5),2.23606797749979)
        self.assertEqual(self.calc.squareroot(-4),'error')
        self.assertEqual(self.calc.squareroot('fred'),'error')
        
    #test sin(3)=0.1411200080598672, sin(-3)=-0.1411200080598672, sin(0)=0.0, sin(pi/2)=1.0, strings are handled
    def testSine(self):
        self.assertEqual(self.calc.sine(3),0.1411200080598672)
        self.assertEqual(self.calc.sine(-3),-0.1411200080598672)
        self.assertEqual(self.calc.sine(0),0.0)
        self.assertEqual(self.calc.sine(math.pi/2),1.0)
        self.assertEqual(self.calc.sine('fred'),'error')
        
    #test cos(3)=-0.9899924966004454, cos(-3)=-0.9899924966004454, cos(0)=1.0, cos(pi)=-1.0, cos(pi*2)=1.0, strings are handled
    def testCosine(self):
        self.assertEqual(self.calc.cosine(3),-0.9899924966004454)
        self.assertEqual(self.calc.cosine(-3),-0.9899924966004454)
        self.assertEqual(self.calc.cosine(0),1.0)
        self.assertEqual(self.calc.cosine(math.pi),-1.0)
        self.assertEqual(self.calc.cosine(math.pi*2),1.0)
        self.assertEqual(self.calc.cosine('fred'),'error')
        
#this line says that if this is run from the command line, then invoke this fxn
#otherwise, return nothing
if __name__ == '__main__':
    unittest.main()
    


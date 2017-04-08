"""
B8IT105 Programming for Big Data
Assignment 1 - A 10 Function Calculator

Submitted by:
Deirdre Flaherty (10349680)
"""

import math

class Calculator(object):

    #Function1: add two numbers together
    def add(self, first, second):
        number_types = (int, long, float, complex)
        if isinstance(first, number_types) and isinstance(second, number_types):
            return first + second
        else:
            return 'error'
        
    #Function2: subtract one number from another
    def subtract(self, first, second):
        number_types = (int, long, float, complex)
        if isinstance(first, number_types) and isinstance(second, number_types):
            return first- second
        else:
            return 'error'
    
    #Function3: multiply two numbers
    def multiply(self, first, second):
        number_types = (int, long, float, complex)
        if isinstance(first, number_types) and isinstance(second, number_types):
            return first * second
        else:
             return 'error'
    
    #Function4: divide one number by another
    def divide(self, first, second):
        number_types = (int, long, float, complex)
        if isinstance(first, number_types) and isinstance(second, number_types):
            if second == 0:
                return 'undefined'
            else:
                return first / float(second)
        else:
            return 'error'
    
    #Function5: exponentiate one number by another
    def exponent(self, first, second):
        number_types = (int, long, float, complex)
        if isinstance(first, number_types) and isinstance(second, number_types):
            return first ** second
        else:
            return 'error'
        
    #Function6: sqare a number
    def square(self, num):
        number_types = (int, long, float, complex)
        if isinstance(num, number_types):
            return num ** 2
        else:
            return 'error'
            
    #Function7: cube a number
    def cube(self, num):
        number_types = (int, long, float, complex)
        if isinstance(num, number_types):
            return num ** 3
        else:
            return 'error'
            
    #Function8: get the sqare root of a number (exponentiate by 0.5)
    def squareroot(self, num):
        number_types = (int, long, float, complex)
        if isinstance(num, number_types):
            #negative numbers cannot be raised to a fractional power
            if num < 0:
               return 'error'
            else:
                return num ** 0.5
        else:
            return 'error'
    
    #Function9: return the sine of x radians
    def sine(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.sin(x)
        else:
            return 'error'
    
    #Function10: return the cosine of x radians
    def cosine(self, x):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types):
            return math.cos(x)
        else:
            return 'error'
    
    def printMenu(self):
        print "Please select an operation from the menu below:"
        print "1: Add"
        print "2: Subtract"
        print "3. Multiply"
        print "4. Divide"
        print "5. Exponent"
        print "6. Square"
        print "7. Cube"
        print "8. Square Root"
        print "9. Sine"
        print "10. Cosine"
        print "Enter Q to quit"
        
        
        


    



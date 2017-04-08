# -*- coding: utf-8 -*-
"""
B8IT105 Programming for Big Data
Assignment 1 - A 10 Function Calculator

Submitted by:
Deirdre Flaherty (10349680)
"""

import calculator

print "##################################################"
print "#     Welcome to Deirdre's Python Calculator!    #"
print "##################################################"

myCalc = calculator.Calculator()

#function to get a number from the user
def getNumber(message):
    while True:
        str_input = raw_input(message)
        try:
            fl_input = float(str_input)
            break
        except:
            print "Bad input"
            continue
    return fl_input

#start the user interface
while True:
    
    #print options
    myCalc.printMenu()
    
    #get choice of operation from user
    str_input = raw_input("Please enter a number from 1 to 10:")
    if str_input.lower() == 'q':
        break
    try:
        int_choice = int(str_input)
    except:
        print 'Bad input, please enter an integer'
        raw_input("Press any key to return to the main menu\n")
        continue
    if int_choice < 1 or int_choice > 10:
        print 'Invalid input, please enter a number between 1 and 10'
        raw_input("Press any key to return to the main menu\n")
        continue
    
    #get input for calculator function from user
    if int_choice in range (1,6):
        message = "Please enter the first operand:"
        first = getNumber(message)
        message = "Please enter the second operand:"
        second = getNumber(message)
    elif int_choice in range(6,9):
        message = "Please enter a number:"
        num = getNumber(message)
    else:
        message = "Please enter the number of radians:"
        num = getNumber(message)
    
    #invoke calculator function
    if int_choice == 1:
        result = myCalc.add(first, second)
        print "{} added to {} is equal to {}".format(first, second, result)
    elif int_choice == 2:
        result = myCalc.subtract(first, second)
        print "{} minus {} is equal to {}".format(first, second, result)
    elif int_choice == 3:
        result = myCalc.multiply(first, second)
        print "{} multiplied by {} is equal to {}".format(first, second, result)
    elif int_choice == 4:
        result = myCalc.divide(first, second)
        print "{} divided by {} is equal to {}".format(first, second, result)
    elif int_choice == 5:
        result = myCalc.exponent(first, second)
        print "{} to the power of {} is equal to {}".format(first, second, result)
    elif int_choice == 6:
        result = myCalc.square(num)
        print "{} squared is equal to {}".format(num, result)
    elif int_choice == 7:
        result = myCalc.cube(num)
        print "{} cubed is equal to {}".format(num, result)
    elif int_choice == 8:
        result = myCalc.squareroot(num)
        print "The square root of {} is equal to {}".format(num, result)
    elif int_choice == 9:
        result = myCalc.sine(num)
        print "The sine of {} radians is equal to {}".format(num, result)
    else:
        result = myCalc.cosine(num)
        print "The cosine of {} radians is equal to {}".format(num, result)
    
    #check if user wants to continue
    if 'q' == raw_input("Q to quit / Any other key to continue> ").lower():
        break

    
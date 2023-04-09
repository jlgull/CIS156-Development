#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 10, Assignment Part A
# Program name: carpet_cost.py

"""
Part A

Create a program called carpet_cost.py that:

    Input #1: Prompts the user for the length of a room that was carpeted.
    Input #2: Prompts the user for the width of the room that was carpeted.
    Input #3: Prompts the use for the amount spent on carpeting.
    Calculates the area of the carpet (length x width).
    Calculates the cost per square foot (cost / area).
    Use try and at least two except statement two handle two probable problem areas.
    A relevant error message is to be displayed to the user:
        if the value entered for length and/or width is 0; the error message for this
            condition must include the word zero,
        if a non-number is entered for length, width, or cost;
            the error message for this condition must include the word non-number.
    Outputs the area and cost per square foot to the user. Dollar values must display
        two decimal places (refer to zyBooks, chapter 7.2, on floating-point precision)

Examples (note that your program does not need to look, or behave, like exactly like these
    examples - they're here to show that all error conditions are caught and that, when there is no error condition,
    the result is outputted):

"""
#
# Import all required options
#
# Define functions and Import modules as required.

def clear():
    # Import system and name from the os module.
    from os import system, name

    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # If Windows, cls is used, else clear (for Mac and Linux)
    (system('cls')) if name == 'nt' else (system('clear'))

# Variable List
#
# Integer Variables
#
#
#
# Floating Variables
#
#
#
# String Variables
#
#
#
# List Variables
#
#

#
# Preset any variables that need to be created prior to first use.
#


# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"
while do_again != "N":
    # Clear screen and start main program.
    #
    clear()


# Beginning of code


    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or a N.")

# End of program

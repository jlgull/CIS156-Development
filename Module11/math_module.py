#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 11, Assignment Part B
# Program name: math_module.py

"""
Part B

Create a program called math_module.py that uses the math module
    (https://docs.python.org/3.5/library/math.html Links to an external site.) to do the following:

    Prompt the user to enter a number.
    Calculate and output the absolute value of the entered number using a function from the math module.
        For example, the absolute value of 4 is 4.0 and the absolute value of -4 is 4.0.
    Calculate and output the square root of the entered number using a function from the math module.
        For example: the square root of 4 is 2.0 and the square root of 12 is 3.4641016151377544.
        Note that Python cannot calculate the square root of a negative number,
            so you will have to take steps to handle that scenario.

Do not format the output; simply display the output form the math function.

Hint: You may find the w3schools Links to an external site.or Python Links to an
    external site.math module references helpful.

Example (note that your program does not need to look, or behave, like exactly like this example -
    it is here to show you one way it might look when the program runs properly):

"""
#
# Import all required options
#
from math import fabs, sqrt
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
# base_number       - The basic entry converted to a floating point number.
#
# String Variables
#
# base_number_1     - The basic entry, to be able to display a string value if required.
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

# Clear screen and start main program.
#
clear()

while do_again != "N":

    print(f"\nThis program will accept any signed number, either integer or floating point, and "
          "\nprint the absolute value of the signed number and then the square root of the absolute value.")

    try:
        # Input to gather a signed numeric value.

        base_number_1 = input(f"\nEnter a signed number: ")
        base_number = float(base_number_1)
    except ValueError:
        print(f"The entry, {base_number_1}, was not a signed number, please try again.")
        continue

    print(f"\nThe floating point number entered was {base_number}."
          f"\n\tThe absolute value of the entered number is {fabs(base_number)}."
          f"\n\tThe square root of the entered number is {sqrt(fabs(base_number))}")


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

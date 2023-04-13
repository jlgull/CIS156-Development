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
    Use try and at least two except statement to handle two probable problem areas.
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
# length    - Length of the room carpeted.
# width     - Width of the room carpeted.
# carpet_cost - Cost for the carpet installed
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

length = width = carpet_cost = 0.00

# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"

# Clear screen and start main program.
#
clear()

while do_again != "N":

    """
        Input #1: Prompts the user for the length of a room that was carpeted.
        Input #2: Prompts the user for the width of the room that was carpeted.
        Input #3: Prompts the use for the amount spent on carpeting.
        
        Use try and at least two except statement to handle two probable problem areas.
            A relevant error message is to be displayed to the user:
            if the value entered for length and/or width is 0; the error message for this
            condition must include the word zero,
            if a non-number is entered for length, width, or cost;
            the error message for this condition must include the word non-number.
    """

    # Beginning of code

    try:
        length = float(input(f"\nEnter the length of a room, in feet, that was carpeted: "))
        width = float(input("Enter the width of a room, in feet, that was carpeted: "))
    except  ValueError:
        print("You entered non-number data.")
        continue
    try:

        # Test that the data is above the lower_limit set above.
        if length <= 0 or width <= 0:
            raise ValueError(f"The room can not have a zero dimension.")
    except ValueError as error_feedback:
        print(error_feedback)
        continue

    try:
        carpet_cost = float(input("Enter the amount spent on carpeting: "))
    except  ValueError:
        print("You entered non-number data.")
        continue
    """
    Calculates the area of the carpet (length x width).
    Calculates the cost per square foot (cost / area).
    """

    area = length * width
    cost_per_sq_ft = carpet_cost / area

    """"
        Outputs the area and cost per square foot to the user. Dollar values must display
        two decimal places (refer to zyBooks, chapter 7.2, on floating-point precision)
        Printing the output
    """

    print(f"\nThe area of the room was {area} Sq.Ft")
    print(f"\tWith the cost per Sq.Ft being ${cost_per_sq_ft:.2f}")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or a N.")

# End of program

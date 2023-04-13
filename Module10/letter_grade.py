#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 10, Assignment Part B
# Program name: letter_grade.py

"""

Part B

Create a program called letter_grade.py that:

    Prompts the user for their current grade percentage (e.g.: 92).
    Determines the letter grade. The letter grade must be uppercase. For the purposes of this program, letter grades are:
        90 - 100 =  A
        80 - 89 =   B
        70 - 79 =   C
        60 - 69 =   D
        less than 60 =   F
    Within a try-except structure, raise two different exceptions. Note that there are three listed,
            and they must all be handled. Exceptions must be raised for at least two of them.
            The third can be handled however you wish.
            Note that you can use ValueError (as described in zyBooks 10.3) and do not need
            to create a custom exception (as described in 10.6).
        for an input less than zero; the error message must include the word zero,
        for an input greater than 100; the error message must include the words one hundred,
        for an input that is not a number; the error message must include the word non-number.

Examples (note that your program does not need to look, or behave, like exactly like these examples -
    they're here to show that all error conditions are caught and that, when there is no error condition,
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
# grade             - Floating point grade value entered.
#
# String Variables
#
# letter_grade      - Letter grade for the floating point grade entered.
# grade_1           - Grade value entered, to be able to display non-number entry values.
#
# List Variables
#
#

#
# Preset any variables that need to be created prior to first use.
#
grade_1 = ""
grade = 0.0

# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"

# Clear screen and start the program.
#

clear()

while do_again != "N":

    # Beginning of code

    """
        Create a program called letter_grade.py that:
    
        Prompts the user for their current grade percentage (e.g.: 92).
        Within a try-except structure, raise two different exceptions. Note that there are three 
            listed,
                and they must all be handled. Exceptions must be raised for at least two of them.
                The third can be handled however you wish.
                Note that you can use ValueError (as described in zyBooks 10.3) and do not need
                to create a custom exception (as described in 10.6).
            for an input less than zero; the error message must include the word zero,
            for an input greater than 100; the error message must include the words one hundred,
            for an input that is not a number; the error message must include the word non-number.
        
    """
    # Set try for input of the grade.
    #

    try:
        # Input to gather the floating point value of the grade.

        grade_1 = input(f"\nEnter a numeric grade value for the student in question: ")
        grade = float(grade_1)
    except ValueError:
        print(f"The grade entered, {grade_1}, was a non-number and can be a floating point value.")
        continue

    # Test that the grade is between 0 and 100.
    try:
        if grade < 0:
            raise ValueError(f"Your entered grade, {grade:.2f}, is less than zero.")
        elif grade > 100:
            raise ValueError(f"Your entered grade, {grade:.2f}, in greater than one hundred.")
    except ValueError as error_feedback:
        print(error_feedback)
        continue


    # Determine the letter grade, with ternary based single in-line if statement.
    letter_grade = "A" if grade >= 90.0 else "B" if grade >= 80.0 else "C" if grade >= 70.0 else "D" \
        if grade >= 60.0 else "F"

    print(f"The students grade entered was {grade:.2f} and that equals a letter grade of {letter_grade}.")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are y, Y, n, or N.")

# End of program

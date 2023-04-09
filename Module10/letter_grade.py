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
    Within a try-except structure, raise two different exceptions. Note that there are three listed
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

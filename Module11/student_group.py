#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 11, Assignment Part A
# Program name: student_group.py

"""
Part A

Create a program called student_group.py that uses a function from the random module to create a list of
    random students to work together on a group project, as follows:

    Create a list of at least 10 student names.
    Display the student list.
    Prompt the user to input how many students should be in the group.
    Generate a random number appropriate to the number of names in the list.
    Use the random number to retrieve and print the corresponding name from the list.
    Repeat until you have output the correct number of students, as input by the user.

Note: Depending on your solution, the same student could be chosen multiple times.
    Although you can solve this issue if you want, you are not required to address it for the assignment.
    What's important is that the proper number of students are chosen.

Hint: You may find the w3schools Links to an external site.or Python Links to an external site.random module
    references helpful.

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

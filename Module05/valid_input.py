#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 5, Assignment Part B
# Program name: valid_input.py

"""
----------
Part B

Create a program called  valid_input.py. In a loop, prompt the user to input their age in years;
 keep prompting until the user inputs a number greater than zero and less than 123
 (the oldest person on record lived to 122 years, 164 days). Once the user has input a valid number, output "Thank You"

Examples (note that your program does not need to look, or behave, like exactly like these examples -
  they're here to show that all error conditions are caught and that, when there is no error condition,
  the result is outputted):
"""

# Variable List
#
# Integer Variable
#
# age_input     - Entered value for the user's age.

# Beginning of code

# Establish sentinel variable and preset its value

sentinel = 'y'

"""
In a loop, prompt the user to input their age in years;
 keep prompting until the user inputs a number greater than zero and less than 123
"""

while sentinel != 'q':
    age_input = int(input("Enter your age in years, must greater than 0 and less than 123: "))
    if age_input <= 0 or age_input >= 123:
        print(f"\nYour entry, {age_input}, is either not greater than 0 or not less than 123, please try again.")
    else:
        print(f"\nThank You, your age is {age_input}.")
        sentinel = 'q'



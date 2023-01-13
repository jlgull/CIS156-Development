#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 7, Assignment Part A
# Program name: letter_count.py

"""
----------
Part A

Create a program in a file named letter_count.py that:
    Includes adequate instructions to the user about how to use the program.
    Inputs #1 through 4: Prompt the user to enter four different words or phrases, one at a time;
      storing each response in a separate variable.
    Input #5: Next, prompt the user a letter they wish to count.
    Determine how many times the letter occurs in each of the four words/phrases,
      regardless of case (uppercase or lowercase).
    Determine the total number of times the letter occurs in all words/phrases,
      regardless of case (uppercase or lowercase).
    Output is a formatted table displaying:
        the four words,
        the number of times the letter appears in each word/phrase,
        the total number of times the letter appears.
    Output a formatted table displaying the results.

Example (note that your program does not need to look, or behave, like exactly like this example -
  it is here to show you one way it might look when the program runs properly):


"""

# Variable List
#
# Integer Variables
#
# input_1       - The first number entered, must be greater than 1.
# input_2       - The second number entered, must be greater than 1.
# total_product - This is the total product of all numbers from 1st to the 2nd number.

# Preset all required Variables.

total_product = 1
input_1 = input_2 = 0

# Beginning of code

# Uses a loop  to:
#         Input #1: Prompts the user for a starting number (integer)  greater than 1.
#         Input #2: Prompts the user for an ending number (integer)  greater than 1.
#         If either of the first two numbers is less than 2,
#            display a message that includes the word ERROR and that they need to enter numbers greater than 1 and
#            continues to prompt the user for two numbers greater than 1 if either number is less than 1.

while input_1 < 2:
    input_1 = int(input("\nEnter the starting number (integer), greater than 1: "))
    if input_1 < 2:
        print("\nERROR, starting number must be greater than 1.")

while (input_2 < 2) or (input_2 == input_1):
    input_2 = int(input("\nEnter the ending number (integer), greater than 1: "))
    if (input_2 < 2) or (input_2 == input_1):
        print("\nERROR, ending number must be greater than 1 and not equal to the starting number.")

for number in range(input_1, input_2+1):
    total_product *= number

print(f"\nThe product of all the numbers between {input_1} and {input_2} is {total_product}.")


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

#
# Import all required options
#
# Import system and name from the os module.
from os import system, name

""" name    - The name of the operating system dependent module imported. 
                The following names have currently been registered: 'posix', 'nt', 'java'.

    system  - Execute the command (a string) in a subshell. 
                This is implemented by calling the Standard C function system(), and has the same 
                limitations. Changes to sys.stdin, etc. are not reflected in the environment of the
                executed command. If command generates any output, it will be sent to the interpreter
                standard output stream. The C standard does not specify the meaning of the return value 
                of the C function, so the return value of the Python function is system-dependent.            

"""

#
# Define the clear function definition for use in this program
#

def clear():
    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Variable List
#
# Integer Variables
#
# total_letters     - Total occurrences of the unique_letter.
#

# String Variables
#
# entered_words     - Words or phrases entered, to be searched for a unique letter.
# unique_letter     - Unique letter to be sought in the words or phrases.
# letter_counter    _ Count of unique_letters in each word or phrase.
#
#

# Floating Variables
#
#
#

# Preset all required Variables.
#
# Preset an empty list to gather the four different words or phrases.

entered_words = []

# Preset an empty list for the count of unique_letter
letter_counter = []

# Reset the total_letters for each run.

total_letters = 0

# Define all local functions
#
# None required

# Beginning of code

# Clear screen and gather the input information.

clear()

# General information about the program.
# Includes adequate instructions to the user about how to use the program.
#     Inputs #1 through 4: Prompt the user to enter four different words or phrases, one at a time;
#       storing each response in a separate variable.

print(f"\nThis program asks for four different words or phrases, one at a time."
      f"\n\tThen you will be asked for a letter to be counted in the entered words or phrases.\n")

# Gather the four different words or phrases.

for counter in range(4):
    entered_words.append(input(f"Enter word or phrase #{counter + 1}: "))

# Input #5: Next, prompt the user a letter they wish to count.

unique_letter = input(f"Enter the unique letter sought in the words or phrases: ")

#  Determine how many times the letter occurs in each of the four words/phrases,
#       regardless of case (uppercase or lowercase).

for counter in range(len(entered_words)):
    letter_counter.append(entered_words[counter].upper().count(unique_letter.upper()))

# Determine the total number of times the letter occurs in all words/phrases,
#       regardless of case (uppercase or lowercase).

for counter in range(len(entered_words)):
    total_letters = total_letters + letter_counter[counter]

print(entered_words, unique_letter, letter_counter, total_letters)

# Zazzle Zoo\nzebra\nGoat\nZzZzZzZ\nz\n


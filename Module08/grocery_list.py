#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 8, Assignment Part A
# Program name: grocery_list.py

"""
----------
Part A

Create a program called grocery_list.py that:

    Input #1: Asks the user to input how many items they will be purchasing at the grocery store.
    Input #2 through x (where x is the number the user entered): Uses a loop to prompt the user to
        input each of the items they are buying, storing each input into a list.
    When finished entering items, print the full list.

Example (note that your program does not need to look, or behave, like exactly like this example -
  it is here to show you one way it might look when the program runs properly):

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
# item_count        - Number of items to be purchased.
# i                 - Loop counter used to collect enter items.
#
# Floating Variables
#
# String Variables
#
# List Variables
#
# item_list         - List of items being purchased today.
#

#
# Preset an variables that need to be created prior to first use.
#

item_list = []


# Clear screen and start main program.

clear()

# Input #1: Asks the user to input how many items they will be purchasing at the grocery store.
#

item_count = int(input('\n\nEnter the number of items you will be purchasing today: '))

# Input #2 through x (where x is the number the user entered): Uses a loop to prompt the user to
#         input each of the items they are buying, storing each input into a list.
#

for i in range(item_count):
    item_list.append(input(f'Enter item number {i + 1}: '))


# When finished entering items, print the full list.
#

print(item_list)

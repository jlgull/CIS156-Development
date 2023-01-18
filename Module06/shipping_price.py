#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 6, Assignment Part B
# Program name: shipping_price.py

"""
----------
Part B

Create a program called shipping_pricea.py that calculates the shipping price for a purchase.

    Input #1: Prompt the user for the total number of items being shipped.
    Input #2: Prompt the user for the total weight of all items.
    Using a function that you create that accepts the information collected from the user,
      calculates the shipping cost and returns (not print) the total amount.
      Use the following parameters to determine shipping costs.
        Less than 3 items and less than two pounds: $5.50 shipping charge.
        Less than 3 items and two pounds or over: $7.00 shipping charge.
        3 to 5 items and less than three pounds: $8.50 shipping charge.
        Anything else: $11.00 shipping charge.
    Display the shipping cost to the user.
      (Note: the dollar amount does not need to be formatted to two decimal places.)

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
# item_count    - The number if items to be shipped.
#

# Floating Variables
#
# total_weight  - The total weight of items being shipped.
# shipping_cost - The total cost of shipping all the items.
#

# Preset all required Variables.
# None required for this program.

# Define all local functions
#
# Using a function that you create that accepts the information collected from the user,
#       calculates the shipping cost and returns (not print) the total amount.
#       Use the following parameters to determine shipping costs.
#         Less than 3 items and less than two pounds: $5.50 shipping charge.
#         Less than 3 items and two pounds or over: $7.00 shipping charge.
#         3 to 5 items and less than three pounds: $8.50 shipping charge.
#         Anything else: $11.00 shipping charge.

def ship_cost(item_count, total_weight):
    if item_count < 3:
        if total_weight < 2:
            shipping_cost = 5.5  # shipping cost is $5.50
        else:
            shipping_cost = 7.0  # shipping cost is $7.00
    elif item_count <= 5 and total_weight < 3:
        shipping_cost = 8.5  # shipping cost is $8.50
    else:
        shipping_cost = 11.0  # shipping cost is $11.00
    return shipping_cost


# Beginning of code

#     Input #1: Prompt the user for the total number of items being shipped.
#     Input #2: Prompt the user for the total weight of all items.

# Clear screen and gather the input information.

clear()

# General information about the program.

print(f"\nThis program asks for the number (an integer) of items to be shipped and"
      f"\n\ttotal weight (can be a value with a decimal point).")

# Gather the data needed.

item_count = int(input(f"\nEnter the number (integer) of items to be shipped: "))
total_weight = float(input(f"Enter the total weight of items to be shipped: "))

# Calculate shipping cost

shipping_cost = ship_cost(item_count, total_weight)


# Display the shipping cost to the user.
#       (Note: the dollar amount does not need to be formatted to two decimal places.)

print(f"\nTo ship your {item_count} items, with a total weight of {total_weight} lbs. is ${shipping_cost:0.2f}.")
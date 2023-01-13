#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 6, Assignment Part B
# Program name: shipping_pricea.py

"""
----------
Part B

Create a program called shipping_price.py that calculates the shipping price for a purchase.

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


# Beginning of code

#     Input #1: Prompt the user for the total number of items being shipped.
#     Input #2: Prompt the user for the total weight of all items.

# General information about the program.

print(f"\nThis program asks for the number (an integer) of items to be shipped and"
      f"\n\ttotal weight (can be a value with a decimal point).")

# Gather the data needed.

item_count = int(input(f"\nEnter the number (integer) of items to be shipped: "))
total_weight = float(input(f"Enter the total weight of items to be shipped: "))

# Calculate shipping cost

if item_count < 3:
    if total_weight < 2:
        shipping_cost = 5.5 # shipping cost is $5.50
    else:
        shipping_cost = 7.0  # shipping cost is $7.00
elif item_count <= 5 and total_weight < 3:
    shipping_cost = 8.5  # shipping cost is $8.50
else:
    shipping_cost = 11.0 # shipping cost is $11.00

# Display the shipping cost to the user.
#       (Note: the dollar amount does not need to be formatted to two decimal places.)

print(f"\nTo ship your {item_count} items, with a total weight of {total_weight} lbs. is ${shipping_cost:0.2f}.")
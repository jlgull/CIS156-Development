#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 9, Assignment
# Program name: shopping_cart.py

"""
----------
Create a program called shopping_cart.py that uses a class and objects to track a couple of items for
purchase from an online store. There are three steps/sections to this program:

1. Create the ItemToPurchase class with the following specifications:

    Attributes (variable names) and their default type.
        item_name (string)
        item_price (float)
        item_quantity (int)
    Default constructor
        Initializes item_name = "none", item_price = 0, item_quantity = 0
    Method (a function in a class) name:
        print_item_cost()

2. In the main section of your code (not in the class definition):

    Instantiate the ItemToPurchase class.
    Prompt the user for two items, creating two objects of the ItemToPurchase class. The order for each is:
        Input #1: item name
        Input #2: item price
        Input #3: item quantity

3.  Finally:

    Calculate the subtotal for the two items.
    Output the two subtotals (see example).
    Calculate the total cost.
    Output the total cost.

Note that the dollar values must display two decimal places (refer to zyBooks, chapter 7.2, on floating-point precision).

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
# item_quantity -   Number of item or items to buy.
#
# Floating Variables
#
# item_price    -   Unit price of each item.
# total_cost    -   Total for the 2 items entered.
#
# String Variables
#
# item_name     -   Descriptive name for item.
#
# List Variables
#
# shopping_cart -   Holds the items entered.

#
# Preset any variables that need to be created prior to first use.
#

shopping_cart = []

total_cost = 0


# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"
while do_again != "N":
    # Clear screen and start main program.
    #
    clear()

    """
    1. Create the ItemToPurchase class with the following specifications:

    Attributes (variable names) and their default type.
        item_name (string)
        item_price (float)
        item_quantity (int)
    Default constructor
        Initializes item_name = "none", item_price = 0, item_quantity = 0
    Method (a function in a class) name:
        print_item_cost()
    """

    class ItemToPurchase:

        # Initialize the variables.
        def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0 ):
            self.item_name = item_name
            self.item_price = item_price
            self.item_quantity = item_quantity

        def print_item_cost(self):
           return (f"You requested {self.item_quantity} {self.item_name} @ ${self.item_price:.2f} = "
                  f"${self.item_price * self.item_quantity:.2f}")

    # Created a test for the class instantiate.
    """
    object1 = ItemToPurchase("apple", 1.75, 2)
    print(object1.print_item_cost())
    object21 = ItemToPurchase("Yogurt", 2, 1)
    print(object21.print_item_cost())
    """

    """
    2. In the main section of your code (not in the class definition):

    Instantiate the ItemToPurchase class.
    Prompt the user for two items, creating two objects of the ItemToPurchase class. The order for each is:
        Input #1: item name
        Input #2: item price
        Input #3: item quantity
    """
    print(f"\nThis program will ask you to enter information about 2 items and "
          "\n\tthen print out the items and the total cost.\n")

    for item_counter in range(2):

        # Get user input for 2 items.
        entered_item = input(f"Enter the name of item {item_counter + 1}: ")
        entered_price = float(input(f"Enter the {entered_item} price, for example 1.25 for $1.25: "))
        entered_quantity = int(input(f"Enter the {entered_item} quantity: "))
        shopping_cart.append(ItemToPurchase(entered_item, entered_price, entered_quantity))
        # Print used to space out the entry process.
        print()

    """
    3.  Finally:

    Calculate the subtotal for the two items.
    Output the two subtotals (see example).
    Calculate the total cost.
    Output the total cost.

    Note that the dollar values must display two decimal places 
    (refer to zyBooks, chapter 7.2, on floating-point precision).

    """

    # Printing the 2 items and calculate the total cost.

    for item_counter in range(2):
        print(shopping_cart[item_counter].print_item_cost())
        total_cost += shopping_cart[item_counter].item_price * shopping_cart[item_counter].item_quantity

    # Printing the total Cost

    print(f"Total Cost = ${total_cost:.2f}")

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or a N.")

# End of program

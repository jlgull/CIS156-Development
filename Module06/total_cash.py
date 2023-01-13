#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 6, Assignment Part A
# Program name: total_cash.py

"""
----------
Part A

Create a program called total_cash.py that determines the total value of a wallet full of cash.

    Inputs #1 through 7: It prompts the user to input the quantity of each denomination of bills,
      in the following order: 1s, 2s, 5s, 10s, 20s, 50s, and 100s (this is seven prompts).
    Using a function that you create that accepts the information collected from the user,
      calculates the total value of all of the bills, and returns (not print) the total amount.
    Output the total amount of cash.

For example, if a user has 3 ones, 3 tens, and 1 fifty, their total is $83 in cash.
"""

# Variable List
#
# List based Variables
#
# bills         - The list of bills in any possible wallet.
# bill_count    - The count of each bill value in the wallet.

# Floating Point Variables
#
# cash_sum      - The sum of the bills in the wallet

# Define all functions
#
# Using a function that you create that accepts the information collected from the user,
#       calculates the total value of all of the bills, and returns (not print) the total amount.

def sum_wallet():
    sum = 0
    for index in range(7):
        sum = sum + (bills[index] * bill_count[index])
    return sum


# Preset the bills Variables.

bills = [1, 2, 5, 10, 20, 50, 100]
bill_count = []


# Beginning of code

# Inputs #1 through 7: It prompts the user to input the quantity of each denomination of bills,
#       in the following order: 1s, 2s, 5s, 10s, 20s, 50s, and 100s (this is seven prompts).

print(f"\nThis program will ask you to look in your wallet and then respond with numbers to 7 requests.")
print(f"\tIf there an none of the bills in question, respond with a 0 (zero).\n")

for index in range(7):
    number = int(input(f"Enter the number ${bills[index]}'s in your wallet: "))
    bill_count.append(number)
print(f"\n{bill_count}")

# Call the function sum_wallet()

sum = sum_wallet()

#  Output the total amount of cash.

print(f"\nSum of the cash in the wallet is ${sum}.")

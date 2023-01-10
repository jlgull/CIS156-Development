#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 3, Assignment Part A
# Program name: name.py

"""
This is the first programming assignment.
Be aware that instructions are requirements, not suggestions.
Most assignments will have two parts.
----------
Part A

Create a program named name.py that:

    Input #1 prompts the user to input their first name and stores it in a variable
    Input #2 prompts the user for their last name, and store that in a second variable
    creates a third variable with their full name (first and last, including a space between)
    print the full name
    output the length of the full name
    output the user's initials with periods after each letter and a space between them
    output the second-to-last letter in the first name
    output the second letter in the last name

Example (note that your program does not need to look, or behave, like exactly like this example -
    it is here to show you one way it might look when the program runs properly):

"""

# Variable List
#
# String Variables
#
# first_name
# last_name
# full_name

# Beginning of code

# Input #1 prompts the user to input their first name and stores it in a variable

first_name = input("\nEnter the user's First name: ")

# Input #2 prompts the user for their last name, and store that in a second variable

last_name = input("\nEnter the user's Last name: ")

# Creates a third variable with their full name (first and last, including a space between)

full_name = first_name + ' ' + last_name

# print the full name

print(f"\nThe user's Full name is: {full_name}")

# Output the length of the full name

print(f"\nThe length of the user's Full name is {len(full_name)} characters.")

# Output the user's initials with periods after each letter and a space between them

print(f"\nThe user's initials are: {first_name[0]}. {last_name[0]}.")

# Output the second-to-last letter in the first name

print(f"\nThe second-to-last letter of the user's First name is: '{first_name[-2]}'")

# Output the second letter in the last name

print(f"\nThe second letter of the user's Last name is: '{last_name[1]}'")


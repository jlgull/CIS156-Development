#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 3, Assignment Part B
# Program name: family.py

"""
This is the first programming assignment.
Be aware that instructions are requirements, not suggestions.
Most assignments will have two parts.
----------
Part B

Create a program named family.py that:

    Creates a dictionary of names and ages for a family of at least four people;
       this may be your family or a fictional family (such as the Simpsons)
    Prints out the dictionary
    Prints the age of the third person in the dictionary
    Adds an entry (without changing or re-creating the existing dictionary data) for Tracy who is 60 years old
    Prints the dictionary again
    Prompts the user for a name to look up, and then outputs that person's age

Example (note that your program does not need to look, or behave,
   like exactly like this example - it is here to show you one way it might look when the program runs properly):

"""

# Variable List
#
# Dictionary Variables
#
# familyDic     - The dictionary to hold the basic family
# last_name
# full_name

# Beginning of code

# Creates a dictionary of names and ages for a family of at least four people;
#        this may be your family or a fictional family (such as the Simpsons)

familyDic = {"Michael":34, "Nicole":38, "Collin":14, "Lucas":12}

# Prints out the dictionary

print(f'\nThe base family is: {familyDic}, which has {len(familyDic)} names.')

#  Prints the age of the third person in the dictionary

print(f"\nThe third person's age is {familyDic['Collin']} years old.")

# Adds an entry (without changing or re-creating the existing dictionary data) for Tracy who is 60 years old

familyDic['Tracy'] = 60

# Prints the dictionary again

print(f'\nThe updated family is: {familyDic}, which has {len(familyDic)} names.')

# Prompts the user for a name to look up, and then outputs that person's age

name = input("\nEnter one of the names above to get that person's age: ").title()

print(f'\nYou selected {name} and that person is {familyDic[name]} years old.')
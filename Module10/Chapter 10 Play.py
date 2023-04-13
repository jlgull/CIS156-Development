#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 10, Play
# Program name: Chapter 10 Play.py

sentinel = ''

while sentinel != 'q':
    try:
        miles = float(input("Enter Miles driven: "))
        gallons = float(input("Enter gallons used: "))
        print(f'Your mpg is {miles / gallons:.2f}')
    except ValueError:
        print("Enter data must be number.")
        continue



    try:
        number = int(input('\nPlease enter a whole number from 1 to 100: '))
    except ValueError:
        print('ERROR: Please enter a whole number!')
    continue

    if number < 1 or number > 100:
        print('ERROR: Please enter a whole number greater than 0 and less than101!')
    continue

else:
        print(f'\nYAY! You followed instructions and entered {number}!')

sentinel = input("Enter 'q' to quit, any other key to continue...")


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
    except:
        print("Enter data must be number.")

sentinel = input("Enter 'q' to quit, any other key to continue...")
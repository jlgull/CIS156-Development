#!/bin/python3
#
# Author: Jonathan Heard

"""
Create a Python file, named airfare_cost.py, that calculates the total cost of an airline ticket,
   based on the following requirements:
User input 1: One of these three letter airport codes, which will be presented to the user:

    LAX for Los Angeles
    LGA for New York (LaGuardia)
    LHR for London (Heathrow)

User input 2: One of these numerical day codes, which will be presented to the user:

    1 for Monday
    2 for Tuesday
    3 for Wednesday
    4 for Thursday
    5 for Friday
    6 for Saturday
    7 for Sunday

User input 3:

    Do they have checked baggage? The accepted inputs are Y for yes or N for no.

Costs, based on destination airport and day of week and whether or not baggage is checked:

    LAX: $100  Mon (1) through Friday (5), $150 Sat (6), $125 Sun (7)
    LGA: $175  Mon (1) through Friday (5), $275 Sat (6), $250 Sun (7)
    LHR: $1,000 Mon (1) and Fri (5), $800 Tue (2) through Thu (4), $1200 Sat (6), $1100 Sun (7)
    Checked baggage cost +$50 for US destinations (LAX and LGA), +$100 for London (LHR).

Refer to the table, below.

Output is the total cost of the ticket.

Additional note: Error checking is not required"""

# Beginning of the code body.

# Print out airport list.
'''
The user will input one of these three letter airport codes:
LAX (Los Angeles)
LGA (New York - LaGuardia)
LHR (London - Heathrow)
'''

print('\nHere is a list of available airports.\n')
print('LAX for Los Angeles')
print('LGA for New York - LaGuardia')
print('LHR for London - Heathrow')

airport = input('\nPlease enter the 3 letter identifier for the airport Destination: ').upper()

# included only for testing
# print('\n', airport)

# Print out the day selection list.

'''
The user will input one of these numerical day codes:
1 for Monday
2 for Tuesday
3 for Wednesday
4 for Thursday
5 for Friday
6 for Saturday
7 for Sunday
'''

print('\nHere is a list of travel days.\n')
print('1 for Monday')
print('2 for Tuesday')
print('3 for Wednesday')
print('4 for Thursday')
print('5 for Friday')
print('6 for Saturday')
print('7 for Sunday')

travelDay = int(input('\nPlease enter the number of the day you wish to fly: '))

# included only for testing
# print('\n', travelDay)

# User is prompted whether or not they have checked baggage, at an extra cost:

luggage = input('\nEnter Y if you will be checking luggage, or N if no checked luggage. ').upper()

# included only for testing
# print('\n', luggage)

# Pricing information.

"""
Costs, based on airport and day of week:
LAX: $100  Mon (1) through Friday (5), $150 Sat (6), $125 Sun (7)
LAX: $175  Mon (1) through Friday (5), $275 Sat (6), $250 Sun (7)
LHR: $1,000 Mon (1) and Fri (5), $800 Tue (2) through Thu (4), $1200 Sat (6), $1100 Sun (7)

Checked baggage cost +$50 to US destinations (LAX and LGA), +$100 to London (LHR)
"""

# Calculate the total cost of the ticket.

"""
Output is the total cost of the ticket.
"""

travelCost = 0

if airport == 'LAX':
    if travelDay <= 5:
        travelCost = 100
    elif travelDay == 6:
        travelCost = 150
    else:
        travelCost = 125

if airport == 'LGA':
    if travelDay <= 5:
        travelCost = 175
    elif travelDay == 6:
        travelCost = 275
    else:
        travelCost = 250

if airport == 'LHR':
    if travelDay == 1 or travelDay == 5:
        travelCost = 1000
    elif travelDay == 6:
        travelCost = 1200
    elif travelDay == 7:
        travelCost = 1100
    else:
        travelCost = 800

if luggage == "Y":
    travelCost += 50 if (airport == 'LAX' or airport == 'LGA') else 100

print(travelCost)

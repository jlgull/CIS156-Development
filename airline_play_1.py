#!/bin/python3
#
# Author: Jonathan Heard

"""
This is an airline cost assignment. Write a program to calculate the total
cost of an airline ticket, based on the following requirements.

The user will input one of these three letter airport codes:
LAX (Los Angeles)
LGA (New York - LaGuardia)
LHR (London - Heathrow)

The user will input one of these numerical day codes:
1 for Monday
2 for Tuesday
3 for Wednesday
4 for Thursday
5 for Friday
6 for Saturday
7 for Sunday

Costs, based on airport and day of week:
LAX: $100  Mon (1) through Friday (5), $150 Sat (6), $125 Sun (7)
LAX: $175  Mon (1) through Friday (5), $275 Sat (6), $250 Sun (7)
LHR: $1,000 Mon (1) and Fri (5), $800 Tue (2) through Thu (4), $1200 Sat (6), $1100 Sun (7)

User is prompted whether or not they have checked baggage, at an extra cost:
Checked baggage cost +$50 to US destinations (LAX and LGA), +$100 to London (LHR)

Output is the total cost of the ticket.
"""

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

luggage = int(input('\nEnter 1 if you will be checking luggage, or 0 if no checked luggage. '))

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

if luggage == 1:
    travelCost += 50 if (airport == 'LAX' or airport == 'LGA') else 100

print(travelCost)

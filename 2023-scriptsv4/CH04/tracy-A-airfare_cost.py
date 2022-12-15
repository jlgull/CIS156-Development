"""
Create a Python file, named airline_cost.py, that calculates the total cost of an airline
ticket, based on the following requirements:

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

User input 3: Do they have checked baggage? The accepted inputs are Y for yes or N for no.

Costs, based on destination airport and day of week:
 LAX: $100  Mon (1) through Friday (5), $150 Sat (6), $125 Sun (7)
 LGA: $175   Mon (1) through Friday (5), $275 Sat (6), $250 Sun (7)
 LHR: $1,000 Mon (1) and Fri (5), $800 Tue (2) through Thu (4), $1200 Sat (6), $1100 Sun (7)

Checked baggage cost +$50 for US destinations (LAX and LGA), +$100 for London (LHR).

Refer to the table.

Output is the total cost of the ticket.

Additional note:
Error checking is not required.
"""

airport_dict = {'LAX': 'Los Angeles', 'LGA': 'New York (LaGuardia)', 'LHR': 'London (Heathrow)'}
weekday_dict = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

print('\n\nPlease enter the three letter airport code for your destination.')
print(f"\n LAX - {airport_dict['LAX']}")
print(f" LGA - {airport_dict['LGA']}")
print(f" LHR - {airport_dict['LHR']}")
airport_code=input('\nEnter airport code (LAX, LGA, or LHR): ').upper()

print(f'\nPlease enter the numerical day code for the day you want to fly to {airport_dict[airport_code]}.\n')
for k,v in weekday_dict.items():
    print(f' {k} - {v}')
day_code=int(input('\nEnter day code (1 - 7): '))

if airport_code == 'LAX':
    if day_code <= 5:
        cost = 100
    elif day_code == 6:
        cost = 150
    else:
        cost = 125

if airport_code == 'LGA':
    if day_code <= 5:
        cost = 175
    elif day_code == 6:
        cost = 275
    else:
        cost = 250

if airport_code == 'LHR':
    if day_code == 1 or day_code == 5:
        cost = 1000
    elif day_code >= 2 and day_code <= 4:
        cost = 800
    elif day_code == 6:
        cost = 1200
    else:
        cost = 1100

if airport_code == 'LHR':
    baggage_charge = 100
else:
    baggage_charge = 50

check_baggage = input(f'\n\n(Subtotal: ${cost}) Are you checking baggage to {airport_dict[airport_code]} at an extra charge (${baggage_charge})? [Y/N]: ').upper()

if check_baggage == 'Y':
    cost = cost + baggage_charge

print(f'\nYour grand total to {airport_dict[airport_code]} on {weekday_dict[day_code]} is: ${cost}')

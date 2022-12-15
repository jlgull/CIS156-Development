"""
Tracy Baker
Mod 3
Part A
Create a program named name.py that:

prompts the user to input their first name and stores it in a variable
prompts the user for their last name, and store that in a second variable
creates a third variable with their full name (first and last, including a space between)
print the full name
output the length of the full name
output the user's initials with periods after each letter and a space between them
output the second-to-last letter in the first name
output the second letter in the last name
"""

first_name = input('\nPlease enter your first name: ')
last_name = input(f'\nThanks, {first_name}. Now enter your last name: ')
full_name = first_name + ' ' + last_name

print(f'\nYour full name is                               : {full_name}')
print(f'Your initials are                               : {first_name[0]}. {last_name[0]}.')
print(f'The second-to-last letter of your first name is : {first_name[-2]}')
print(f'The second letter of your last name is          : {last_name[1]}')

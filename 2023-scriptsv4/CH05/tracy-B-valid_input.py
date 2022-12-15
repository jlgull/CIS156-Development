"""
Create a program called valid_input.py.
In a loop, prompt the user to input their age in years;
keep prompting until the user inputs a number greater than zero and less than 123
(the oldest person on record lived to 122 years, 164 days).
Once the user has input a valid number, output "Thank you"
"""

user_age = 0

while user_age < 1 or user_age > 122:

    user_age = int(input('\nPlease enter your age as a whole number: '))

    if user_age >= 1 and user_age <= 122:
        break

    elif user_age > 122:
        print('\nYou cannot be that old, please enter an age less than 123.')

    else:
        print('\nYou cannot be that young, please enter an age greater than 0.')

print('\nThank You')

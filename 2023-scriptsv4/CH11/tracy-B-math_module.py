
from math import sqrt, fabs

print('\n\nPlease enter a number and I will find its square root and absolute value.')
print('If a negative number is entered, its absoulte value will be used. ')
number = int(input('\nInput number: '))

number2 = fabs(number)

print(f'\nThe square root of {number2} is {sqrt(number2)}')

print(f'\nThe absolute value of {number} is {number2}')

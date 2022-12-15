"""
Create a program called product_loop.py that:

Prompts the user for a starting number (integer) greater than 1.

Prompts the user for an ending number (integer) greater than 1.

If either of the first two numbers is less than 2:
    display a message, that includes the word ERROR, to enter numbers greater than 1 and
    use a loop to continue to prompt the user for two numbers greater than 1.

Using a loop, calculate the product (the result of multiplication) of every number from the first to the second.

The output will be the product of all numbers.
"""

num_start = 0
num_end = 0

while num_start < 2 or num_end < 2:
    num_start = int(input('\n\nPlease enter a starting number greater than 1 : '))
    num_end = int(input('Please enter an ending number greater than 1  : '))

    if num_start < 2 or num_end < 2:
        print('\nERROR! Both numbers must be greater than 1. Try again!')

# initialize variables; assign num_start to i to retain the
# contents of num_start for later use
i = num_start
result = 1

# loop from i (num_start) to num_end, multiplying each successive
# number to the one that came before it, storing it in result
while i <= num_end:
    result = result * i
    i += 1

print(f'\n\nThe product of all numbers from {num_start} and {num_end} is: {result}\n\n')

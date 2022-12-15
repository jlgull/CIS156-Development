def calculate_total(ones=0, twos=0, fives=0, tens=0, twenties=0, fifties=0, hundreds=0):
    return (1 * ones) + (2 * twos) + (5 * fives) + (10 * tens) + (20 * twenties) + (50 * fifties) + (100 * hundreds)

print('\nThis program will calculate the amount of cash found in a wallet.')
print('Please only enter whole numbers. If a denomination does not exist, enter 0.\n')

denominations = ['$1', '$2', '$5', '$10', '$20', '$50', '$100']
bills = []

for i in range(len(denominations)):
    bills.append(int(input(f'How many {denominations[i]} bill(s) are there? ')))

print(f'\nThe total is: ${calculate_total(bills[0], bills[1], bills[2], bills[3], bills[4], bills[5], bills[6])}')

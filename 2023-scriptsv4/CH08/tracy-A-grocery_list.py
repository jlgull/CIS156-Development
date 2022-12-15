grocery_list=[]

num_items = int(input('\nHow many items will you be buying at the grocery store today? '))
print()

for i in range(num_items):
    grocery_list.append(input(f'Please input item #{i+1}: '))

print(f'\nHere is your grocery list: {grocery_list}')

def calculate_shipping(item_num=0, item_weight=0):
    if item_num < 3:
        if item_weight < 2:
            return 5.50
        else:
            return 7.00
    elif item_num <= 5 and item_weight < 3:
        return 8.50
    else:
        return 11.00


print('\nThis program will calculate a shipping cost.')

num_item = int(input('\nHow many items are you shipping? '))
weight = int(input('How much do the items weight?    '))

print(f'\nYour shipping cost is: ${calculate_shipping(num_item, weight):.2f}')

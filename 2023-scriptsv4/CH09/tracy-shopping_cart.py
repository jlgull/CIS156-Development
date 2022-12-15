class ItemToPurchase:
    
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.total = (self.item_price * self.item_quantity)

    def print_item_cost(self):
        print(f'{self.item_name}: {self.item_quantity} at ${self.item_price:.2f} = ${self.total:.2f}')

# start main
print('\n\nThis program will ask for a list of grocery items - their')
print('name, cost, and quantity. It will then print out list with')
print('the totals.')

# Get first item's information then call the ItemToPurchase class
# (create an instance of the class) using the gathered data
i_name = input('\nEnter the name of the item: ')
i_price = float(input(f'({i_name}) Price?:    $' ))
i_quantity = int(input(f'({i_name}) Quantity?:  '))
item1 = ItemToPurchase(i_name, i_price, i_quantity)

# Get second item's information then call the ItemToPurchase class
# (create another instance of the class) using the gathered data
i_name = input('\nEnter the name of the item: ')
i_price = float(input(f'({i_name}) Price?:    $' ))
i_quantity = int(input(f'({i_name}) Quantity?:  '))
item2 = ItemToPurchase(i_name, i_price, i_quantity)

# Use the instance method print_item_cost to print the subtotal
# per instance
print('\nSubtotals:')
item1.print_item_cost()
item2.print_item_cost()

# Get the grand total, referencing a attribute reference operator
print(f'\nTOTAL COST: ${item1.total + item2.total:.2f}')

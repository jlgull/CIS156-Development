class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.00, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        max_length = len(self.item_name) if len(self.item_name) > len(str(self.item_price)) else len(str(self.item_price))
        spacer = 1 if len(self.item_name) > len(str(self.item_price)) else 2
        # length = 4 if len(str(self.item_price)) == 3 else len(str(self.item_price))
        length = len(str(self.item_price))
        print(f'Max Length = {max_length}; Spacer = {spacer}; Length = {length}')
        print(f'\n     Item name    : {self.item_name:>{max_length + spacer}}')
        print(f'     Item price   : {" $":>{max_length - length}}{self.item_price:>{length}.2f}')
        # print(f'     Item price   : {" $":>{max_length - length}}{self.item_price:.2f}')
        print(f'     Item quantity: {self.item_quantity:>{max_length + spacer}}')

    def subtotal(self):
        return self.item_price * self.item_quantity

total = 0

for i in range(2):

    item = ItemToPurchase(input('Please enter the name of your item              :  '),
                    float(input('Please enter the price of your item             : $')),
                    int(input('Please enter how many you would like to purchase:  ')))

    item.print_item_cost()

    print(f'\n   Item {i + 1} subtotal: ${item.subtotal():.2f}\n')

    total += item.subtotal()

print(f'The grand total is: ${total:.2f}')

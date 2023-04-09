# Tracy Baker
# programming assignment 9

### CLASS DEFINITION ###

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

        # self.field_width is used in this method and in the main body of the program
        # 5 is the minimum field length because of the price attribute,
        # if .1 is entered, it'll be $0.10 and 1 will be $1.00
        self.field_width = 5

    def print_item_cost(self):

        # The item_list, print_list objects (lists) are available only within this method
        # item_list holds the string (and formatted) versions of name, price and quantity attributes
        # print_list holds text to be printed (allowing the use of a loop and a single print statement)
        item_list = [self.item_name, '$' + '{:.2f}'.format(self.item_price), str(self.item_quantity)]
        print_list = ['name       : ', 'price      : ', 'quantity   : ']

        # figure out which attribute (self.item_name, self.item_price, self.item_quantity) is the 'longest' -
        # use that as self.field_width
        for i in item_list:
            if self.field_width < len(i):
                self.field_width = len(i)

        # print the three attributes, using self.field_width as an on-the-fly field width, right justified
        print()
        for i in range(3):
            print(f'Item {print_list[i]}{item_list[i]:>{self.field_width}}')

    def subtotal(self):
        return self.item_price * self.item_quantity


### FUNCTION DEFINITION ###

def dotted_line(char, length):
    print(char * (18 + length))


### MAIN ###

# this is used to keep a running total of all items' costs
total = 0

# Get the information for the two items. Each instantiated object will replace the prior one
print('\n')
for i in range(2):

    # instantiate the ItemToPurchase class as the item object and, at the same time, collect
    # the information from the user (name, price, quantity)
    item = ItemToPurchase(input('What are you buying?     :  '),
                          float(input('How much does it cost?   : $')),
                          int(input('How many are you buying? :  ')))

    # print the information for the current item
    item.print_item_cost()

    # determine which is longer, the existing field width value or the length of the item's subtotal
    # (including the $ and decimal). Use the longer of the two as item.field_width
    if item.field_width < len('$' + '{:.2f}'.format(item.subtotal())):
        item.field_width = len('$' + '{:.2f}'.format(item.subtotal()))

    # print a - line that will match the length of the subtotal
    dotted_line('-', item.field_width)
    print(f'item {i + 1} subtotal : ${item.subtotal():.2f}\n')

    total += item.subtotal()

# print a = line that will match the length of the grand total
dotted_line('=', len('$' + '{:.2f}'.format(total)))
print(f'The grand total : ${total:.2f}')

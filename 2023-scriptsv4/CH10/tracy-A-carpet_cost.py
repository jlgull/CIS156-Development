print("\n\nWelcome to Tracy's magical carpet cost figure-out-er program!")
print("We'll figure out the cost per square foot for carpeting that room!")

# set choice to '', the loop will exit of the user enteres Q or q
#choice = ''
#while choice != 'Q':
try:
    # collect data
    carpet_length = int(input("\nPlease enter the carpet's length, in feet:  "))
    carpet_width = int(input("Please enter the carpet's width, in feet :  "))
    paint_cost = float(input("How much money did you spend on the carpet? : $"))

    # calculate area and cost per square foot
    carpet_area = carpet_length * carpet_width
    carpet_cost = paint_cost / carpet_area
            
    # print results
    print(f'\nThe area of the carpet is {carpet_area} sqft.')
    print(f'The carpet cost ${carpet_cost:.2f} / sqft.')

# if any inputted value is NOT a number, print this error
except ValueError:
    print('>>> A non-number was entered. Please enter numbers for all values! <<<')
#    continue

# if carpet_length or carpet_width are 0, print this error because there
# is a divide by 0 issue. (BTW, black holes are created when God
# divides by zero! haha)
except ZeroDivisionError:
    print('>>> 0 was entered for height and/or width. Please enter numbers greater than zero! <<<')
#    continue

    # wanna do it again?
#    choice = input('\nEnter Q to quit, anything else to do it again: ').upper()


poem_file = open('tin_wedding_whistle.txt')
poem_lines = poem_file.readlines()
poem_file.close()

# preamble
print('\n\nThis file will display a sentence from an Ogden Nash poem.')
print(f'\nThere are {len(poem_lines)} lines.')

# loop through until the user no long wants to play
while True:

    line_num = input('\nWhat line would you like to see (enter exit to exit)? ')

    if line_num == 'exit':
        break
    else:
        print(f'\n{poem_lines[int(line_num) - 1]}')

print('\n\nThanks for using my program!')

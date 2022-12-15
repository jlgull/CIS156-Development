word_list = []
total_count = 0
word_count = 0
num_words=4

# Preamble
print(f'\n\nThis program will ask you to input {num_words} words.')
print('It will then ask for a letter. It will then')
print('count how many times the letter appears in')
print('each of the words you have supplied.')

print()

# Get words and letter - set them all to lowercase
for i in range(num_words):
    word_list.append(input(f'Please enter word #{i+1}: ').lower())
search_letter = input("\nNow please enter the letter that you'd like to find: ").lower()

# Print dashed line
print(f'\nThe incidence of {search_letter} in each word is:')
print('-' * 35)

# Get count of incidence of letter in each word. Get total for all.
for i in range(num_words):
    total_count = total_count + word_list[i].count(search_letter)
    print(f'{word_list[i]:<30}{word_list[i].count(search_letter):>5}')

# Print dashed line and total
print('-' * 35)
print(f'{"Total":<30}{total_count:>5}')

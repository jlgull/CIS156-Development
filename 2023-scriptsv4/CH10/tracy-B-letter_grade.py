print("\n\nWelcome to Tracy's letter grade conversion program!")
print("Give me your numerical grade, and I'll tell you your letter grade!")

# declare and set a dictionary to determine grade

from sys import exit

grade_dict = {'A': 89, 'B': 79, 'C': 69, 'D': 59, 'F': 0}

try:
	grade = input('\nPlease please enter your numerical grade: ')

	try:
		grade = float(grade)
	except:
		print('\n>>> Error: input is a non-number <<<')
		exit(1)

	if grade < 0:
		raise ValueError('number is less than zero!')
	
	if grade > 100:
		raise ValueError('number is greater than one hundred!')

	for key, value in grade_dict.items():
		if grade > value:
			print(f'You have earned a letter grade of: {key}')
			break

except ValueError as error_message:
	print(f'>>> Error: {error_message} <<<')

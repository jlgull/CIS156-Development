"""
Tracy Baker
Mod 3
Part B

Create a program named family.py that:

creates a dictionary of names and ages for a family of at least four people; this may be your family or a fictional family (such as the Simpsons)
prints out the dictionary
prints the age of the third person in the dictionary
adds an entry (without changing or re-creating the existing dictionary data) for Tracy who is 60 years old
prints the dictionary again
prompts the user for a name to look up, and then outputs that person's age
"""

winwood_family = {'Steve Winwood': 73, 'Robin Trower': 76, 'Elton John': 74, 'Dave Mason': 75}

print("\n\nSome of the Steve Winwood's 'family':")
print(winwood_family)

print('\nThe age of the third person in this dictionary is:', winwood_family['Elton John'])

winwood_family['Tracy'] = 60

print('\nOops, forgot a very important one! Congrats, you are now associated with Steve Winwood!')
print(winwood_family)

choice = input("\nEnter a name and I'll tell you their age (requires full name, proper capitalization, and the space): ")
print(f'{choice} is {winwood_family[choice]}')

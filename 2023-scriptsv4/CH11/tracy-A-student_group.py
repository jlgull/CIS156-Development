
#import random

from random import sample

student_list = ['Arya', 'Sansa', 'Rickon', 'Jon', 'Brandon', 'Robb', 'Tyrion', 'Jamie', 'Cersei', 'Daenerys', 'Viserys', 'Rhaegar']

print('\n\nHere is the list of students:')
print(student_list)

num_students = int(input('\nPlease enter how many should be randomly chosen to form a group: '))

student_group_list = sample(student_list, num_students)
print(f'\nThe {num_students} students in the group are:')
for i in student_group_list:
    print(i)

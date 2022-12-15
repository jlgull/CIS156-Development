# Micheal Cudd
# Module 13 Programming Assignment
# Part A
# Pets.

# Create a program called pets.py that that defines a pet class with at least three general attributes (fields)
# for all pets (for example, name, age, etc.) and at least two functions/behaviors for all pets
# (for example, eating). The functions can simply print something.
#
# Next, create two derived classes from the base class that represent specific types of pets. For example,
# one derived class might be a dog. Add at least one attribute/field and at least two functions/behaviors
# specific to that kind of pet.
#
# Finally, demonstrate that both derived classes work by creating at least one instance of
# each and showing off their fields and functions.
#
# Note: In preparation for the Final Project, this assignment leaves room for you to make more
# decisions about the code than previous assignments.
# Just be sure that your submission demonstrates the key concepts from the chapter, as indicated in these directions.

###############################

# parent class - Pets
class Pets:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def behavior_1(self):
        print('This pet has a license.')

    def behavior_2(self):
        print('This pet lives in the house.')

# Inherited class 1 - Dogs
class Dog(Pets):
    def __init__(self, name, age, breed):
        Pets.__init__(self, name, age, breed)
        self.trick = 'This dog knows how to fetch'

    def dog_behavior_1(self):
        print('this dog has been trained in protection.')

    def dog_behavior_2(self):
        print('this dog is great with kids and other pets')

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}, Breed: {self.breed}')
        print(f'{self.trick} ')

# Inherited class 2 - Cats
class Cat(Pets):
    def __init__(self, name, age, breed):
        Pets.__init__(self, name, age, breed)
        self.trick = 'This cat knows how to use a scratching post.'

    def cat_behavior_1(self):
        print('this cat has been trained to use a litter box.')

    def cat_behavior_2(self):
        print('this cat is great with females, but runs from males.')

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}, Breed: {self.breed}')
        print(f'{self.trick} ')


dog1 = Dog(name='Kane', age='12', breed='Rottweiler')
dog1.display()
dog1.behavior_1()
dog1.behavior_2()
dog1.dog_behavior_1()
dog1.dog_behavior_2()
print('\n')
cat1 = Cat(name='Oliver', age='1', breed='Black Cat')
cat1.display()
cat1.behavior_1()
cat1.behavior_2()
cat1.cat_behavior_1()
cat1.cat_behavior_2()

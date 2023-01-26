#!/usr/bin/python3
# Original Author: Tracy Baker
# Modified by: Jonathan Heard
# Sort a group of items; integers, floating point or string.
#   Using a new sort concept, by Jonathan.
# Program name: sort17j.py
#

# Import all required modules
# Import sample from the random module.

from random import sample, randint, uniform

"""  random.sample(population, k)
        Return a k length list of unique elements chosen from the population sequence or set. 
        Used for random sampling without replacement.
"""

# Import system and name from the os module.
from os import system, name

""" name    - The name of the operating system dependent module imported. 
                The following names have currently been registered: 'posix', 'nt', 'java'.

    system  - Execute the command (a string) in a subshell. 
                This is implemented by calling the Standard C function system(), and has the same 
                limitations. Changes to sys.stdin, etc. are not reflected in the environment of the
                executed command. If command generates any output, it will be sent to the interpreter
                standard output stream. The C standard does not specify the meaning of the return value 
                of the C function, so the return value of the Python function is system-dependent.            

"""

# Import the time library to allow for the timing of the sorting process

from time import thread_time_ns

#
# Define all functions used in this program
#

def clear():
    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Variable definition section
#
# start_time    - Start time, used to time the sort process
#

# List variables
#
# word_list     - collection of 3 letter groups
# selected_list - Randomly selected list of items to be sorted.
# temp_list     - Hold the selected_list prior to sorting, for comparison usage.

# Integer variables
#
# i, j, k       - Counters for the loop variables
# size_of_list  - Holds the number of random groups to select
# show_output   - Controls whether sorting is displayed as it happens or not
# pass_num      - Counter for the number of passes in the sort routine.
# swap_count    - Used to keep track of the number of swaps per pass. It is incremented
#                 for each NO SWAP. If swap_count >= iterations in a pass (num_entries), 
#                 then there is no need to continue; the list is fully sorted.

# Preset any required variables
show_output = ''
pass_num = 0
swap_count = 0
done = 0

# Preset required list variables
word_list = []
selected_list = []
temp_list = []

# Start of the Main program.

clear()

# Select data_type to be sorted and how many.

# Set the default data_type to "string".
data_type = 'string'

# usage statement and get input from user
print('\nThis program will sort random strings, integers (whole numbers), or floating point (decimal numbers).')
user_input = input('\nEnter a letter, whole number, or decimal number (as an example): ')

# detect if user_input is integer
try:
    user_input = int(user_input)
    data_type = 'integer'
except:
    pass

# if data_type is still "string" (meaning it wasn't converted to an integer),
# detect if it is a floating point number
if data_type == 'string':
    try:
        user_input = float(user_input)
        data_type = 'floating point'
    except:
        pass

# if data_type is integer or floating point, ask user if they really wanted a string - as
# entries such as 1 or 3.14 can also be strings
if data_type != 'string':
    if (input(f'\nThe data type entered was {data_type}. If it should be a string, enter y: ')) == 'y':
        data_type = 'string'

print(f'\nThe list will be made up of {data_type}s.')

while True:
    try:
        size_of_list = int(input(f"\nHow many {data_type} values do you want sorted? "))
        break
    except:
        print('Please enter an integer for the number of values you want.')
        continue
    
# Generate the type and number of items to be sorted.
if data_type != 'string':
    
    # since the list will be numbers (integers or floating points),
    # ask the user for minimum and maximum values
    print('\nEnter minimum and maximum values for the random number list.')
    while True:

        min = input('min: ')
        max = input('max: ')
        try:
            min = int(min)
            max = int(max)
        except:
            print('\nPlease enter a number for min and max!')
            continue

        if max < min:
            print('\nmin must be less than max!')
            continue
        else:
            break

    # Generate the type and number of items to be sorted.
    for i in range(size_of_list):
        if data_type == 'integer':
            selected_list.append(randint(min, max))
        else:
            selected_list.append(uniform(min, max))
else:
    
    # generate string list
    for i in range(75):
        for j in range(75):
            for k in range(75):
                word_list.append(chr(i + 48) + chr(j + 48) + chr(k + 48))
    # word_list, at this point has 421,875 elements. use the sample()
    # function to pick size_of_list elements and place the result into
    # selected_list
    selected_list = sample(word_list, size_of_list)

show_output = input('\nWatch the sorting as it takes place (slows processing)? (y = yes, anything else = no): ')

# Save the original list for later review.
temp_list = selected_list[:]

# Start the timer for the sort process
start_time = thread_time_ns()

# New Sort Routine, something different.
i = 0
while done == 0:
    # Test 2 items to determine if they need to be swapped.
    if selected_list[i] > selected_list[i + 1]:
        # Swap tested values if required.
        selected_list[i + 1], selected_list[i] = selected_list[i], selected_list[i + 1]
        swap_count += 1
        # Reset i and begin the testing / sorting loop again.

        i = -1
    i += 1
    pass_num += 1
    # If all comparisons are completed, end the while loop.
    if i == len(selected_list) - 1:
        done = 1


# Calculate the actual run time.
run_time = thread_time_ns() - start_time

# Print out the results

print(f'\nThe unsorted list:\n{temp_list}')

print(f'\nThe sorted list :\n{selected_list}')

print(f'\nThe list to be sorted had {len(selected_list)} {data_type} items in it.')
print(f'\nThe sorting process took {swap_count} swaps and the run time was:')

# Modified this section to display the run_time of the sort,
#   with the correct time units.

if run_time <= 1e3:
    print(f"\n\t--- {run_time:,.0f} nanoseconds ---")
elif run_time <= 1e6:
    print(f"\n\t--- {run_time/1e3:,.3f} microseconds ---")
elif run_time <= 1e9:
    print(f"\n\t--- {run_time/1e6:,.3f} milliseconds ---")
else:
    print(f"\n\t--- {run_time/1e9:,.3f} seconds ---")

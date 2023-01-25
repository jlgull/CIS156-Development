#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 7, Assignment Part B
# Program name: str_modifier.py

"""
----------
Part B

Create a program in a file named str_modifier.py that:

    Includes adequate instructions to the user about how to use the program.
    Asks the user for the name of their favorite sports team. The single input should be the
      name of the city and team name; for example: Phoenix Cardinals or Los Angeles Lakers
    Replaces all spaces with underscore characters. This must be done using a string method.
    Outputs the result.

Example (note that your program does not need to look, or behave, like exactly like this example -
  it is here to show you one way it might look when the program runs properly):

"""

#
# Import all required options
#
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

#
# Define the clear function definition for use in this program
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


# Variable List
#
# Integer Variables
#
#
# Floating Variables
#
# String Variables
#

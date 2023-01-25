#!/usr/bin/python3
#
# Author: Jonathan Heard
# Module 8, Assignment Part B
# Program name: baseball_players.py

"""
----------
Part B

Create a program called baseball_players.py that:

    Has a dictionary with seven baseball players (for example: Babe Ruth, Louis Gonzalez), etc.
      and their lifetime batting average (for example: .342, .283).
      One of the players must be Willie Mays who had a lifetime batting average of .301.
      (Note: a good reference to look up players can be found here: https://www.baseball-reference.com/
      Links to an external site.).
    Display the available players to the user.
    Prompt the user to enter one of the names. Instruct the user that proper capitalization and spaces are required.
    Display the batting average for the play that the user entered.
    The program repeats the previous three steps this until the user enters quit at the prompt.

Note: The program does NOT need to gracefully handle the error that may occur if the player is not
  found in the dictionary; for now, your program only needs to work when a player is entered correctly.

Note: If the program displays a .301 batting average as 0.301, that is OK.

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

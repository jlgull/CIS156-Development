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
    Display the batting average for the player that the user entered.
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
# Define functions and Import modules as required.

def clear():
    # Import system and name from the os module.
    from os import system, name

    # Found on this website: https://www.geeksforgeeks.org/clear-screen-python/
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.

    # If Windows, cls is used, else clear (for Mac and Linux)
    (system('cls')) if name == 'nt' else (system('clear'))


# Variable List
#
# Integer Variables
#
#
# Floating Variables
#
#
# String Variables
#
# player_select     - The player selected to show the lifetime batting average of.
#
# Dictionary Variables
#
# mlb_player_dic
#

#
# Preset any variables that need to be created prior to first use.
#

mlb_player_dic = {}

# Has a dictionary with seven baseball players (for example: Babe Ruth, Louis Gonzalez), etc.
#       and their lifetime batting average (for example: .342, .283).
#       One of the players must be Willie Mays who had a lifetime batting average of .301.
#       (Note: a good reference to look up players can be found here: https://www.baseball-reference.com/
#       Links to an external site.).
#       The site I used was: https://www.baseball-reference.com/leaders/batting_avg_career.shtml

# Fill the dictionary with the seven required baseball players and their lifetime batting average,
#   rounded to 3 digits after the decimal.

mlb_player_dic = {'Willie Mays': '0.301', 'Ty Cobb': '0.366', 'Ted Williams': '0.344', 'Babe Ruth': '0.342',
                  'Lou Gehrig': '0.340', 'Wade Boggs': '0.328', 'Joe DiMaggio': '0.325'}
# Use while, regarding the desire to re-run the program.
# Set the while control value to "Y".
do_again = "Y"
while do_again != "N":
    # Clear screen and start main program.
    #

    clear()

    #  Display the available players to the user.

    print(f'\nThis program contains a list of {len(mlb_player_dic)} MLB players.'
          f'\nHere are the players:')
    # Print the Players and their lifetime batting averages.
    print(f"{20 * '-'}")
    print(f"|{'Player Name':^18}|")
    print(20 * "-")
    for dic_key, dic_value in mlb_player_dic.items():
        print(f'|{dic_key:^18}|')
    print(20 * "-")

    #     Prompt the user to enter one of the names. Instruct the user that proper capitalization and spaces are required.

    player_select = input(f'\nEnter one of the names above, to show the players'
                          f'\n\tLifetime Batting Average.'
                          f'\nSpelling, Spacing and Capitalization must match that shown: ')

    #     Display the batting average for the player that the user entered.

    print(f'\nThe Lifetime Batting average for - {player_select} - is: '
          f'{mlb_player_dic.get(f"{player_select}", "The name entered is unknown or misspelled")}.')

    '''
    print(f'\nThis program contains a list of {len(mlb_player_dic)} MLB players'
          f'\nand their lifetime batting averages. Here is the list:')
    # Print the Players and their lifetime batting averages.
    print(f"{45 * '-'}")
    print(f"|{'Player Name':^16}| {f'Lifetime Batting Average':^24} |")
    print(45 * "-")
    for dic_key, dic_value in mlb_player_dic.items():
        print(f'|{dic_key:^16}| {dic_value:^24} |')
    print(45 * "-")

    '''

    #     The program repeats the previous steps this until the user enters quit at the prompt.

    # Ask if the user would like to play again.
    # Also, validate for the correct response.
    while True:
        do_again = input("\nWould you like to play again? Enter (Y) for yes or (N) for no. ").upper()
        # do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or a N.")

# End of program

player_dict = {'Willie Mays': .301, 'Babe Ruth': .342, 'Louis Gonzalez': .283, 'Roberto Clemente': .317, 'Barry Bonds': .298, 'Hank Aaron': .305, 'Ted Williams': .344}

while True:

    print()
    for k,v in player_dict.items():
        print(f'{k}')

    player_name = input('\nPlease enter the name of a player from the list. Proper capitalization and spaces are required (enter quit to quit): ')

    if player_name == 'quit':
        break
    else:
        print(f"\n{player_name}'s lifetime batting average is {player_dict[player_name]}")

print('\nThanks for using my program!')

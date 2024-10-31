import random
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack, cli_coordinates_input

players = {}

def generate_attack():
    '''
    Generates randomly the coordinates a player (AI opponent) will attack
    Returns the coordinates in form of a tuple
    '''
    y = random.randint(0, 9)
    x = random.randint(0, 9)

    return (y, x)

def ai_opponent_game_loop():
    '''
    Simulates a battleship game between 2 players, the user and an AI
    Prints if any of the users hit a ship 
    When one of the players has no more battleships left, it prints if the user lost of won the game
    Returns True
    '''
    print("Welcome to the game!")

    user_board = initialise_board()
    user_ships = create_battleships()
    players['user'] = [place_battleships(user_board, user_ships, "Custom"), user_ships]


    opp_board = initialise_board()
    opp_ships = create_battleships()
    players['opp'] = [place_battleships(opp_board, opp_ships, "Random"), opp_ships]

    fleet_sizes = [sum(user_ships.values()), sum(opp_ships.values())]
    end = False

    while end != True:

        a_coords = cli_coordinates_input()
        res = attack(a_coords, players['opp'][0], players['opp'][1])
        if res:
            print("Hit!")
            fleet_sizes[1] -= 1
        else:
            print("Miss!")
        for el in opp_board:
            print(el)

        a_coords = generate_attack()
        res = attack(a_coords, players['user'][0], players['user'][1])
        print(a_coords)
        if res:
            print("Hit!")
            fleet_sizes[0] -= 1
        else:
            print("Miss!")
        for el in user_board:
            print(el)

        if fleet_sizes[0] == 0 or fleet_sizes[1] == 0:
            end = True

        print(fleet_sizes[0], fleet_sizes[1])
        

    if fleet_sizes[0] == 0:
        print("Game over! You lost")
    elif fleet_sizes[1] == 0:
        print("Game over! You won")

    return True

if __name__ == "__main__":
    ai_opponent_game_loop()
    


from components import initialise_board, create_battleships, place_battleships


def attack(coordinates, board, battleships):
    '''
    Receives arguments as the coordinates of the place the player wants to shoot, the opponent's board and the battleshops of the opponent
    Prints that a ship has been sunk if it has been sunk
    Returns a boolean, True if a ship has been hit and False if not
    '''
    if board[coordinates[0]][coordinates[1]] != None:
        battleships[board[coordinates[0]][coordinates[1]]] -= 1

        if (battleships[board[coordinates[0]][coordinates[1]]] == 0):
            print(board[coordinates[0]][coordinates[1]], "has been sunk")

        board[coordinates[0]][coordinates[1]] = None
        return True
    
    return False


def cli_coordinates_input():
    '''
    Asks to input the coordinates a player (our user) wants to attacks
    Returns the coordinates in form of a tuple
    '''
    y = int(input("Enter your row: "))
    x = int(input("Enter your column: "))
    print(y, x)

    return (y, x)

def simple_game_loop():
    '''
    Simulates a single player mode version of battleships, doesn't finish until you sank all the enemy ships
    Always returns True
    '''
    print("Welcome to the game!")

    empty_board = initialise_board()
    ships = create_battleships()
    ship_board = place_battleships(empty_board, ships, "Custom")

    fleet_size = sum(ships.values())
    while fleet_size != 0:
        
        
        a_coords = cli_coordinates_input()
        res = attack(a_coords, ship_board, ships)

        if res:
            print("Hit!")
            fleet_size -= 1
        else:
            print("Miss!")

        for line in ship_board:
            print(line)

    print("Game over!")

    return True

    

if __name__ == "__main__":
    simple_game_loop()

    


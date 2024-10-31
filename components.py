import random
import json

def initialise_board(size = 10):
    '''
    Receives a parameter 'size' with default value of 10
    Initializes and returns an empty board in a form of list of lists of None with size*size dimensions
    '''
    board = [[None] * size for i in range(size)]
    return board

def create_battleships(filename = "battleships.txt"):
    '''
    Accepts a txt file with a set default name containing the name of the battleships and their size
    Opens and read the file, then converts it into an easy to use dictionary, then returns the dictionary
    '''
    bships = open(filename,"r")
    bships = bships.readlines()
    battleships = {}

    for line in bships:
        key, value = line.strip().split(':')
        battleships[key] = int(value)

    return battleships

def place_battleships(board, ships, algorithm = "Simple"):
    '''
    Receives an empty board, dictionary of available ships and an optional comp which is the type of placement with a default value of 'Simple'
    Has an imbedded function check_fits() which checks if a given ship can be placed on certain spot given its length and direction and thus returns a Boolean
    The function itself returns a board with battleships placed in 3 possible type of placements
    '''
    def check_fits(y, x, dir, ship):
        for i in range(ships[ship]):
                if dir == "v":
                    if y + ships[ship] >= 10:
                        return False
                    if board[y + i][x] != None:
                        return False
                    
                elif dir == "h":
                    if x + ships[ship] >= 10:
                        return False
                    if board[y][x + i] != None:
                        return False      
        return True
                            
    if algorithm == "Simple":
        row = 0
        for ship in ships:
            for i in range(0, ships[ship]):
                board[row][i] = ship
            row += 1

    elif algorithm == "Random":
        for ship in ships:
            found = False
            while found != True:
                orientation = random.choice(["h", "v"])
                start_row = random.randint(0, 9)
                start_col = random.randint(0, 9)
                ans = check_fits(start_row, start_col, orientation, ship)
                if ans:
                    #print(ship, start_row, start_col, orientation)
                    for i in range(ships[ship]):
                        if orientation == "v":
                            board[start_row + i][start_col] = ship
                        elif orientation == "h":
                            board[start_row][start_col + i] = ship
                    found = True     

    elif algorithm == "Custom":
        with open("placement.json") as file:
            plc = json.load(file)

        for ship, coords in plc.items():
            start_row, start_col, orientation = int(coords[1]), int(coords[0]), coords[2]

            for i in range(ships[ship]):
                #print(ships[ship])
                if orientation == "v":
                    board[start_row + i][start_col] = ship
                elif orientation == "h":
                    board[start_row][start_col + i] = ship

    return board
    
empty_board = initialise_board()
ships = create_battleships()
ship_board = place_battleships(empty_board, ships, "Custom")





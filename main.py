from flask import Flask, render_template, jsonify, request, json
from components import initialise_board, create_battleships, place_battleships
from mp_game_engine import generate_attack
from game_engine import attack

app = Flask(__name__)

players = {}
fleet_sizes = [None, None]


@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():

    """
    Accepts a post request containing the players board in the form of a config.json
    also accepts a get request which returns the placement.html template with a ships dictionary and a board size
    :return:
    """

    # SHIPS WOULD BE THE RETURN OF A BATTLESHIPS FUNCTION FROM YOUR GAME LOGIC
    ships = create_battleships()
    board_size = 10

    if request.method == "GET":
        return render_template("placement.html", ships = ships, board_size = board_size)

    if request.method == "POST":
        # DATA HERE IS A DICTIONARY WITH THE SAME FORMAT AS CONFIG.JSON
        # YOU WOULD WANT TO TAKE DATA AND CREATE A BOARD USING THE INFORMATION
        # THIS BOARD WOULD THEN BE USED WHEN RENDERING MAIN.HTML
        data = request.get_json()
        print(data)
        with open('placement.json', 'w') as placement:
            json.dump(data, placement)

        return jsonify({"message": "success"}), 200

@app.route(rule='/', methods=['GET'])
def root():
    """
    Returns the main.html template, passing
    a player board to the template
    :return:
    """

    empty_board = initialise_board()
    user_ships = create_battleships()
    user_board = place_battleships(empty_board, user_ships, "Custom")
    fleet_sizes[0] = sum(user_ships.values())
    players['user'] = [user_board, user_ships]

    # THE BOARD HERE WOULD BE A BOARD BASED ON THE DATA RECEIVED FROM THE PLACEMENT INTERFACE


    empty_board = initialise_board()
    opp_ships = create_battleships()
    fleet_sizes[1] = sum(opp_ships.values())
    opp_board = place_battleships(empty_board, opp_ships, "Random")
    players['opp'] = [opp_board, opp_ships]

    return render_template("main.html", player_board = user_board)

@app.route('/attack', methods=['GET'])
def process_attack():
    """
    Accepts get request contains two parameters x and y
    if game finished respond with jsonify {hit: True/False, AI_Turn: (x,y), finished: "SOME MESSAGE"}
    :return:
    """
    
    if request.args:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        #print(x, y)
        # THIS X AND Y REPRESENT THE PLAYERS TURN AGAINST THE AI

        user_hit = attack((y, x), players['opp'][0], players['opp'][1])
        if user_hit: fleet_sizes[1] -= 1

        
        

        ai_coords = generate_attack()
        ai_hit = attack(ai_coords, players['user'][0], players['user'][1])
        if ai_hit: fleet_sizes[0] -= 1


        
        # THIS IS A PLACEHOLDER FOR THE GAME FINISHED LOGIC
        # THIS WOULD USE YOUR BATTLESHIP GAME LOGIC TO CHECK IF THE GAME HAS FINISHED
    
        if fleet_sizes[1] == 0:
            return jsonify({"hit": user_hit, "AI_Turn": ai_coords, "finished": "You won"})
        elif fleet_sizes[0] == 0:
            return jsonify({"hit": user_hit, "AI_Turn": ai_coords, "finished": "You lost"})
        else:
            return jsonify({"hit": user_hit, "AI_Turn": ai_coords})


if __name__ == '__main__':
    app.template_folder = "templates"
    app.run()





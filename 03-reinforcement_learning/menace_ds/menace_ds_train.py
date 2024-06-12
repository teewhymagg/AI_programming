# 22200849, 22207839

# Import necessary libraries
from random import randint
import json
# menace_ds contains the Menace class that creates hash map to store Menace values
from menace_ds import Menace

# Function to check if the current state is a final state and return relevant information


def final_state(state):
    """Function returns 3 values:
        1. Bool: check if winning state is achieved
        2. state
        3. Bool: check if there are any "_" left"""
    # Check rows for a win
    for i in range(0, 7, 3):
        if state[i] == state[i+1] and state[i] == state[i+2] and state[i] != "_":
            return True, state, True
    # Check columns for a win
    for i in range(0, 3):
        if state[i] == state[i+3] and state[i] == state[i+6] and state[i] != "_":
            return True, state, True
    # Check diagonals for a win
    if (state[0] == state[4] and state[0] == state[8] and state[0] != "_") or (state[2] == state[4] and state[2] == state[6] and state[2] != "_"):
        return True, state, True
    # Check if there are any empty spaces left
    if "_" not in state:
        return True, state, False
    return False, state, False

# Function to play one game of Tic Tac Toe using Menace


def OneGame(menace):
    state = "_________"  # Initial empty state
    history = []  # Record of moves and states
    while not final_state(state)[0]:  # Continue until a final state is reached
        if state not in menace.keys():
            # Initialize state in menace dictionary if not present
            menace[state] = [300 for _ in state if _ == "_"]
        move = None
        while move == None:
            # Choose a move based on Menace's strategy
            move = choose(menace[state], state)
        # Append state and move (that will be displayed in next state)
        history.append((state, move))
        state = make_move(state, move)  # Update the state with the chosen move

    if final_state(state)[2] == True:
        # Determine the winner based on the final state
        winner = final_state(state)[1][history[-1][-1]]
    else:
        winner = None
    # Update Menace's strategy based on the game outcome
    update_menace(menace, history, winner)
    return menace

# Function to determine the winner of the game


def who_is_winner(state):
    # Check rows for a win
    for i in range(0, 7, 3):
        if state[i] == state[i+1] == state[i+2] and state[i] != "_":
            return state[i]

    # Check columns for a win
    for i in range(0, 3):
        if state[i] == state[i+3] == state[i+6] and state[i] != "_":
            return state[i]

    # Check diagonals for a win
    if (state[0] == state[4] == state[8] and state[0] != "_") or (state[2] == state[4] == state[6] and state[2] != "_"):
        return state[4]

    return None

# Function to get a unique identifier for a cell in a state


def get_weight_id(state, cell_on_state):
    weight_ids = 0
    weight_ids_dict = {}
    for i, cell in enumerate(state):
        if cell == "_":
            weight_ids_dict[i] = weight_ids
            weight_ids += 1
    return weight_ids_dict[cell_on_state]

# Function to update Menace's strategy based on the game outcome


def update_menace(menace, history, winner):
    for i, (state, move) in enumerate(history):
        weight_id = get_weight_id(state, move)
        if i % 2 == 0 and winner == 'X':  # Winner is X => reward
            menace[state][weight_id] += 3
        if i % 2 == 0 and winner == 'O':  # Winner is O, Looser is X => penalty
            menace[state][weight_id] -= 1
            if menace[state][weight_id] < 0:
                menace[state][weight_id] = 50
        if i % 2 == 1 and winner == 'O':  # Winner is O => reward
            menace[state][weight_id] += 3
        if i % 2 == 1 and winner == 'X':  # Winner is X, Looser is O => penalty
            menace[state][weight_id] -= 1
            if menace[state][weight_id] < 0:  # If weight gets less than 0 => update weight to 50
                menace[state][weight_id] = 50
        else:
            continue

# Function to make a move in the Tic Tac Toe game


def make_move(state, move):
    Xn = 0
    On = 0
    for i in state:
        if i == "X":
            Xn += 1
        elif i == "O":
            On += 1
    if Xn > On:
        state = state[0:move]+"O"+state[move+1:]
    else:
        state = state[0:move]+"X"+state[move+1:]
    return state

# Function to choose a move based on Menace's strategy


def choose(weights, state):
    empties = [i for i, cell in enumerate(state) if cell == "_"]
    total = sum(weights)

    if total == 0:
        # All weights are zero, return the first empty cell
        return empties[0]

    try:
        roll = randint(1, total)
    except ValueError:
        # Handle the exception by choosing a random index from available empty cells
        return empties[randint(0, len(empties)-1)]

    for i, empty_cell_id in enumerate(empties):
        roll = roll - weights[i]
        if roll <= weights[i]:
            return empty_cell_id

    # This should not be reached, but return the first empty cell as a fallback
    return empties[0]

# Function to train Menace by playing multiple games


def train(menace, n):
    for i in range(n):
        if i % 10000 == 0:
            print(i)
        menace = OneGame(menace)
    return menace


# Main block to run Menace and save the trained strategy
if __name__ == "__main__":
    menace = Menace()  # Initialize Menace
    # Train Menace for 15000 games and print the resulting strategy
    print(train(menace, 10000000)['_________'])

    dictionary = menace.return_normal_dict  # Get the strategy as a dictionary
    with open("weights_ds.json", "w") as json_file:
        # Save the strategy to a JSON file
        json.dump(dictionary, json_file, indent=4)

    # Save the strategy to a binary file
    menace.dump_to_binary_file("weights_ds.bin")

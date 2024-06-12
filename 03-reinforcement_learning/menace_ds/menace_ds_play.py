# 22200849, 22207839

# Import necessary libraries
from menace_ds_train import who_is_winner, final_state, make_move
from menace_ds import Menace


def print_board(board_str):
    # Function to print the Tic Tac Toe board
    board = [list(board_str[i:i+3]) for i in range(0, 9, 3)]

    line = "-------------"
    row_format = "| {} | {} | {} |"

    print(line)
    for row in board:
        print(row_format.format(*row))
        print(line)


def allowed(board, move):
    # Check if the move is allowed on the board
    if move == None:
        return False
    elif (0 <= move <= 8) and (board[move] == "_"):
        return True
    else:
        return False


def user_turn(board):
    # Function to handle user's turn
    move = None
    while not allowed(board, move):
        move = int(input("Select number where to place [0-8]"))
    board = make_move(board, move)
    print(f"User did {board} - {move}")
    return board


def ai_turn(board):
    # Function to handle AI's turn
    weights_turn = menace_weights[board]
    move = get_state_cell_id(board, weights_turn.index(max(weights_turn)))
    board = make_move(board, move)
    print(f"AI did {board} - {move}")
    return board


def get_state_cell_id(state, weight_id):
    # Function to get the cell ID based on the weight ID
    state_empty_cell_ids = {}
    empties = 0
    for key, value in enumerate(state):
        if value == "_":
            state_empty_cell_ids[empties] = key
            empties += 1
    return state_empty_cell_ids[weight_id]


# Load Menace weights from the binary file
menace_weights = Menace().read_binary_weights("weights_ds.bin")
board = "_________"

# Decide who plays first
who_first = input("Do you want to play first? [Y/n]")
if who_first.lower() == "y":
    # User plays first
    while not final_state(board)[0]:
        print_board(board)
        board = user_turn(board)
        try:
            board = ai_turn(board)
            winner = who_is_winner(board)
        except KeyError:
            winner = who_is_winner(board)
            print(f"Winner is {winner}")
else:
    # AI plays first
    board = ai_turn(board)
    while not final_state(board)[0]:
        print_board(board)
        board = user_turn(board)
        try:
            board = ai_turn(board)
            winner = who_is_winner(board)
        except KeyError:
            winner = who_is_winner(board)
            print(f"Winner is {winner}")

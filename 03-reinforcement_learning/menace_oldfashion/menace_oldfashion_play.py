# 22200849, 22207839

import json
from menace_oldfashion_train import who_is_winner, final_state, make_move


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
    return board


def ai_turn(board):
    # Function to handle AI's turn
    weights_turn = menace_weights[board]
    weight_turn_dict = {key: value for key, value in enumerate(weights_turn)}
    move = max(weight_turn_dict, key=weight_turn_dict.get)
    board = make_move(board, move)
    return board


weights_file = open("weights_oldfashion.json", "r")
menace_weights = json.load(weights_file)

board = "_________"


# game body
# until not final state continue playing ai-human-ai... or human-ai-human...
who_first = input("Do you want to play first? [Y/n]")
if who_first.lower() == "y":
    while not final_state(board)[0]:
        print_board(board)
        board = user_turn(board)
        try:
            board = ai_turn(board)
            winner = who_is_winner(board)
            print(f"Winner is {winner}")
        except KeyError:
            winner = who_is_winner(board)
            print(f"Winner is {winner}")
else:
    board = ai_turn(board)
    while not final_state(board)[0]:
        print_board(board)
        board = user_turn(board)
        try:
            board = ai_turn(board)
            winner = who_is_winner(board)
            print(f"Winner is {winner}")
        except KeyError:
            winner = who_is_winner(board)
            print(f"Winner is {winner}")


weights_file.close()

# 22200849, 22207839
# this menace does not use any optimizaitions like rotation or mirroring of
# the board to increase training effectiveness

from random import randint
import json


def final_state(state):
    """Function returns 3 values:
        1. Bool: check if winning state is achieved
        2. state
        3. Bool: check if there are any "_" left"""
    for i in range(0, 7, 3):
        if state[i] == state[i+1] and state[i] == state[i+2] and state[i] != "_":
            return True, state, True
    for i in range(0, 3):
        if state[i] == state[i+3] and state[i] == state[i+6] and state[i] != "_":
            return True, state, True
    if (state[0] == state[4] and state[0] == state[8] and state[0] != "_") or (state[2] == state[4] and state[2] == state[6] and state[2] != "_"):
        return True, state, True
    if "_" not in state:
        return True, state, False
    return False, state, False


def OneGame(menace):
    state = "_________"
    history = []
    while not final_state(state)[0]:
        if state not in menace.keys():
            menace[state] = [300 for i in range(9)] # we took 300 as compromise

        numbered_weights = {}
        for key, value in enumerate(menace[state]):
            if state[key] == "_":
                numbered_weights.update({key: value})
        move = None
        while move == None:
            move = choose(menace[state], numbered_weights)
        history.append((state, move))
        state = make_move(state, move)

    if final_state(state)[2] == True:
        winner = final_state(state)[1][history[-1][-1]]
    else:
        winner = None
    update_menace(menace, history, winner)
    return menace


def who_is_winner(state):
    for i in range(0, 7, 3):
        if state[i] == state[i+1] == state[i+2] and state[i] != "_":
            return state[i]

    for i in range(0, 3):
        if state[i] == state[i+3] == state[i+6] and state[i] != "_":
            return state[i]

    if (state[0] == state[4] == state[8] and state[0] != "_") or (state[2] == state[4] == state[6] and state[2] != "_"):
        return state[4]

    return None


def update_menace(menace, history, winner):
    for i, (state, move) in enumerate(history):
        if i % 2 == 0 and winner == 'X':
            menace[state][move] += 3
        if i % 2 == 0 and winner == 'O':
            menace[state][move] -= 1
            if menace[state][move] < 0:
                menace[state][move] = 0
        if i % 2 == 1 and winner == 'O':
            menace[state][move] += 3
        if i % 2 == 1 and winner == 'X':
            menace[state][move] -= 1
            if menace[state][move] < 0:
                menace[state][move] = 0
        else:
            menace[state][move] -= 1
            if menace[state][move] < 0:
                menace[state][move] = 0


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


def choose(weights, numbered_weights):
    total = sum(weights)
    roll = randint(1, total)
    for i in range(0, len(weights)):
        # print(roll)
        roll = roll - weights[i]
        if roll <= weights[i] and i in numbered_weights.keys():
            return i


menace = {}


def train(menace, n):
    for i in range(n):
        if i % 10000 == 0:
            print(i)
        menace = OneGame(menace)
    return menace


if __name__ == "__main__":
    # this will take long, so stick to provided weights file
    print(train(menace, 10000000)['_________'])

    with open("weights_oldfashion.json", "w") as json_file:
        json.dump(menace, json_file, indent=4)

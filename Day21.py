import numpy as np
from functools import lru_cache

def DeterminedDice():
    f = open("input day 21.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()
    lines[0] = lines[0][:-1]
    P1pos = int(lines[0].split(' ')[-1])
    P2pos = int(lines[1].split(' ')[-1])
    P1Score = 0
    P2Score = 0
    rolls = np.array([1, 2, 3], dtype=int)
    turns = 0
    while True:
        for number in rolls:
            if number > 100:
                number -= 100
        P1pos += np.sum(rolls)
        if P1pos % 10 == 0:
            P1Score += 10
            P1pos = 10
        else:
            P1Score += P1pos % 10
            P1pos %= 10
        turns += 3
        if P1Score >= 1000:
            print(turns * P2Score)
            print(turns, P1Score, P2Score)
            break
        rolls += 3

        for number in rolls:
            if number > 100:
                number -= 100
        P2pos += np.sum(rolls)
        if P2pos % 10 == 0:
            P2Score += 10
            P2pos = 10
        else:
            P2Score += P2pos % 10
            P2pos %= 10
        turns += 3
        if P2Score >= 1000:
            print(turns * P1Score)
            print(turns, P1Score, P2Score)
            break
        rolls += 3

        #if # in rolls > 100, # -= 100
        #player 1 position += sum(rolls)
        #if player1 position > 10, player1 pos -= 9
        #player1 score += player1 position
        #turns += 1
        #if player1 score >= 1000, end game, print(turns * player2 score)

def DiracMain():
    f = open("input day 21.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    lines[0] = lines[0][:-1]
    P1pos = int(lines[0].split(' ')[-1])
    P2pos = int(lines[1].split(' ')[-1])
    wins = DiracDice(P1pos, 0, P2pos, 0)
    print(wins)
    print(max(wins))

rolls = np.array([3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9], dtype=int)

@lru_cache(maxsize=None)
def DiracDice(my_pos, my_score, other_pos, other_score):
    if my_score >= 21:
        return 1, 0

    if other_score >= 21:
        return 0, 1

    my_wins = other_wins = 0

    for roll in rolls:
        new_pos = (my_pos + roll) % 10
        if new_pos == 0:
            new_pos = 10
        new_score = my_score + new_pos

        ow, mw = DiracDice(other_pos, other_score, new_pos, new_score)
        my_wins += mw
        other_wins += ow

    return my_wins, other_wins



#861062272302 too low

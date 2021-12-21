import numpy as np

def DeterminedDice():
    f = open("input day 21.txt", "r")
    #f = open("test.txt", "r")
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
    print(DiracDice(0, 0, P1pos, P2pos, 1))


def DiracDice(P1Score, P2Score, P1pos, P2pos, player):
    P1Won = 0
    P2Won = 0
    rolls = np.array([3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9], dtype=int)
    while P1Score < 21 and P2Score < 21:
        if player == 1:
            P1prevPos = P1pos
            P1prevScore = P1Score
            for roll in rolls:
                P1Score = P1prevScore
                P1pos = P1prevPos + roll
                if P1pos % 10 == 0:
                    P1Score += 10
                    P1pos = 10
                else:
                    P1Score += P1pos % 10
                    P1pos %= 10

                if P1Score >= 21:
                    P1Won += 1
                else:
                    P1, P2 = DiracDice(P1Score, P2Score, P1pos, P2pos, 2)
                    P1Won += P1
                    P2Won += P2
            player = 2

        if player == 2:
            P2prevPos = P2pos
            P2prevScore = P2Score
            for roll in rolls:
                P2Score = P2prevScore
                P2pos = P2prevPos + roll
                if P2pos % 10 == 0:
                    P2Score += 10
                    P2pos = 10
                else:
                    P2Score += P2pos % 10
                    P2pos %= 10

                if P2Score >= 21:
                    P2Won += 1
                else:
                    P1, P2 = DiracDice(P1Score, P2Score, P1pos, P2pos, 1)
                    P1Won += P1
                    P2Won += P2
            player = 1
    print(P1Won, P2Won)
    return P1Won, P2Won




#Diracdice(1score, 2score, 1pos, 2pos)
    #1won = 0
    #2won = 0
    #while 1score < 21 and 2score < 21:
        #

def OctopusBingo():
    f = open("input day 4.txt", "r")
#    f = open("test.txt", "r")
    lines = f.readlines()
    numbers = lines[0]
    numbers = numbers.split(',')
    numbers[-1] = numbers[-1][:-1]
    print(numbers)

    bingocards = []
    newcard = []
    i = 1
    while i < len(lines):
        if lines[i] == '\n':
            if newcard != []:
                bingocards.append(newcard)
            newcard = []
        else:
            newcard.append(lines[i][0:-1].split(' '))
        i += 1
    newcard[-1] = lines[i - 1].split(' ')
    bingocards.append(newcard)
    for card in bingocards:
        for line in card:
            for number in line:
                if number == '':
                    del line[line.index(number)]
    originalcards = bingocards.copy()

    result = bingofinder(bingocards, numbers)
    totalunmarked = 0
    for row in result[0]:
        for item in row:
            if item != 'X':
                totalunmarked += int(item)
    print('part 1')
    print(totalunmarked * int(numbers[result[1]]))

    print('part 2')
    while len(originalcards) > 0:
        result = bingofinder(originalcards, numbers)
        # returns [card, numbers.index(number), cards.index(card)]
        # winning card, index of winning number, index of winning card
        del originalcards[result[2]]
    print(result)

    totalunmarked = 0
    for row in result[0]:
        for item in row:
            if item != 'X':
                totalunmarked += int(item)
    print(totalunmarked * int(numbers[result[1]]))

def bingofinder(cards, numbers): # returns winning card, index of winning number, index of winning card
    bingoturns = []
    for number in numbers:
        for card in cards:
            winningturn = len(numbers)
            y = 0
            while y < len(card[0]):
                for getal in card[y]:
                    if getal == number:
                        card[y][card[y].index(getal)] = 'X'
                        if card[y] == ['X', 'X', 'X', 'X', 'X']:
                            if numbers.index(number) < winningturn:
                                winningturn = numbers.index(number)
                        x = 0
                        while x < len(card[0]):
                            if card[0][x] == 'X' and card[1][x] == 'X' and card[2][x] == 'X' and card[3][x] == 'X' and card[4][x] == 'X':
                                if numbers.index(number) < winningturn:
                                    winningturn = numbers.index(number)
                            x += 1
                #                        if card[0][0] == card[1][1] == card[2][2] == card[3][3] == card[4][4] == 'X':
                #                            if numbers.index(number) < winningturn:
                #                                winningturn = numbers.index(number)
                #                        if card[0][4] == card[1][3] == card[2][2] == card[3][1] == card[4][0] == 'X':
                #                            if numbers.index(number) < winningturn:
                #                                winningturn = numbers.index(number)
                #no diagonal bingo lol
                y += 1
            if winningturn < len(numbers):
                bingoturns.append(winningturn)
                #print(cards.index(card))
                return [card, numbers.index(number), cards.index(card)]
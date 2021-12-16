import numpy as np

def lowerNeighbor():
    f = open("input day 15.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()
    numbergrid = []
    for line in lines:
        numberrow = []
        if line[-1] == '\n':
            line = line[:-1]
        for number in line:
            numberrow.append(int(number))
        numbergrid.append(numberrow)
    numbergrid = np.asarray(numbergrid)
    path = [[0, 0]]
    risktotal = 0
    x = 0
    y = 0
    prevX = 0
    prevY = 0
    while x != np.size(numbergrid, 1) - 1 and y != np.size(numbergrid, 0) - 1:
        neighbors = []
        neighborlocations = []
        #if y > 0 and prevY != y - 1 and [x, y - 1] not in path:
        #    neighbors.append(numbergrid[y - 1][x])
        #    neighborlocations.append([x, y - 1])
        #if x > 0 and prevX != x - 1 and [x - 1, y] not in path:
        #    neighbors.append(numbergrid[y][x - 1])
        #    neighborlocations.append([x - 1, y])
        if y < np.size(numbergrid, 0) - 1 and prevY != y + 1 and [x, y + 1] not in path:
            neighbors.append(numbergrid[y + 1][x])
            neighborlocations.append([x, y + 1])
        if x < np.size(numbergrid, 1) - 1 and prevX != x + 1 and [x + 1, y] not in path:
            neighbors.append(numbergrid[y][x + 1])
            neighborlocations.append([x + 1, y])

        lowestneighbor = min(neighbors)
        path.append(neighborlocations[neighbors.index(lowestneighbor)])
        print(path)
        risktotal += lowestneighbor
        prevX = x
        prevY = y
        x, y = neighborlocations[neighbors.index(lowestneighbor)]
    print(risktotal)



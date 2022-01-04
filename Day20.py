import numpy as np

def imageEnhancer(cycles):
    f = open("input day 20.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    algorithmstring = lines[0][:-1]
    algorithm = np.zeros((1, len(algorithmstring)), dtype=int)

    i = 0
    while i < len(algorithmstring):
        if algorithmstring[i] == '#':
            algorithm[0][i] = 1
        i += 1

    i = 2
    grid = []
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        grid.append(lines[i])
        i += 1
    print(grid)
    npGrid = np.zeros((len(grid), len(grid[0])), dtype=int)
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == '#':
                npGrid[y, x] = 1

    cycle = 0
    while cycle < cycles:
        if cycle % 2 == 0:
            mode = True
            npGrid = np.pad(npGrid, 3)
        else:
            mode = False
            npGrid = np.pad(npGrid, 3, mode='constant', constant_values=1)
        newGrid = np.zeros(np.shape(npGrid), dtype=int)
        for y in range(0, np.shape(npGrid)[0]):
            for x in range(0, np.shape(npGrid)[1]):
                newGrid[y, x] = algorithm[0][Neighbors9(x, y, npGrid, mode)]
        npGrid = newGrid.copy()
        cycle += 1
    print(np.sum(npGrid))
    #5083 too high

def Neighbors9(x, y, npGrid, even):
    if even == True:
        mode = '0'
    else:
        mode = '1'
    neighbors = ''
    if x == 0 and y == 0:
        neighbors = 3 * mode + \
                    mode + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    mode + str(npGrid[y + 1, x]) + str(npGrid[y + 1, x + 1])
    elif x == 0 and y > 0 and y < np.shape(npGrid)[0] - 1:
        neighbors = mode + str(npGrid[y - 1, x]) + str(npGrid[y - 1, x + 1]) + \
                    mode + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    mode + str(npGrid[y + 1, x]) + str(npGrid[y + 1, x + 1])
    elif x == 0 and y == np.shape(npGrid)[0] - 1:
        neighbors = mode + str(npGrid[y - 1, x]) + str(npGrid[y - 1, x + 1]) + \
                    mode + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    3 * mode
    elif x > 0 and x < np.shape(npGrid)[1] - 1 and y == 0:
        neighbors = 3 * mode + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    str(npGrid[y + 1, x - 1]) + str(npGrid[y + 1, x]) + str(npGrid[y + 1, x + 1])
    elif x > 0 and x < np.shape(npGrid)[1] - 1 and y > 0 and y < np.shape(npGrid)[0] - 1:
        neighbors = str(npGrid[y - 1, x - 1]) + str(npGrid[y - 1, x]) + str(npGrid[y - 1, x + 1]) + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    str(npGrid[y + 1, x - 1]) + str(npGrid[y + 1, x]) + str(npGrid[y + 1, x + 1])
    elif x > 0 and x < np.shape(npGrid)[1] - 1 and y == np.shape(npGrid)[0] - 1:
        neighbors = str(npGrid[y - 1, x - 1]) + str(npGrid[y - 1, x]) + str(npGrid[y - 1, x + 1]) + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + str(npGrid[y, x + 1]) + \
                    3 * mode
    elif x == np.shape(npGrid)[1] - 1 and y == 0:
        neighbors = 3 * mode + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + mode + \
                    str(npGrid[y + 1, x - 1]) + str(npGrid[y + 1, x]) + mode
    elif x == np.shape(npGrid)[1] - 1 and y > 0 and y < np.shape(npGrid)[0] - 1:
        neighbors = str(npGrid[y - 1, x - 1]) + str(npGrid[y - 1, x]) + mode + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + mode + \
                    str(npGrid[y + 1, x - 1]) + str(npGrid[y + 1, x]) + mode
    elif x == np.shape(npGrid)[1] - 1 and y == np.shape(npGrid)[0] - 1:
        neighbors = str(npGrid[y - 1, x - 1]) + str(npGrid[y - 1, x]) + mode + \
                    str(npGrid[y, x - 1]) + str(npGrid[y, x]) + mode + \
                    3 * mode
    Algo_index = int(neighbors, 2)


    return Algo_index

import numpy as np

def SubmarineParking():
    f = open("input day 25.txt", "r")
    lines = f.readlines()

    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        i += 1
    oldgrid = np.zeros((len(lines), len(lines[0])), dtype=int)
    print(np.shape(oldgrid))
    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[0]):
            if lines[y][x] == '>':
                oldgrid[y, x] = 1
            if lines[y][x] == 'v':
                oldgrid[y, x] = 2
            x += 1
        y += 1
    print(oldgrid)
    prevgrid = np.zeros((np.shape(oldgrid)), dtype=int)

    count = 0
    while np.array_equal(oldgrid, prevgrid) != True:
        prevgrid = oldgrid.copy()
        newgrid = np.zeros((np.shape(oldgrid)), dtype=int)
        for y in range(0, np.shape(oldgrid)[0]):
            for x in range(0, np.shape(oldgrid)[1]):
                if x < np.shape(oldgrid)[1] - 1 and oldgrid[y, x] == 1 and oldgrid[y, x + 1] == 0:
                    newgrid[y, x + 1] = 1
                elif x == np.shape(oldgrid)[1] - 1 and oldgrid[y, x] == 1 and oldgrid[y, 0] == 0:
                    newgrid[y, 0] = 1
                elif oldgrid[y, x] == 1:
                    newgrid[y, x] = 1
                if oldgrid[y, x] == 2:
                    newgrid[y, x] = 2
        oldgrid = newgrid.copy()
        newgrid = np.zeros((np.shape(oldgrid)), dtype=int)
        for y in range(0, np.shape(oldgrid)[0]):
            for x in range(0, np.shape(oldgrid)[1]):
                if y < np.shape(oldgrid)[0] - 1 and oldgrid[y, x] == 2 and oldgrid[y + 1, x] == 0:
                    newgrid[y + 1, x] = 2
                elif y == np.shape(oldgrid)[0] - 1 and oldgrid[y, x] == 2 and oldgrid[0, x] == 0:
                    newgrid[0, x] = 2
                elif oldgrid[y, x] == 2:
                    newgrid[y, x] = 2
                if oldgrid[y, x] == 1:
                    newgrid[y, x] = 1
        oldgrid = newgrid.copy()
        count += 1
    print(count)

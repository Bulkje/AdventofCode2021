import numpy as np

def Octopuslight(steps):
    f = open("input day 11.txt", "r")
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
    step = 0
    print(numbergrid)
    totalflashes = 0
    while step < steps:
        numbergrid += 1
        flashed = np.zeros((10, 10), dtype=int)
        while np.amax(numbergrid) > 9:
            for x in range(10):
                for y in range(10):
                    if numbergrid[x, y] > 9 and flashed[x, y] == 0:
                        totalflashes += 1
                        flashed[x, y] = 1
                        numbergrid[x, y] = 0
                        if x > 0 and y > 0:
                            numbergrid[x - 1, y - 1] += 1
                        if y > 0:
                            numbergrid[x, y - 1] += 1
                        if x < 9 and y > 0:
                            numbergrid[x + 1, y - 1] += 1
                        if x > 0:
                            numbergrid[x - 1, y] += 1
                        if x < 9:
                            numbergrid[x + 1, y] += 1
                        if x > 0 and y < 9:
                            numbergrid[x - 1, y + 1] += 1
                        if y < 9:
                            numbergrid[x, y + 1] += 1
                        if x < 9 and y < 9:
                            numbergrid[x + 1, y + 1] += 1
        for x in range(10):
            for y in range(10):
                if flashed[x, y] == 1:
                    numbergrid[x, y] = 0
        print(numbergrid)
        step += 1
    print(totalflashes)

def Octopuslight_sync():
    f = open("input day 11.txt", "r")
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
    step = 0
    print(numbergrid)
    totalflashes = 0
    while True:
        numbergrid += 1
        flashed = np.zeros((10, 10), dtype=int)
        while np.amax(numbergrid) > 9:
            for x in range(10):
                for y in range(10):
                    if numbergrid[x, y] > 9 and flashed[x, y] == 0:
                        totalflashes += 1
                        flashed[x, y] = 1
                        numbergrid[x, y] = 0
                        if x > 0 and y > 0:
                            numbergrid[x - 1, y - 1] += 1
                        if y > 0:
                            numbergrid[x, y - 1] += 1
                        if x < 9 and y > 0:
                            numbergrid[x + 1, y - 1] += 1
                        if x > 0:
                            numbergrid[x - 1, y] += 1
                        if x < 9:
                            numbergrid[x + 1, y] += 1
                        if x > 0 and y < 9:
                            numbergrid[x - 1, y + 1] += 1
                        if y < 9:
                            numbergrid[x, y + 1] += 1
                        if x < 9 and y < 9:
                            numbergrid[x + 1, y + 1] += 1
        if np.array_equiv(flashed, np.ones((10, 10))):
            print(step + 1)
            break
        for x in range(10):
            for y in range(10):
                if flashed[x, y] == 1:
                    numbergrid[x, y] = 0
        print(numbergrid)
        step += 1

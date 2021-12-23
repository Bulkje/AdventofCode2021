import re

def Trickshot():
    f = open("input day 17.txt", "r")
    lines = f.readlines()
    numbers = re.sub(r'[^-\d]', " ", lines[0]).split(' ')
    print(numbers)
    Coords = []
    for item in numbers:
        if item != '':
            Coords.append(int(item))
    print(Coords)
    yMax = 0
    maxV = (0, 0)
    hits = []
    for xV in range(0, Coords[1] + 1):
        for yV in range(Coords[2], 300):
            yTajectory = []
            xSpeed = xV
            ySpeed = yV
            xPos = 0
            yPos = 0
            while xPos <= Coords[1] and yPos >= Coords[2]:
                xPos += xSpeed
                yPos += ySpeed
                yTajectory.append(yPos)
                if xPos >= Coords[0] and xPos <= Coords[1] and yPos >= Coords[2] and yPos <= Coords[3]:
                    hits.append(str((xV,yV )))
                    if max(yTajectory) > yMax:
                        yMax = max(yTajectory)
                        maxV = (xV, yV)
                    break
                if xSpeed != 0:
                    xSpeed -= 1
                ySpeed -= 1
    print(maxV, yMax, len(hits))

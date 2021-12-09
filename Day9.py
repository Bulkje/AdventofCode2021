#per location that != '9'
    #look at what neighbour is lowest
    #check if that number is a well
    #if not, look at what neighbour is closest from that
    #if location is well, add 1 to dict where key is well location
    #at the end, get the sizes of three largest entries in dict, multiply them together

def lavaflows_lowestpoints():
    f = open("input day 9.txt", "r")
    lines = f.readlines()
    lowestpoint = []
    locations = []

    line = 0
    while line < len(lines):
        if lines[line][-1] == '\n':
            lines[line] = lines[line][:-1]
        number = 0
        while number < len(lines[line]):
            nummer = int(lines[line][number])
            if line == 0:
                nummeronder = int(lines[line + 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummeronder:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummerlinks and nummer < nummeronder:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            if 0 < line < (len(lines) - 1):
                nummeronder = int(lines[line + 1][number])
                nummerboven = int(lines[line - 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummeronder and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummeronder and nummer < nummerlinks and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder and nummer < nummerboven:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            if line == len(lines) - 1:
                nummerboven = int(lines[line - 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummerlinks and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerboven and nummer < nummerlinks:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            number += 1
        line += 1
    sum = 0
    for point in lowestpoint:
        sum += point + 1
    print(sum)
    print(lowestpoint)
    print(locations)

#returns bool
def isWell(x, y, input):
    nummer = int(input[y][x])
    if y == 0:
        nummeronder = int(input[y + 1][x])
        if x != 0:
            nummerlinks = int(input[y][x - 1])
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
        if x == 0:
            if nummer < nummerrechts and nummer < nummeronder:
                return True
        elif x == len(input[y]) - 1:
            if nummer < nummerlinks and nummer < nummeronder:
                return True
        elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder:
            return True
    elif 0 < y < (len(input) - 1):
        nummeronder = int(input[y + 1][x])
        nummerboven = int(input[y - 1][x])
        if x != 0:
            nummerlinks = int(input[y][x - 1])
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
        if x == 0:
            if nummer < nummerrechts and nummer < nummeronder and nummer < nummerboven:
                return True
        elif x == len(input[y]) - 1:
            if nummer < nummeronder and nummer < nummerlinks and nummer < nummerboven:
                return True
        elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder and nummer < nummerboven:
            return True
    elif y == len(input) - 1:
        nummerboven = int(input[y - 1][x])
        if x != 0:
            nummerlinks = int(input[y][x - 1])
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
        if x == 0:
            if nummer < nummerrechts and nummer < nummerboven:
                return True
        elif x == len(input[y]) - 1:
            if nummer < nummerlinks and nummer < nummerboven:
                return True
        elif nummer < nummerrechts and nummer < nummerboven and nummer < nummerlinks:
            return True
    else:
        return False

#returns [x, y] of lowest neighbor
def lowerNeighbor(x, y, input):
    nummer = input[y][x]
    neighbors = []
    nummerlinks = 9
    nummerrechts = 9
    nummeronder = 9
    nummerboven = 9
    if y == 0:
        nummeronder = int(input[y + 1][x])
        neighbors.append(nummeronder)
        if x != 0:
            nummerlinks = int(input[y][x - 1])
            neighbors.append(nummerlinks)
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
            neighbors.append(nummerrechts)
    elif 0 < y < (len(input) - 1):
        nummeronder = int(input[y + 1][x])
        nummerboven = int(input[y - 1][x])
        neighbors.append(nummeronder)
        neighbors.append(nummerboven)
        if x != 0:
            nummerlinks = int(input[y][x - 1])
            neighbors.append(nummerlinks)
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
            neighbors.append(nummerrechts)
    elif y == len(input) - 1:
        nummerboven = int(input[y - 1][x])
        neighbors.append(nummerboven)
        if x != 0:
            nummerlinks = int(input[y][x - 1])
            neighbors.append(nummerlinks)
        if x < len(input[y]) - 1:
            nummerrechts = int(input[y][x + 1])
            neighbors.append(nummerrechts)
    laagste = min(neighbors)
    if laagste == nummerlinks:
        return [x - 1, y]
    if laagste == nummerrechts:
        return [x + 1, y]
    if laagste == nummerboven:
        return [x, y - 1]
    if laagste == nummeronder:
        return [x, y + 1]

#gets locations, makes dict with locations and checks all the locations and other stuff
def lavaflows_basins():
    f = open("input day 9.txt", "r")
    lines = f.readlines()
    lowestpoint = []
    locations = []
    
    line = 0
    while line < len(lines):
        if lines[line][-1] == '\n':
            lines[line] = lines[line][:-1]
        number = 0
        while number < len(lines[line]):
            nummer = int(lines[line][number])
            if line == 0:
                nummeronder = int(lines[line + 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummeronder:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummerlinks and nummer < nummeronder:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            if 0 < line < (len(lines) - 1):
                nummeronder = int(lines[line + 1][number])
                nummerboven = int(lines[line - 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummeronder and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummeronder and nummer < nummerlinks and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerlinks and nummer < nummeronder and nummer < nummerboven:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            if line == len(lines) - 1:
                nummerboven = int(lines[line - 1][number])
                if number != 0:
                    nummerlinks = int(lines[line][number - 1])
                if number < len(lines[line]) - 1:
                    nummerrechts = int(lines[line][number + 1])
                if number == 0:
                    if nummer < nummerrechts and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif number == len(lines[line]) - 1:
                    if nummer < nummerlinks and nummer < nummerboven:
                        lowestpoint.append(nummer)
                        locations.append([number, line])
                elif nummer < nummerrechts and nummer < nummerboven and nummer < nummerlinks:
                    lowestpoint.append(nummer)
                    locations.append([number, line])
            number += 1
        line += 1
    sum = 0
    for point in lowestpoint:
        sum += point + 1
    print(sum)
    print(lowestpoint)
    print(locations)
    Wells = {}
    for location in locations:
        Wells[str(location)] = 0

    y = 0
    while y < len(lines):
        x = 0
        while x < len(lines[y]):
            if int(lines[y][x]) < 9:
                pointX = x
                pointY = y
                while True:
                    coordinates = lowerNeighbor(pointX, pointY, lines)
                    pointX = coordinates[0]
                    pointY = coordinates[1]
                    if isWell(pointX, pointY, lines):
                        Wells[str(coordinates)] += 1
                        break
            x += 1
        y += 1

    #writing out a for loop
    print(Wells)
    answer = max(Wells, key=Wells.get)
    total = Wells[answer]
    Wells[answer] = 0
    answer = max(Wells, key=Wells.get)
    total *= Wells[answer]
    Wells[answer] = 0
    answer = max(Wells, key=Wells.get)
    total *= Wells[answer]
    print(total)
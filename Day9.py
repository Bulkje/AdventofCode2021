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

def lavaflows_basins():
    f = open("input day 9.txt", "r")
    # f = open("test.txt", "r")
    lines = f.readlines()
    lowestpoint = []
    locations = []
    #per location that != '9'
    #look at what neighbour is lowest
    #check if that number is a well
    #if not, look at what neighbour is closest from that
    #if neighbour is well, add 1 to dict where key is well location
    #at the end, get the sizes of three largest entries in dict, multiply them together
    #TODO
    #function to see if location is a well
    #def iswell(x, y) --> returns bool

    #function to see which neighbour is lowest
    #def isLower(x, y) --returns x, y of new location

    #
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




import re
from collections import defaultdict


def hydrothermalvents():
    f = open("input day 5.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    coords = []
    hydrovents = defaultdict(int)
    for line in lines:
        coords.append(re.findall(r'\d+', line))
        #print(re.findall(r'\d+', line))
    for location in coords:
        x1 = int(location[0])
        y1 = int(location[1])
        x2 = int(location[2])
        y2 = int(location[3])
        if y1 == y2:
            if x1 > x2:
                i = x2
                while i <= x1:
                    if (str(i) + ',' + str(y1)) in hydrovents:
                        hydrovents[(str(i) + ',' + str(y1))] += 1
                    else:
                        hydrovents[(str(i) + ',' + str(y1))] = 1
                    i += 1
            if x2 > x1:
                i = x1
                while i <= x2:
                    if (str(i) + ',' + str(y1)) in hydrovents:
                        hydrovents[(str(i) + ',' + str(y1))] += 1
                    else:
                        hydrovents[(str(i) + ',' + str(y1))] = 1
                    i += 1
        elif x1 == x2:
            if y1 > y2:
                i = y2
                while i <= y1:
                    if (str(x1) + ',' + str(i)) in hydrovents:
                        hydrovents[(str(x1) + ',' + str(i))] += 1
                    else:
                        hydrovents[str(x1) + ',' + str(i)] = 1
                    i += 1
            if y2 > y1:
                i = y1
                while i <= y2:
                    if (str(x1) + ',' + str(i)) in hydrovents:
                        hydrovents[str(x1) + ',' + str(i)] += 1
                    else:
                        hydrovents[str(x1) + ',' + str(i)] = 1
                    i += 1
        elif x1 == x2 and y1 == y2:
            if (str(x1) + ',' + str(y1)) in hydrovents:
                hydrovents[(str(x1) + ',' + str(y1))] += 1
            else:
                hydrovents[(str(x1) + ',' + str(y1))] = 1
        #print(hydrovents)
        elif x1 < x2 and y1 < y2: # \ top left to bottom right
            i = x1
            j = y1
            while i <= x2:
                if (str(i) + ',' + str(j)) in hydrovents:
                    hydrovents[str(i) + ',' + str(j)] += 1
                else:
                    hydrovents[str(i) + ',' + str(j)] = 1
                i += 1
                j += 1
        elif x2 < x1 and y1 < y2: # / top right to bottom left
            i = x1
            j = y1
            while i >= x2:
                if (str(i) + ',' + str(j)) in hydrovents:
                    hydrovents[str(i) + ',' + str(j)] += 1
                else:
                    hydrovents[str(i) + ',' + str(j)] = 1
                i -= 1
                j += 1
        elif x1 < x2 and y2 < y1: # / bottom left to top right
            i = x1
            j = y1
            while i <= x2:
                if (str(i) + ',' + str(j)) in hydrovents:
                    hydrovents[str(i) + ',' + str(j)] += 1
                else:
                    hydrovents[str(i) + ',' + str(j)] = 1
                i += 1
                j -= 1
        elif x2 < x1 and y2 < y1: # \ bottom right to top left
            i = x1
            j = y1
            while i >= x2:
                if (str(i) + ',' + str(j)) in hydrovents:
                    hydrovents[str(i) + ',' + str(j)] += 1
                else:
                    hydrovents[str(i) + ',' + str(j)] = 1
                i -= 1
                j -= 1
        #print(hydrovents)
    #print(hydrovents)
    print(sum(value > 1 for value in hydrovents.values()))
    #19717 too low
    #14857 too low


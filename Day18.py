import re
import ast
import math

def snailfishHW():
    f = open("input day 18.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        i += 1
    print(lines)
    snailfishNumbers = []
    for line in lines:
        line = ast.literal_eval(line)
        snailfishNumbers.append(line)

    #list of all the lists to be added
    print(snailfishNumbers)
    line = 0
    while line < len(lines) - 1:
        Cont = True
        snailNumber = '[' + lines[line] + ',' + lines[line + 1] + ']'
        while Cont == True:
            snailNumber, Cont = reduce(snailNumber)
        #print(snailNumber)
        line += 1
    print(snailNumber)
    print(magnitude(ast.literal_eval(snailNumber)))

def reduce(strList):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newStr = strList
    depth = 0
    i = 0
    leftIndex = -1
    while i < len(strList):
        if strList[i] == '[':
            depth += 1
        elif strList[i] == '0':
            leftNr = 0
            leftIndex = i
        elif strList[i] in numbers:
            leftNr = int(strList[i])
            leftIndex = i
        elif strList[i] == ']':
            depth -= 1

        #explode
        if depth > 4:
            pairIndex = (i, i + 4)
            first = int(strList[i + 1])
            second = int(strList[i + 3])
            rightIndex = i + 5
            while rightIndex < len(strList):
                if strList[rightIndex] in numbers:
                    rightNr = int(strList[rightIndex]) + second
                    break
                rightIndex += 1
            if rightIndex == len(strList):
                rightNr = None

            #does not work if exploding happens on the right
            if leftIndex == -1:
                newLeft = ''
                leftIndex = 0

                newStr = strList[:leftIndex]
                newStr += str(newLeft)
                newStr += strList[leftIndex:pairIndex[0]]
                newStr += '0' + strList[pairIndex[1] + 1]
                newStr += strList[pairIndex[1]:rightIndex - 2]

            else:
                newLeft = first + leftNr

                newStr = strList[:leftIndex]
                newStr += str(newLeft) + ','
                newStr += strList[leftIndex + 2:pairIndex[0]] + '0'
                newStr += strList[pairIndex[1] + 1]
                newStr += strList[pairIndex[1] + 2:rightIndex]

            if rightNr != None:
                #if newStr[-1] != ',':
                    #newStr += '['

                newStr += str(rightNr)
                newStr += strList[rightIndex + 1:]
            return newStr, True

        #split
        if strList[i] == '1' and strList[i + 1] in numbers:
            split = int(strList[i:i + 2])
            newPair = '[' + str(split // 2) + ',' + str(math.ceil(split / 2)) + ']'
            newStr = strList[:i] + newPair + strList[i + 2:]
            return newStr, True

        i += 1
    return strList, False

def magnitude(list):
    sum = 0
    if isinstance(list[0], int):
        sum += list[0] * 3
    else:
        sum += magnitude(list[0]) * 3
    if isinstance(list[1], int):
        sum += list[1] * 2
    else:
        sum += magnitude(list[1]) * 2
    return sum



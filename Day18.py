import itertools
import re
import ast
import math

def snailfishHW():
    f = open("input day 18.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        i += 1
    #print(lines)
    snailfishNumbers = []
    for line in lines:
        line = ast.literal_eval(line)
        snailfishNumbers.append(line)

    #list of all the lists to be added
    #print(snailfishNumbers)
    line = 0
    snailNumber = lines[0]
    while line < len(lines) - 1:
        Cont = True
        snailNumber = '[' + snailNumber + ',' + lines[line + 1] + ']'
        #print(snailNumber)
        while Cont == True:
            snailNumber, Cont = reduce(snailNumber)
            #print(snailNumber)
        line += 1
    #print(snailNumber)
    print(magnitude(ast.literal_eval(snailNumber)))

    maximum = 0
    for combination in itertools.combinations(snailfishNumbers, 2):
        Cont = True
        snailNumber = '[' + str(combination[0]) + ',' + str(combination[1]) + ']'
        while Cont == True:
            snailNumber, Cont = reduce(snailNumber)
        M = magnitude(ast.literal_eval(snailNumber))
        if M > maximum:
            maximum = M
    print(maximum)

def reduce(strList):
    strList.replace(' ', '')
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    newStr = strList
    depth = 0
    i = 0
    while i < len(strList):
        if strList[i] == '[':
            depth += 1
        elif strList[i] == ']':
            depth -= 1

        #explode
        if depth > 4:
            endIndex = strList[i:].index(']') + i + 1
            beginIndex = i
            pair = strList[beginIndex:endIndex]
            #print(pair)
            numbersInPair = re.findall('[0-9]+', pair)
            leftNumber = int(numbersInPair[0])
            rightNumber = int(numbersInPair[1])

            leftNumbers = re.search('[0-9]+(?!.*[0-9]+)', strList[:i])
            rightNumbers = re.search('[0-9]+', strList[endIndex:])

            if rightNumbers != None:
                newRightNumber = rightNumber + int(rightNumbers.group())
                newStr = newStr[:endIndex + rightNumbers.span()[0]] + str(newRightNumber) + newStr[endIndex + rightNumbers.span()[1]:]

            #put '0' in new string
            newStr = newStr[:i] + '0' + newStr[endIndex:]

            if leftNumbers != None:
                newLeftNumber = leftNumber + int(leftNumbers.group())
                newStr = newStr[:leftNumbers.span()[0]] + str(newLeftNumber) + newStr[leftNumbers.span()[1]:]

            return newStr, True
        i += 1
    i = 0
    while i < len(strList):
        if strList[i] in numbers and strList[i + 1] in numbers:
            split = int(strList[i:i + 2])
            #print(split)
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

#1752 too low

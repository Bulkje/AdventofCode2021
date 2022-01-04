import numpy as np

def packetVersionSum():
    f = open("input day 16.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()

    for code in lines:
        bin = ''
        for char in code:
            if char != '\n':
                bin += hexToBin(char)
        print(code)
        print(bin)
        sum = packetVersion(bin)
        print('Het antwoord is:', sum)

def literalPacket(packetBin):
    index = 0
    literal = ''
    version = int(packetBin[:3], 2)
    typeID = int(packetBin[3:6], 2)
    index += 6
    print(packetBin)
    while packetBin[index] == '1':
        index += 1
        literal += packetBin[index:index + 4]
        index += 4
    if packetBin[index] == '0':
        index += 1
        literal += packetBin[index:index + 4]
        index += 4
    value = int(literal, 2)
    newPacket = packetBin[index:]
    print(value)
    return version, value, newPacket

def packetVersion(packetBin, *Amount):
    version = 0
    index = 0
    if Amount:
        Amount = Amount[0]
        while Amount > 0:
            if Amount == 1:
                packetTuple = packetVersion(packetBin[index:], 1)
                version += packetTuple[0]
                index += packetTuple[1]
                Amount = 0
                break
            print(index)
            packetTuple = packetVersion(packetBin[index:])
            version += packetTuple[0]
            index += packetTuple[1]

            Amount -= 1

    while index < len(packetBin) - 7:
        #print(packetBin[index:])
        index += 3
        version += int(packetBin[index - 3:index], 2)
        typeID = int(packetBin[index:index + 3], 2)
        index += 3
        if typeID != 4:
            lenID = packetBin[index:index + 1]
            index += 1
            if lenID == '0':
                lengthSub = int(packetBin[index:index + 15], 2)
                index += 15
                packetTuple = packetVersion(packetBin[index:index + lengthSub])
                version += packetTuple[0]
                processedLen = packetTuple[1]
                while processedLen < lengthSub:
                    packetTuple = packetVersion(packetBin[index + processedLen:index + lengthSub + processedLen])
                    version += packetTuple[0]
                    processedLen += packetTuple[1]

                index += lengthSub

            elif lenID == '1':
                subAmount = int(packetBin[index:index + 11], 2)
                index += 11
                packetTuple = packetVersion(packetBin[index:], subAmount)
                version += packetTuple[0]
                index += packetTuple[1]
        else:
            packetTuple = literalPacket(packetBin[index:])
            version += packetTuple[0]
            index -= len(packetTuple[2])
            packetBin = packetTuple[2]
    return (version, len(packetBin))

#538 too low


def hexToBin(char):
    if char == '0':
        return '0000'
    elif char == '1':
        return '0001'
    elif char == '2':
        return '0010'
    elif char == '3':
        return '0011'
    elif char == '4':
        return '0100'
    elif char == '5':
        return '0101'
    elif char == '6':
        return '0110'
    elif char == '7':
        return '0111'
    elif char == '8':
        return '1000'
    elif char == '9':
        return '1001'
    elif char == 'A':
        return '1010'
    elif char == 'B':
        return '1011'
    elif char == 'C':
        return '1100'
    elif char == 'D':
        return '1101'
    elif char == 'E':
        return '1110'
    elif char == 'F':
        return '1111'


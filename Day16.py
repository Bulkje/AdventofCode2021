import numpy as np

def packetVersionSum():
    f = open("input day 16.txt", "r")
    lines = f.readlines()

    for code in lines:
        bin = ''
        for char in code:
            if char != '\n':
                bin += hexToBin(char)
        sum = totalVersion(bin)
        total = parseSingle(bin)
        print('Antwoord deel 1:', sum)
        print('Antwoord deel 2:', total[0])


def totalVersion(packetBin):
    version = int(packetBin[:3], 2)
    typeID = int(packetBin[3:6], 2)
    index = 6
    anotherPacket = True
    while anotherPacket == True:
        if typeID == 4:
            while packetBin[index] == '1':
                index += 5
            index += 5
            if len(packetBin) - index > 7:
                anotherPacket = True
            else:
                anotherPacket = False
        else:
            lenID = packetBin[index]
            index += 1
            if lenID == '0':
                index += 15
                anotherPacket = True
            else:
                index += 11
                anotherPacket = True
        if anotherPacket == True:
            version += int(packetBin[index:index + 3], 2)
            typeID = int(packetBin[index + 3:index + 6], 2)
            index += 6
    return version

def parseSingle(packetBin):
    typeID = int(packetBin[3:6], 2)
    if typeID == 4: #literal value
        return Type4(packetBin)
    else:
        values, length = queue(packetBin)
    if typeID == 0:
    #sum of contained values
        return sum(values), length
    elif typeID == 1:
    #product of contained values
        value = 1
        for number in values:
            value *= number
        return value, length
    elif typeID == 2:
    #minimum of contained values
        return min(values), length
    elif typeID == 3:
    #maximum of contained values
        return max(values), length
    elif typeID == 5:
    #returns 1 if 1st packet > 2nd packet, else 0
    #always contains 2 subpackets
        if values[0] > values[1]:
            return 1, length
        else:
            return 0, length
    elif typeID == 6:
    #returns 1 if 1st packet < 2nd packet, else 0
    #always contains 2 subpackets
        if values[0] < values[1]:
            return 1, length
        else:
            return 0, length
    elif typeID == 7:
    #returns 1 if 1st packet == 2nd packet, else 0
    #always contains 2 subpackets
        if values[0] == values[1]:
            return 1, length
        else:
            return 0, length

def queue(packetBin):
    values = []
    index = 6
    lenID = packetBin[index]
    index += 1
    if lenID == '0':
        lengthSub = int(packetBin[index:index + 15], 2)
        index += 15
        subPackets = packetBin[index:index + lengthSub]
        length = index
        while len(subPackets) > 6:
            packetTuple = parseSingle(subPackets)
            values.append(packetTuple[0])
            subIndex = packetTuple[1]
            length += subIndex
            subPackets = subPackets[subIndex:]
    else:
        amount = int(packetBin[index:index + 11], 2)
        index += 11
        length = index
        subPackets = packetBin[index:]
        subIndex = 0
        while len(values) < amount:
            packetTuple = parseSingle(packetBin[index + subIndex:])
            values.append(packetTuple[0])
            subIndex += packetTuple[1]
            length += packetTuple[1]
            subPackets = subPackets[subIndex:]
    return values, length

def Type4(packetBin):
    index = 6
    literal = ''
    while packetBin[index] == '1':
        index += 1
        literal += packetBin[index:index + 4]
        index += 4
    index += 1
    literal += packetBin[index:index + 4]
    index += 4
    value = int(literal, 2)
    return value, index

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


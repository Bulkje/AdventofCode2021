def day3():
    f = open("input day 3.txt", "r")
    lines = f.readlines()
    digits = []
    binary = []
    inverse = []
    gamma = 0
    epsilon = 0
    for digit in lines[0]:
        if digit == "0" or digit == "1":
            digits.append(0)
    for line in lines:
        i = 0
        while i < len(line):
            if line[i] == "1":
                digits[i] += 1
            i += 1
    i = 0
    while i < len(digits):
        if digits[i] >= (len(lines)/2):
            binary.append(1)
        else:
            binary.append(0)
        i += 1
    gamma = sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))
    for bit in binary:
        if bit == 1:
            inverse.append(0)
        else:
            inverse.append(1)
    epsilon = sum(val*(2**idx) for idx, val in enumerate(reversed(inverse)))
    print(gamma * epsilon)
    #16699856 too high

def day3_2():
    f = open("input day 3.txt", "r")
    lines = f.readlines()
    numbers = []
    for line in lines:
        numbers.append(line)
    print(oxygengenerator(numbers) * CO2Scrubber(numbers))


def oxygengenerator(list):
    bin = []
    for line in list:
        if '\n' in line:
            bin.append(line[0:-1])
        else:
            bin.append(line)
    i = 0
    while i < len(bin[0]):
        count = 0
        newlist = []
        for number in bin:
            if number[i] == '1':
                count += 1
        if count >= len(bin) / 2:
            for number in bin:
                if number[i] == '1':
                    newlist.append(number)
        else:
            for number in bin:
                if number[i] == '0':
                    newlist.append(number)
        bin = newlist
        i += 1
    print(bin)
    return int(bin[0], 2)

def CO2Scrubber(list):
    bin = []
    for line in list:
        if '\n' in line:
            bin.append(line[0:-1])
        else:
            bin.append(line)
    i = 0
    while i < len(bin[0]):
        count = 0
        newlist = []
        for number in bin:
            if number[i] == '0':
                count += 1
        if count <= len(bin) / 2:
            for number in bin:
                if number[i] == '0':
                    newlist.append(number)
        else:
            for number in bin:
                if number[i] == '1':
                    newlist.append(number)
        bin = newlist
        i += 1
        if len(bin) == 1:
            return int(bin[0], 2)
    return int(bin[0], 2)


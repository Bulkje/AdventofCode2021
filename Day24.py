import math

def ALU():
    f = open("input day 24.txt", "r")
    lines = f.readlines()
    #add
    #mul
    #div round down can't div by 0
    #mod can't have 0 as input
    #eql a b if true, a = 1. else a = 0
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        i += 1
    w = 0
    Vars = {"w":0, "x":0, "y":0, "z":0}
    for instruction in lines:
        operation = instruction.split()[0]
        if operation == 'add':
            Vars[instruction.split()[1]] += int(instruction.split()[2])
        elif operation == 'mul':
            Vars[instruction.split()[1]] *= int(instruction.split()[2])
        elif operation == 'div':
            Vars[instruction.split()[1]] /= int(instruction.split()[2])
            Vars[instruction.split()[1]] = math.floor(Vars[instruction.split()[1]])
        elif operation == 'mod' and Vars[instruction.split()[1]] != 0:
            Vars[instruction.split()[1]] %= int(instruction.split()[2])



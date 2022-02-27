import math
from functools import lru_cache



def ALU():
    f = open("input day 24.txt", "r")
    lines = f.readlines()
    #add
    #mul
    #div round down can't div by 0
    #mod can't have 0 as input
    #eql a b if true, a = 1 else a = 0
    i = 0
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        i += 1

    modelNumber = "99999999999999"
    Answer = False

    tries = 0
    while Answer == False:
        Answer = checkModelNr(modelNumber, lines)
        modelNr = int(modelNumber)
        modelNr -= 1
        modelNumber = str(modelNr)
        modelNumber.replace("0", "1")
        tries += 1
        print(tries)
    print("Het is goed!", int(modelNumber) + 1)



def checkModelNr(modelNumber, lines):
    digit = 13
    Vars = {"w":0, "x":0, "y":0, "z":0}
    for instruction in lines:
        if len(instruction) < 6:
            Vars["w"] = int(modelNumber[digit])
            digit -= 1
        else:
            items = instruction.split()
            operation = items[0]
            if items[2] in Vars.keys():
                if operation == 'add':
                    Vars[items[1]] += Vars[items[2]]
                elif operation == 'mul':
                    Vars[items[1]] *= Vars[items[2]]
                elif operation == 'div':
                    if Vars[items[2]] != 0:
                        Vars[items[1]] /= Vars[items[2]]
                        Vars[items[1]] = math.floor(Vars[items[1]])
                    else:
                        print('GODVERDOMME DOOR NUL GEDEELD')
                elif operation == 'mod':
                    Vars[items[1]] %= Vars[items[2]]
                elif operation == 'eql':
                    if Vars[items[1]] == Vars[items[2]]:
                        Vars[items[1]] = 1
                    else:
                        Vars[items[1]] = 0


            elif operation == 'add':
                Vars[items[1]] += int(items[2])
            elif operation == 'mul':
                Vars[items[1]] *= int(items[2])
            elif operation == 'div':
                Vars[items[1]] /= int(items[2])
                Vars[items[1]] = math.floor(Vars[items[1]])
            elif operation == 'mod' and Vars[items[1]] != 0:
                Vars[items[1]] %= int(items[2])
    if Vars["z"] == 0:
        return True
    else:
        return False




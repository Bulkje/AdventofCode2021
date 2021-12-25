import re

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
    depth = 0
    number = list(lines[0])
    i = 0
    while i < len(lines):
        number.append(list(lines[i]))





        i += 1

def reduceNumber(list):
    print('TODO')
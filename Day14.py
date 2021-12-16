def polymer(steps):
    f = open("input day 14.txt", "r")
    lines = f.readlines()
    input = lines[0][:-1]
    letters = []
    for letter in input:
        letters.append(letter)
    codes = []
    i = 2
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        code = []
        code.append(lines[i].split(' ')[0])
        code.append(lines[i].split(' ')[2])
        codes.append(code)
        i += 1
    print(input)
    print(codes)
    step = 0
    while step < steps:
        newcode = input
        letterindex = 1
        while letterindex < len(input):
            prevletter = input[letterindex - 1]
            currletter = input[letterindex]
            for code in codes:
                if prevletter + currletter in code[0]:
                    newcode = newcode.replace(code[0], (prevletter + code[1] + currletter), 1)
            letterindex += 1

        input = newcode
        step += 1
        print(step)
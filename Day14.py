def polymer(steps):
    f = open("input day 14.txt", "r")
    #f = open("test.txt", "r")
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
    firstletter = input[0]
    lastletter = input[-1]
    print(codes)
    step = 0
    combinations = {}
    letterindex = 1
    while letterindex < len(input):
        prevletter = input[letterindex - 1]
        currletter = input[letterindex]
        if (prevletter + currletter) in combinations:
            combinations[prevletter + currletter] += 1
        else:
            combinations[prevletter + currletter] = 1
        letterindex += 1
    print(combinations)

    newdict = combinations.copy()
    olddict = combinations.copy()
    while step < steps:
        for key in olddict:
            if olddict[key] > 0:
                for code in codes:
                    if key == code[0]:
                        value = olddict[key]
                        if (code[0][0] + code[1]) in newdict:
                            newdict[code[0][0] + code[1]] += value
                        else:
                            newdict[code[0][0] + code[1]] = value
                        if (code[1] + code[0][1]) in newdict:
                            newdict[code[1] + code[0][1]] += value
                        else:
                            newdict[code[1] + code[0][1]] = value
                        newdict[key] -= value
        olddict = newdict.copy()
        step += 1
    all_freq = {}
    all_freq[firstletter] = 1
    all_freq[lastletter] = 1
    for key in newdict:
        for letter in key:
            if letter in all_freq:
                all_freq[letter] += newdict[key]
            else:
                all_freq[letter] = newdict[key]

    for key in all_freq:
        all_freq[key] /= 2
    maxKey = max(all_freq, key=all_freq.get)
    minKey = min(all_freq, key=all_freq.get)

    print(all_freq[maxKey] - all_freq[minKey])

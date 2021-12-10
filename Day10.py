import statistics

def syntaxError():
    f = open("input day 10.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
    linescores = []
    totalerror = 0
    for line in lines:
        haakjes = []
        x = 0
        while x < len(line):
            if line[x] == '(' or line[x] == '[' or line[x] == '{' or line[x] == '<':
                haakjes.append(line[x])

            if line[x] == ')' or line[x] == ']' or line[x] == '}' or line[x] == '>':
                closechar = line[x]
                if haakjes[-1] != '(' and closechar == ')':
                    totalerror += 3
                    haakjes = []
                    break
                elif haakjes[-1] == '(' and closechar == ')':
                    haakjes.pop()

                elif haakjes[-1] != '[' and closechar == ']':
                    totalerror += 57
                    haakjes = []
                    break
                elif haakjes[-1] == '[' and closechar == ']':
                    haakjes.pop()

                elif haakjes[-1] != '{' and closechar == '}':
                    totalerror += 1197
                    haakjes = []
                    break
                elif haakjes[-1] == '{' and closechar == '}':
                    haakjes.pop()

                elif haakjes[-1] != '<' and closechar == '>':
                    totalerror += 25137
                    haakjes = []
                    break
                elif haakjes[-1] == '<' and closechar == '>':
                    haakjes.pop()
            x += 1

        if len(haakjes) > 0:
            autocomplete = []
            while len(haakjes) > 0:
                if haakjes[-1] == '(':
                    autocomplete.append(')')
                elif haakjes[-1] == '[':
                    autocomplete.append(']')
                elif haakjes[-1] == '{':
                    autocomplete.append('}')
                elif haakjes[-1] == '<':
                    autocomplete.append('>')
                haakjes.pop()
            score = 0
            for char in autocomplete:
                score *= 5
                if char == ')':
                    score += 1
                elif char == ']':
                    score += 2
                elif char == '}':
                    score += 3
                elif char == '>':
                    score += 4
            linescores.append(score)
    print("part 1: ", totalerror)
    print("part 2: ", statistics.median(linescores))
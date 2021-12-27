from collections import defaultdict


def Caves():
    f = open("input day 12.txt", "r")
    lines = f.readlines()
    neighbours = defaultdict(list)
    for line in lines:
        a, b = line.strip().split('-')
        neighbours[a] += [b]
        neighbours[b] += [a]

    def count(part, seen=[], cave='start'):
        if cave == 'end':
            return 1
        if cave in seen:
            if cave == 'start':
                return 0
            if cave.islower():
                if part == 1:
                    return 0
                else:
                    part = 1

        return sum(count(part, seen+[cave], n) for n in neighbours[cave])

    print(count(part=1), count(part=2))
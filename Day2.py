def direction():
    f = open("input day 2.txt", "r")
    lines = f.readlines()
    horizontal = 0
    depth = 0
    for line in lines:
        order = line.split(" ")
        if order[0] == "forward":
            horizontal += int(order[1])
        if order[0] == "down":
            depth += int(order[1])
        if order[0] == "up":
            depth -= int(order[1])
    print(horizontal * depth)

def direction2():
    f = open("input day 2.txt", "r")
    lines = f.readlines()
    horizontal = 0
    depth = 0
    aim = 0
    for line in lines:
        order = line.split(" ")
        if order[0] == "forward":
            horizontal += int(order[1])
            depth += (aim * int(order[1]))
        if order[0] == "down":
            aim += int(order[1])
        if order[0] == "up":
            aim -= int(order[1])
    print(horizontal * depth)
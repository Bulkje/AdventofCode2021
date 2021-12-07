import statistics


def crabsubmarines():
    # f = open("input day 7.txt", "r")
    f = open("test.txt", "r")
    lines = f.readlines()

    locations = []
    for location in lines[0].split(','):
        locations.append(int(location))
    preflocation = int(statistics.median(locations))
    fuel = 0

    for location in locations:
        if preflocation > location:
            fuel += preflocation - location
        if location > preflocation:
            fuel += location - preflocation
    print(fuel)

def crabsubmarines_highfuel():
    f = open("input day 7.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()

    locations = []
    for location in lines[0].split(','):
        locations.append(int(location))
    preflocation = round(sum(locations) / len(locations))
    fuel = 0

    for location in locations:
        if preflocation > location:
            n = preflocation - location
        if location > preflocation:
            n = location - preflocation
        for num in range(0, n + 1, 1):
            fuel = fuel + num

    print(fuel)
    # 368365 too low
    # 99420073 too low
    # 99788438 too high

import statistics


def crabsubmarines():
    f = open("input day 7.txt", "r")
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
    lines = f.readlines()

    locations = []
    for location in lines[0].split(','):
        locations.append(int(location))
    preflocation = []
    #because of rounding shenanigans I have to do this
    preflocation.append(round(sum(locations) / len(locations)) - 1)
    preflocation.append(round(sum(locations) / len(locations)))
    preflocation.append(round(sum(locations) / len(locations)) + 1)

    totalfuel = []
    for ideallocation in preflocation:
        fuel = 0
        for location in locations:
            if ideallocation > location:
                n = ideallocation - location
            if location > ideallocation:
                n = location - ideallocation
            for num in range(0, n + 1, 1):
                fuel = fuel + num
        totalfuel.append(fuel)
    print(min(totalfuel))

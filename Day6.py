def LanternFish(days):
    f = open("input day 6.txt", "r")
    lines = f.readlines()

    fishpopulation = []
    for i in range(9):
        fishpopulation.append(lines[0].count(str(i)))

    i = 0
    print(fishpopulation)
    while i < days:
        newpop = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        day = 1
        while day < len(fishpopulation):
            #shift everything left
            newpop[day - 1] = fishpopulation[day]
            day += 1
        #put the new fish at the back
        newpop[8] = fishpopulation[0]
        #put the mother fish at 7 days away
        newpop[6] += fishpopulation[0]
        fishpopulation = newpop
        i += 1
    print(fishpopulation)
    print(sum(fishpopulation))
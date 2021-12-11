def Octopuslight(steps):
    f = open("input day 11.txt", "r")
    lines = f.readlines()
    numbergrid = []
    for line in lines:
        numberrow = []
        if line[-1] == '\n':
            line = line[:-1]
        for number in line:
            numberrow.append(int(number))
        numbergrid.append(numberrow)
    print(numbergrid)
    step = 0
    while step < steps:
        flashed = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
        newgrid = 'unimplemented'




        step += 1
    #per step
    #make empty 10x10 array 'flashed'
    #increase all values by 1
    #while octopuses.max() > 9
        #check all locations
        #if location >9, check 'flashed' if the octopus flashed already
        #if not, add location to flashed, add 1 to all adjacent locations
        #totalflashes += 1
    #for each location

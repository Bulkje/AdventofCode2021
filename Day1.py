def depths(): # increasing depths
    f = open("input day 1.txt", "r")
    lines = f.readlines()
    i = 1
    depths = []
    increasing = 0
    for line in lines:
        depths.append(int(line))

    while(i < len(lines)):
        if(depths[i] > depths[i - 1]):
            increasing += 1
        i += 1
    print(increasing)
    print("done")

def windowdepths(): # depth measurement window
    f = open("input day 1.txt", "r")
    lines = f.readlines()
    i = 1
    depths = []
    increasing = 0
    for line in lines:
        depths.append(int(line))

    while (i < len(lines) - 2):
        current = depths[i] + depths[i + 1] + depths[i + 2]
        prevdepth = depths[i - 1] + depths[i] + depths[i + 1]
        if current > prevdepth:
            increasing += 1
        i += 1
    print(increasing)
    print("done")
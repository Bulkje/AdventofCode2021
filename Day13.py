import sys
import numpy as np

def folding():
    f = open("input day 13.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    locations = []
    for line in lines:
        if line == '\n':
            break
        locations.append(line[:-1].split(','))
    for location in locations:
        location[0] = int(location[0])
        location[1] = int(location[1])
    print(locations)
    maxX = max([sublist[0] for sublist in locations])
    maxY = max([sublist[1] for sublist in locations])
    print('Max X:', maxX)
    print('Max Y:', maxY)

    grid = np.zeros((maxY + 1, maxX + 1), dtype=int)
    for location in locations:
        grid[location[1], location[0]] = 1
    print(grid)

    instructions = []
    i = lines.index('\n') + 1
    while i < len(lines):
        if lines[i][-1] == '\n':
            lines[i] = lines[i][:-1]
        instruction = lines[i].split(' ')[2].split('=')
        instructions.append(instruction)
        i += 1
    print(instructions)
    count = 0
    for instruction in instructions:
        foldline = int(instruction[1])
        axis = instruction[0]
        if axis == 'y':
            count += 1
            print(count)
            print(np.size(grid, 0))
            if (np.size(grid, 0) + 1) % 2 == 1:
                if foldline + 1 < np.size(grid, 0) / 2:
                    print('deleting')
                    grid = np.delete(grid, np.size(grid, 0) - 1, 0)
                else:
                    row = np.zeros((1, np.size(grid, 1)), dtype=int)
                    grid = np.append(grid, row, axis=0)
            grid = np.delete(grid, foldline, axis=0)
            topArray, bottomArray = np.split(grid, 2)
            #bottomArray = grid[foldline:]
            #topArray = grid[:foldline]
            bottomArray = np.flip(bottomArray, axis=0)
            result = topArray + bottomArray
        if axis == 'x':
            #leftArray = grid[..., :foldline]
            #rightArray = grid[..., foldline + 1:]
            grid = np.delete(grid, foldline, axis=1)
            leftArray, rightArray = np.split(grid, 2, axis=1)
            rightArray = np.flip(rightArray, axis=1)
            result = leftArray + rightArray
        grid = result.copy()
        if instructions.index(instruction) == 0:
            print("Part 1:", (result > 0).sum())
    np.set_printoptions(linewidth=np.nan)
    print(result)
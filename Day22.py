import numpy as np
import re

def Reboot():
    f = open("input day 22.txt", "r")
    #f = open("test.txt", "r")
    #f = open("test2.txt", "r")
    lines = f.readlines()
    Reactor = np.zeros((101, 101, 101), dtype=int)

    for line in lines[:20]:
        numbers = re.sub(r'[^-\d]', " ", line).split(' ')
        Coords = []
        for item in numbers:
            if item != '':
                Coords.append(int(item))

    for line in lines[:20]:
        numbers = re.sub(r'[^-\d]', " ", line).split(' ')
        Coords = []
        for item in numbers:
            if item != '':
                Coords.append(int(item) + 50)

        if line.split(' ')[0] == 'on':
            func = 1
        else:
            func = 0
        cube = np.full((abs(Coords[5] - Coords[4] + 1), abs(Coords[3] - Coords[2] + 1), abs(Coords[1] - Coords[0] + 1)), func, dtype=int)

        pos_x, pos_y, pos_z = Coords[0], Coords[2], Coords[4]  # a 3d offset -> to plonk cube in [position] of Reactor

        z_range1 = slice(max(0, pos_z), max(min(pos_z + cube.shape[0], Reactor.shape[0]), 0))
        y_range1 = slice(max(0, pos_y), max(min(pos_y + cube.shape[1], Reactor.shape[1]), 0))
        x_range1 = slice(max(0, pos_x), max(min(pos_x + cube.shape[2], Reactor.shape[2]), 0))

        z_range2 = slice(max(0, -pos_z), min(-pos_z + Reactor.shape[0], cube.shape[0]))
        y_range2 = slice(max(0, -pos_y), min(-pos_y + Reactor.shape[1], cube.shape[1]))
        x_range2 = slice(max(0, -pos_x), min(-pos_x + Reactor.shape[2], cube.shape[2]))

        Reactor[z_range1, y_range1, x_range1] = cube[z_range2, y_range2, x_range2]
    print(np.sum(Reactor))

def RebootComplete():
    f = open("input day 22.txt", "r")
    steps = []
    for line in f.readlines():
        act, cuboid = line.split()
        cuboid = tuple(map(parse_range, cuboid.split(',')))
        steps.append((act, cuboid))

    print(sum(unique_cuboid_volume(cuboid, steps[idx + 1:])
               for idx, (act, cuboid) in enumerate(steps)
               if act == 'on'))

def parse_range(s):
    c0, c1 = s[2:].split('..')
    return range(int(c0), int(c1)+1)

def unique_cuboid_volume(cuboid, rest):
    conflicts = []

    for act, other in rest:
        intersection = cuboid_intersect(cuboid, other)
        if cuboid_volume(intersection) == 0:
            continue

        conflicts.append((act, intersection))

    volume = cuboid_volume(cuboid)
    volume -= sum(unique_cuboid_volume(conflict, conflicts[idx+1:])
                  for idx, (_, conflict) in enumerate(conflicts))

    return volume

def cuboid_intersect(base, other):
    return tuple(range(max(b.start, o.start),
                       min(b.stop, o.stop))
                 for b, o in zip(base, other))

def cuboid_volume(cuboid):
    x, y, z = tuple(map(len, cuboid))
    return x * y * z
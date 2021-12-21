import numpy as np
from collections import namedtuple, deque
import heapq
from collections import defaultdict
from math import inf as INF

def lowerNeighbor():
    f = open("input day 15.txt", "r")
    lines = f.readlines()
    numbergrid = []
    for line in lines:
        numberrow = []
        if line[-1] == '\n':
            line = line[:-1]
        for number in line:
            numberrow.append(int(number))
        numbergrid.append(numberrow)
    numbergrid = np.asarray(numbergrid)
    print(dijkstra(numbergrid))

def biggermap():
    f = open("input day 15.txt", "r")
    #f = open("test.txt", "r")
    lines = f.readlines()
    numbergrid = []
    for line in lines:
        numberrow = []
        if line[-1] == '\n':
            line = line[:-1]
        for number in line:
            numberrow.append(int(number))
        numbergrid.append(numberrow)
    numbergrid = np.asarray(numbergrid)
    xLen = np.size(numbergrid[1])
    yLen = np.shape(numbergrid)[0]

    newTile1 = numbergrid + np.ones((yLen, xLen), dtype=int)
    newTile2 = numbergrid + np.full((yLen, xLen), 2, dtype=int)
    newTile3 = numbergrid + np.full((yLen, xLen), 3, dtype=int)
    newTile4 = numbergrid + np.full((yLen, xLen), 4, dtype=int)

    for x in range(xLen):
        for y in range(yLen):
            if newTile1[y, x] > 9:
                newTile1[y, x] -= 9
            if newTile2[y, x] > 9:
                newTile2[y, x] -= 9
            if newTile3[y, x] > 9:
                newTile3[y, x] -= 9
            if newTile4[y, x] > 9:
                newTile4[y, x] -= 9
    bigTile = np.concatenate((numbergrid, newTile1, newTile2, newTile3, newTile4), axis=1)

    mask = np.ones((np.shape(bigTile)[0], np.size(bigTile[1])), dtype=int)
    bigRow = bigTile + mask
    for x in range(np.size(bigRow[1])):
        for y in range(np.shape(bigTile)[0]):
            if bigRow[y, x] > 9:
                bigRow[y, x] -= 9
    bigTile = np.concatenate((bigTile, bigRow))

    mask = np.full((np.shape(bigTile)[0], np.size(bigTile[1])), 2, dtype=int)
    bigRow = bigTile + mask
    for x in range(np.size(bigRow[1])):
        for y in range(np.shape(bigTile)[0]):
            if bigRow[y, x] > 9:
                bigRow[y, x] -= 9
    bigTile = np.concatenate((bigTile, bigRow))

    bigRow = bigTile[3 * yLen:]
    mask = np.full((np.shape(bigRow)[0], np.size(bigRow[1])), 1, dtype=int)
    bigRow = bigRow + mask
    for x in range(np.size(bigRow[1])):
        for y in range(np.shape(bigRow)[0]):
            if bigRow[y, x] > 9:
                bigRow[y, x] -= 9

    bigTile = np.append(bigTile, bigRow, axis=0)
    print(dijkstra(bigTile))

def dijkstra(grid):
    yLen, xLen = np.shape(grid)
    source = (0, 0)
    destination = (yLen - 1, xLen - 1)

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = [(0, source)]
    mindist = defaultdict(lambda: INF, {source: 0})
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)

        # If we got to the destination, we have our answer.
        if node == destination:
            return dist

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue

        # Mark the node as visited.
        visited.add(node)
        y, x = node

        # For each unvisited neighbor of this node...
        for neighbor in directneighbor(y, x, yLen, xLen):
            if neighbor in visited:
                continue

            # Calculate the total distance from the source to this neighbor
            # passing through this node.
            ny, nx = neighbor
            newdist = dist + grid[ny, nx]

            # If the new distance is lower than the minimum distance we have to
            # reach this neighbor, then update its minimum distance and add it
            # to the queue, as we found a "better" path to it.
            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))

    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    return INF

def directneighbor(y, x, yLen, xLen):
    neighbors = []
    if y > 0:
        neighbors.append((y - 1, x))
    if x > 0:
        neighbors.append((y, x - 1))
    if x < xLen - 1:
        neighbors.append((y, x + 1))
    if y < yLen - 1:
        neighbors.append((y + 1, x))
    return neighbors

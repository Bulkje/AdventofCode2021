import numpy as np
from collections import namedtuple, deque
from pprint import pprint as pp

def lowerNeighbor():
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
    yLen = np.size(numbergrid[0])
    paths = []
    print(xLen, yLen)
    for x in range(xLen):
        for y in range(yLen):
            if y > 0:
                #paths.append([str([y, x]), str([y - 1, x]), numbergrid[x, y - 1]])
                paths.append([str([x, y]), str([x, y - 1]), numbergrid[x, y - 1]])
            if x > 0:
                #paths.append([str([y, x]), str([y, x - 1]), numbergrid[x - 1, y]])
                paths.append([str([x, y]), str([x - 1, y]), numbergrid[x - 1, y]])
            if x < xLen - 1:
                #paths.append([str([y, x]), str([y, x + 1]), numbergrid[x + 1, y]])
                paths.append([str([x, y]), str([x + 1, y]), numbergrid[x + 1, y]])
            if y < yLen - 1:
                #paths.append([str([y, x]), str([y + 1, x]), numbergrid[x, y + 1]])
                paths.append([str([x, y]), str([x, y + 1]), numbergrid[x, y + 1]])
    print(numbergrid)
    print(numbergrid[3, 1])
    #print(paths)
    print('Edges: ', len(paths))

    graph = Graph([(paths[i][0], paths[i][1], paths[i][2]) for i in range(len(paths))])
    #pp(graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1])))
    route = graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1]), numbergrid)
    dist = numbergrid[0, 0] * -1
    for location in route:
        location = location[1:-1]
        x = int(location.split(', ')[0])
        y = int(location.split(', ')[1])
        #print(x, y, numbergrid[y, x])
        dist += numbergrid[y, x]
    print(route)
    print(dist)

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

def biggermap():
    f = open("input day 15.txt", "r")
    f = open("test.txt", "r")
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
    yLen = np.size(numbergrid[0])

    mask = np.ones((yLen, xLen), dtype=int)

    newTile1 = numbergrid + mask
    newTile2 = numbergrid + mask * 2
    newTile3 = numbergrid + mask * 3
    newTile4 = numbergrid + mask * 4

    for x in range(xLen):
        for y in range(yLen):
            if newTile1[y, x] > 9:
                newTile1[y, x] -= 8
            if newTile2[y, x] > 9:
                newTile2[y, x] -= 8
            if newTile3[y, x] > 9:
                newTile3[y, x] -= 8
            if newTile4[y, x] > 9:
                newTile4[y, x] -= 8
    np.set_printoptions(linewidth=np.nan)
    #something wrong while adding mask

    bigTile = np.concatenate((numbergrid, newTile1, newTile2, newTile3, newTile4), axis=1)

    mask = np.ones((np.shape(bigTile)[0], np.size(bigTile[1])), dtype=int)
    bigRow = bigTile + mask
    for x in range(np.size(bigRow[1])):
        for y in range(np.shape(bigTile)[0]):
            if bigRow[y, x] > 9:
                bigRow[y, x] = 1
    bigTile = np.concatenate((bigTile, bigRow))

    print(bigTile)

    mask = np.full((np.shape(bigTile)[0], np.size(bigTile[1])), 2, dtype=int)
    bigRow = bigTile + mask
    for x in range(np.size(bigRow[1])):
        for y in range(np.shape(bigTile)[0]):
            if bigRow[y, x] > 9:
                bigRow[y, x] = 1
    bigTile = np.concatenate((bigTile, bigRow))
    print(bigTile)
    print(np.shape(bigTile))
    print('lmao')

    bigRow = bigTile[30:]
    print(bigRow)
    return



    paths = []
    print(xLen, yLen)
    for x in range(xLen):
        for y in range(yLen):
            if y > 0:
                # paths.append([str([y, x]), str([y - 1, x]), numbergrid[x, y - 1]])
                paths.append([str([x, y]), str([x, y - 1]), numbergrid[x, y - 1]])
            if x > 0:
                # paths.append([str([y, x]), str([y, x - 1]), numbergrid[x - 1, y]])
                paths.append([str([x, y]), str([x - 1, y]), numbergrid[x - 1, y]])
            if x < xLen - 1:
                # paths.append([str([y, x]), str([y, x + 1]), numbergrid[x + 1, y]])
                paths.append([str([x, y]), str([x + 1, y]), numbergrid[x + 1, y]])
            if y < yLen - 1:
                # paths.append([str([y, x]), str([y + 1, x]), numbergrid[x, y + 1]])
                paths.append([str([x, y]), str([x, y + 1]), numbergrid[x, y + 1]])
    print(numbergrid)
    print(numbergrid[3, 1])
    # print(paths)
    print('Edges: ', len(paths))

    graph = Graph([(paths[i][0], paths[i][1], paths[i][2]) for i in range(len(paths))])
    # pp(graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1])))
    route = graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1]), numbergrid)
    dist = numbergrid[0, 0] * -1
    for location in route:
        location = location[1:-1]
        x = int(location.split(', ')[0])
        y = int(location.split(', ')[1])
        # print(x, y, numbergrid[y, x])
        dist += numbergrid[y, x]
    print(route)
    print(dist)


inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest, grid):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end))
            neighbours[end].add((start))

        # pp(neighbours)

        while q:
            #pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break

            for v in neighbours[u]:
                location = u[1:-1]
                endX = int(location.split(', ')[0])
                endY = int(location.split(', ')[1])
                alt = dist[u] + grid[endY, endX]
                if alt < dist[v]:  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        #pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
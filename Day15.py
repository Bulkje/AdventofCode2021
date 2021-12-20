import numpy as np
from collections import namedtuple, deque
from pprint import pprint as pp

def lowerNeighbor():
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
    paths = []
    print(xLen, yLen)
    for x in range(xLen):
        for y in range(yLen):
            #need to make 9 separate cases to be sure nothing is duplicated
            if y > 0:
                paths.append([str([y, x]), str([y - 1, x]), numbergrid[x, y - 1]])
            if x > 0:
                paths.append([str([y, x]), str([y, x - 1]), numbergrid[x - 1, y]])
            if x < xLen - 1:
                paths.append([str([y, x]), str([y, x + 1]), numbergrid[x + 1, y]])
            if y < yLen - 1:
                paths.append([str([y, x]), str([y + 1, x]), numbergrid[x, y + 1]])
    print(numbergrid)
    print(paths)
    print('Edges: ', len(paths))

    graph = Graph([(paths[i][0], paths[i][1], paths[i][2]) for i in range(len(paths))])
    #pp(graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1])))
    route = graph.dijkstra('[0, 0]', str([xLen - 1, yLen - 1]))
    dist = numbergrid[0, 0] * -1
    for location in route:
        location = location[1:-1]
        x = int(location.split(', ')[0])
        y = int(location.split(', ')[1])
        #print(x, y, numbergrid[y, x])
        dist += numbergrid[y, x]
    print(route)
    print(dist)

#need to add paths differently, going to and from location is different values
#438 too high
#not 441
#[0, 1] --> 444
#[1, 0] --> 442


inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        # print(dir(self.edges[0]))
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
            neighbours[end].add((start, cost))

        # pp(neighbours)

        while q:
            # pp(q)
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        # pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
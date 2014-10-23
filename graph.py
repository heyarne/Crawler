
# Graph implementation taken from
# http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def add_vertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def get_vertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def add_edge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def get_vertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

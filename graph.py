# Graph implementation taken from
# http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html


class PageNode:

    def __init__(self, key):
        self.id = key
        self.out_links = []
        self.in_links = []

    def add_out_link(self, neighbor):
        self.out_links.append(neighbor)

    def add_in_link(self, neighbor):
        self.in_links.append(neighbor)

    def links_to(self, target):
        self.add_out_link(target)
        target.add_in_link(self)

    def __str__(self):
        return str(self.id) + ' is linked to by: ' + str([x.id for x in self.out_links])

    def get_connections(self):
        return self.out_links

    def get_id(self):
        return self.id


class Graph:

    def __init__(self):
        self.node_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = PageNode(key)
        self.node_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.node_list:
            return self.node_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.node_list

    def add_edge(self, f, t):
        if f not in self.node_list:
            self.add_vertex(f)
        if t not in self.node_list:
            self.add_vertex(t)

        self.node_list[f].links_to(self.node_list[t])

    def get_vertices(self):
        return self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())

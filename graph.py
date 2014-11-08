# Graph implementation taken from
# http://interactivepython.org/courselib/static/pythonds/Graphs/graphintro.html


class PageNode:

    def __init__(self, key):
        self.id = key
        self.out_links = set()
        self.in_links = set()

    def add_out_link(self, neighbor):
        self.out_links.add(neighbor)

    def add_in_link(self, neighbor):
        self.in_links.add(neighbor)

    def links_to(self, target):
        self.add_out_link(target)
        target.add_in_link(self)

    def __str__(self):
        return str(self.short_id()) + ': ' + str([x.short_id() for x in self.out_links])

    def get_id(self):
        return self.id

    def short_id(self):
        base_name = self.id[self.id.rindex('/') + 1:]
        without_ending = base_name[:base_name.rindex('.')]

        return without_ending


class Graph:

    def __init__(self):
        self.node_list = {}
        self.num_nodes = 0

    def add_node(self, key):
        self.num_nodes = self.num_nodes + 1
        new_node = PageNode(key)
        self.node_list[key] = new_node
        return new_node

    def get_node(self, n):
        if n in self.node_list:
            return self.node_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.node_list

    def add_edge(self, f, t):
        if f not in self.node_list:
            self.add_node(f)
        if t not in self.node_list:
            self.add_node(t)

        self.node_list[f].links_to(self.node_list[t])

    def get_node_ids(self):
        return self.node_list.keys()

    def __iter__(self):
        return iter(self.node_list.values())

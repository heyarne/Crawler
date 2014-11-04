import copy


class Ranker():

    """Implementation of the graph-based ranking algorithm"""

    def __init__(self, graph, teleportation_rate=0.1):
        self.teleportation_rate = teleportation_rate
        self.curb_factor = 1 - teleportation_rate

        # leave the original graph untouched
        self.graph = copy.deepcopy(graph)

    def calculate_rank(delta=0):
        all_nodes = self.graph.get_vertices()
        num_nodes = len(all_nodes)
        with_links = []
        without_links = []

        for node in all_nodes:
            links = node.get_connections()
            for link in links:
                link.last_rank = 1 / num_nodes

            if node.get_connections():
                with_links.append(node)
            else:
                without_links.append(node)

        # the actual calculation starts here
        last_distance = 1
        while not self.should_abort(delta):
            rank = self.teleportation_rate / num_nodes
            for node in with_links:
                pass

    def should_abort(delta):
        for node in self.graph.get_vertices():
            if (abs(node.last_rank - node.rank) > delta):
                return False

        return True

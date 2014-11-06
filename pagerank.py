import copy


class Ranker():

    """Implementation of the graph-based ranking algorithm"""

    def __init__(self, graph, curb_factor=0.9):
        self.curb_factor = curb_factor
        self.teleportation_rate = 1 - curb_factor

        # leave the original graph untouched
        self.graph = copy.deepcopy(graph)

    def calculate_rank(self, delta=0):
        without_in_links = []

        # cache this as we'll reuse it often
        num_nodes = len(self.graph.get_node_ids())

        # in the first run we're just giving an initial rank / last rank to kick
        # off the other algorithm and order the pages into different lists to
        # make later iteration easier

        for node in self.graph:
            node.last_rank = float("inf")
            node.rank = 1 / num_nodes

            if not node.in_links:
                without_in_links.append(node)

        # the actual calculation starts here
        while not self.should_abort(delta):
            for node in self.graph:
                rank = 0.0
                # first summand of formula
                for link in node.in_links:
                    rank += link.rank / len(link.out_links)
                # second summand
                for link in without_in_links:
                    rank += link.rank / num_nodes

                rank *= self.curb_factor
                rank += self.teleportation_rate / num_nodes

                node.next_rank = rank

            for node in self.graph:
                node.last_rank = node.rank
                node.rank = node.next_rank
                node.next_rank = None

    def should_abort(self, delta):
        for node in self.graph:
            if (abs(node.last_rank - node.rank) > delta):
                return False

        return True

    def __str__(self):
        long_str = ""

        for node in self.graph:
            long_str += str(node.short_id() + " has the rank " + str(node.rank)) + "\n"

        return long_str

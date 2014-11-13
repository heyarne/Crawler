import copy


class Ranker():

    """Implementation of the graph-based ranking algorithm"""

    def __init__(self, graph):
        # leave the original graph untouched
        self.graph = copy.deepcopy(graph)

    def calculate_rank(self, curb_factor=0.9, delta=0.04):
        without_out_links = []

        # cache this as we'll reuse it often
        num_nodes = len(self.graph.get_node_ids())
        teleportation_rate = 1 - curb_factor

        # in the first run we're just giving an initial rank / last rank to kick
        # off the other algorithm and order the pages into different lists to
        # make later iteration easier

        for node in self.graph:
            node.last_rank = float("inf")
            node.rank = 1 / num_nodes
            if not node.out_links:
                without_out_links.append(node)

        # the actual calculation starts here
        while not self.should_abort(delta):
            print (self)

            for node in self.graph:
                rank = 0.0
                # first summand of formula
                for link in node.in_links:
                    rank += link.rank / len(link.out_links)
                # second summand
                for link in without_out_links:
                    rank += link.rank / num_nodes

                rank *= curb_factor
                rank += teleportation_rate / num_nodes

                node.next_rank = rank

            for node in self.graph:
                node.last_rank = node.rank
                node.rank = node.next_rank


    def should_abort(self, delta):
        for node in self.graph:
            if (abs(node.last_rank - node.rank) > delta):
                return False

        return True

    def __str__(self):
        long_str = ""

        for node in self.graph:
            long_str += node.short_id() + " has the rank " + str(node.rank) + "\n"

        return long_str

class Frontier:

    def __init__(self, visit_queue = []):
        self.visited = []
        self.to_visit = visit_queue

    def add_url(self, page_url):
        self.to_visit.append(page_url)

    def get_next_url(self):
        # pop in python returns the last element of the list.
        # to make it easier understandable we return the first one
        next_url = self.to_visit[0]
        self.to_visit = self.to_visit[1:]

        self.visited.append(next_url)
        return next_url

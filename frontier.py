class Frontier:

    """Really simple frontier implementation"""

    def __init__(self, visit_queue=[]):
        self.visited = []
        self.to_visit = visit_queue

    def add_url(self, page_url):
        if page_url not in self.visited and page_url not in self.to_visit:
            self.to_visit.append(page_url)

    def add_urls(self, page_urls):
        for url in page_urls:
            self.add_url(url)

    def get_next_url(self):
        if self.to_visit:
            # pop in python returns the last element of the list.
            # to make it easier understandable we return the first one
            next_url = self.to_visit[0]
            self.to_visit = self.to_visit[1:]

            self.visited.append(next_url)
            return next_url

    def __iter__(self):
        while self.to_visit:
            # pop in python returns the last element of the list.
            # to make it easier understandable we return the first one
            next_url = self.to_visit[0]
            self.to_visit = self.to_visit[1:]

            self.visited.append(next_url)
            yield next_url

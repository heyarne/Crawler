from frontier import Frontier
from parser import Parser
from graph import Graph
from pagerank import Ranker

frontier = Frontier([
    'http://mysql12.f4.htw-berlin.de/crawl/d01.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d06.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d08.html'
])
parser = Parser()
web_graph = Graph()

for url in frontier:
    # get all links on page
    links_on_page = parser.getLinks(url)

    # build our webgraph
    for out_link in links_on_page:
        web_graph.add_edge(url, out_link)

    # hand links to the frontier to make sure they are all crawled
    frontier.add_urls(links_on_page)

for node in web_graph:
    print(node)

ranker = Ranker(web_graph)
ranker.calculate_rank(curb_factor=0.95, delta=0.04)
print(ranker)

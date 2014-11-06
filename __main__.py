from frontier import Frontier
from parser import Parser
from graph import Graph

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
    web_graph.add_node(url)
    for link in links_on_page:
        # third param is "weight", which is arbitrary for now
        web_graph.add_edge(url, link)

    # hand links to the frontier to make sure they are all crawled
    frontier.add_urls(links_on_page)

for node in web_graph:
    print(node)

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
    # get outgoing links for the graph and content for tokenization
    body, links_on_page = parser.parse(url)

    # build our webgraph
    node = web_graph.get_node(url)
    if node is None:
        node = web_graph.add_node(url)

    for out_link in links_on_page:
        web_graph.add_edge(url, out_link)

    # attach the parsing data to the node for our tokenizer / indexer
    node.body = body

    # hand links to the frontier to make sure they are all crawled
    frontier.add_urls(links_on_page)

for node in web_graph:
    print(node)

print()

ranker = Ranker(web_graph)
ranker.calculate_rank(curb_factor=0.95, delta=0.04)
print(ranker)

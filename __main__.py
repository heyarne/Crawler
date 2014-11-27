from frontier import Frontier
from parser import Parser
from graph import Graph
from pagerank import Ranker
from indexer import Indexer
from scorer import Scorer

frontier = Frontier([
    'http://mysql12.f4.htw-berlin.de/crawl/d01.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d06.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d08.html'
])
parser = Parser()
indexer = Indexer()
web_graph = Graph()

for url in frontier:
    # get outgoing links for the graph and content for tokenization
    body, links_on_page = parser.parse(url)

    # add document to indexer
    indexer.add_document(url, body)

    # build our webgraph
    node = web_graph.get_node(url)
    if node is None:
        node = web_graph.add_node(url)

    for out_link in links_on_page:
        web_graph.add_edge(url, out_link)

    # hand links to the frontier to make sure they are all crawled
    frontier.add_urls(links_on_page)

# for node in web_graph:
#     print(node)
#
# print()

ranker = Ranker(web_graph)
ranker.calculate_rank(curb_factor=0.95, delta=0.04)
print(ranker)

#
# for k in indexer.index:
#     print(k, indexer.index[k])
# print(indexer.find('supervised'))

# query = ["index"]
scorer = Scorer(indexer, ranker)
queries = [['tokens'], ['index'], ['classification'], ['tokens', 'classification']]
for query in queries:
    print(str(query) + ':')
    print('non-weighted:')
    score_list = scorer.cosine_score(query) # [(doc, score), (doc2, score2), ...]
    for tupel in score_list:
        print(tupel)
    print("________________________________")
    print('weighted with pagerank:')
    score_list2 = scorer.weighted_score(query) #[(doc, score), (doc2, score2),...]
    for tupel in score_list2:
        print(tupel)
    print("________________________________")

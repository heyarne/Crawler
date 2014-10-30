from frontier import Frontier
from parser import Parser

# frontier = Frontier(['http://google.de', 'http://blog.fefe.de', 'http://facebook.com'])
frontier = Frontier(['http://mysql12.f4.htw-berlin.de/crawl/d01.html',
    'http://mysql12.f4.htw-berlin.de/crawl/d06.html', 'http://mysql12.f4.htw-berlin.de/crawl/d08.html'])
parser = Parser()

added_url = False
for url in frontier:
    print(url)
    print parser.getLinks(url)

    frontier.add_urls(parser.getLinks(url))

    # if not added_url:
    #     frontier.add_url('http://arne.in')
    #     added_url = True

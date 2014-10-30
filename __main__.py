from frontier import Frontier

frontier = Frontier(['http://google.de', 'http://blog.fefe.de', 'http://facebook.com'])

added_url = False
for url in frontier:
    print(url)
    if not added_url:
        frontier.add_url('http://arne.in')
        added_url = True

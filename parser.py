from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

class Parser():
    def getLinks(self, url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())

        list = []

        for anchor in soup.find_all('a'):
            link = anchor.get('href')
            list.append(urljoin(url, link))
        return list

# parser = Parser()
# print parser.getLinks('http://mysql12.f4.htw-berlin.de/crawl/d01.html')

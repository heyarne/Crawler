from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request as urllib2

class Parser():
    def getLinks(self, url):
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read())

        list = []

        for anchor in soup.find_all('a'):
            link = anchor.get('href')
            list.append(urljoin(url, link))
        return list

# parser = Parser()
# print parser.getLinks('http://mysql12.f4.htw-berlin.de/crawl/d01.html')

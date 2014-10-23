import urlparse
import urllib2
from bs4 import BeautifulSoup

class Parser():
    def getLinks(self, url):
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response.read())

        list = []

        for link in soup.find_all('a'):
            list.append(link.get('href'))
        return list

# parser = Parser()
# print parser.getLinks('http://mysql12.f4.htw-berlin.de/crawl/d01.html')

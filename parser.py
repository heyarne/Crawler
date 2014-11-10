from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

class Parser():
    def parse(self, url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())

        document_text = soup.get_text()
        links = []
        for anchor in soup.find_all('a'):
            link = anchor.get('href')
            links.append(urljoin(url, link))

        return document_text, links

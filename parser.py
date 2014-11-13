from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

class Parser():
    def parse(self, url):
        response = urlopen(url)
        soup = BeautifulSoup(response.read())

        document_text = soup.get_text()
        links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]

        return document_text, links

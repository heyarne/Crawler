import re

class Indexer():
    def __init__(self):
        self.index = {}
        self.stopwords = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08',
            'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do'
            'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
            'that', 'the', 'this', 'to', 'we']

    def add_document(self, docname, text):
        text = text.lower()
        for word in re.findall('\w+', text):
            if word not in self.stopwords:
                if (word not in self.index):
                    self.index[word] = {docname: 1}
                else:
                    if (docname not in self.index[word]):
                        self.index[word][docname] = 1
                    else:
                        self.index[word][docname] = self.index[word][docname] + 1
            # print(self.index)

    def find(self, word):
        word = word.lower()
        if word in self.index:
            return self.index[word]

from math import log10

class Scorer():
    def __init__(self, indexer):
        self.indexer = indexer

    def df(self, term):
        """
        Number of documents that contain a term
        """
        return len(self.indexer.find(term).keys())

    def idf(self, term):
        """
        Inverse document frequency; a measure of importance for a term
        """
        return log10(self.indexer.doc_count / self.df(term))

    def tf(self, term, doc):
        """
        Amount one term occurs in a specific document
        """
        return self.indexer.find(term).get(doc, 0)

    def tfidf(self, term, doc):
        """
        Scores a document for a term; terms that occur rarely get a higher score,
        documents containing a term more frequently as well
        """
        return self.idf(term) * self.tf(term, doc)

    def calculate_weight(self):
        weight_map = {}

        for term in self.indexer.index:
            weight_map[term] = {}
            for doc in self.indexer.find(term):
                weight_map[term][doc] = self.tfidf(term, doc)

        return weight_map

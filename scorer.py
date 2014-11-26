from math import log10
import operator

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
        Term frequency; how often one term occurs in a specific document
        """
        return self.indexer.find(term).get(doc, 0)

    def tfidf(self, term, doc):
        """
        Scores a document for a term; terms that occur rarely get a higher score,
        documents containing a term more frequently as well
        """
        return self.idf(term) * self.tf(term, doc)

    def term_weight(self, tf, df):
        return (1 + log10(tf)) * log10(self.indexer.doc_count / df)

    def calculate_weight_list(self):
        weight_list = {}

        for term in self.indexer.index:
            weight_list[term] = {}
            for doc in self.indexer.find(term):
                weight_list[term][doc] = self.tfidf(term, doc)

        return weight_list

    def cosine_score(self, query):
        scores = {}
        length = {}

        weight_list = self.calculate_weight_list()

        for query_term in query:
            # calculate w t,q
            wtq = self.term_weight(1, len(weight_list[query_term]))

            for word in weight_list:
                for doc in weight_list[word]:
                    term_weight_doc = weight_list[word][doc]

                    wtd = self.term_weight(term_weight_doc, len(weight_list[query_term]))
                    scores[doc] = scores.get(doc, 0) + wtq * wtd

        # adjust length
        for doc in scores:
            if self.indexer.doc_lengths.get(doc):
                scores[doc] /= self.indexer.doc_lengths.get(doc)
            else:
                scores[doc] = 0

        sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
        return sorted_scores

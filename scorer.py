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
        Amount one term occurs in a specific document
        """
        return self.indexer.find(term).get(doc, 0)

    def tfidf(self, term, doc):
        """
        Scores a document for a term; terms that occur rarely get a higher score,
        documents containing a term more frequently as well
        """
        return self.idf(term) * self.tf(term, doc)

    def calculate_postings_list(self):
        postings_list = {}

        for term in self.indexer.index:
            postings_list[term] = {}
            for doc in self.indexer.find(term):
                postings_list[term][doc] = self.tfidf(term, doc)

        return postings_list

    def cosine_score(self, query):
        scores = {}
        length = {}

        postings_list = self.calculate_postings_list()

        for term in query:
            for term in postings_list:
                for doc in term:
                    tf_query = query.count(term)
                    tfidf_query = log10(len(query)) * tf_query
                    scores[doc] = scores.get(doc, 0) + postings_list.get(term, {}).get(doc, 0) + tf_query

        for doc in scores:
            if self.indexer.doc_lengths.get(doc):
                scores[doc] /= self.indexer.doc_lengths.get(doc)
            else:
                scores[doc] = 0

        print(scores)
        #sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
        #print(sorted_scores)

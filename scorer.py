from math import log10, sqrt
import operator

class Scorer():
    def __init__(self, indexer):
        self.indexer = indexer
        self.flipped_index = self.flip_index(self.indexer.index)

    def term_weight(self, tf, df):
        """
        Calculates the tfidf based on term and document frequency
        """
        return (1 + log10(tf)) * log10(self.indexer.doc_count / df)

    def flip_index(self, index):
        """
        Our index maps each term to a document with a frequency; we need it vice
        versa, so we flip it
        """
        flipped_index = {}
        for term in self.indexer.index:
            for document in self.indexer.index[term]:
                # set up a list for each document if there is none yet
                flipped_index[document] = flipped_index.get(document, {})
                # put the each term and it's frequency in this document into the list
                flipped_index[document][term] = self.indexer.index[term][document]

        return flipped_index

    def vector_length(self, terms, document=None):
        length = 0
        for term in terms:
            posting_list = self.indexer.find(term)
            # the term frequency is mapped to each document; however, when we
            # want to get the vector length of our query, it's different
            tf = posting_list.get(document, 1)
            df = len(posting_list.keys())

            length += self.term_weight(tf, df) ** 2
        return sqrt(length)

    def cosine_score(self, query):
        print(str(query) + ':')

        scores = {}
        lengths = {}

        # calculate the length of each document
        for document, terms in self.flipped_index.items():
            lengths[document] = self.vector_length(terms, document)

        for query_term in query:
            # get all documents in our index for our query term
            posting_list = self.indexer.find(query_term)

            df = len(posting_list.keys())
            wtq = self.term_weight(query.count(query_term), df)

            for document, tf in self.indexer.find(query_term).items():
                wtd = self.term_weight(tf, df)
                scores[document] = scores.get(document, 0) + wtd * wtq

        for doc in scores:
            scores[doc] = scores[doc] / lengths[doc] / self.vector_length(query)

        ascending_scores = sorted(scores.items(), key=operator.itemgetter(1))
        return list(reversed(ascending_scores))

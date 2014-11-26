from math import log10, sqrt
import operator

class Scorer():
    def __init__(self, indexer):
        self.indexer = indexer

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

    def vector_length(self, terms, document):
        length = 0
        for term in terms:
            posting_list = self.indexer.find(term)
            # the term frequency is mapped to each document; however, when we
            # want to get the vector length of our query, it's different
            tf = posting_list.get(document, document.count(term))
            df = len(posting_list.keys())

            length += self.term_weight(tf, df) ** 2
        return sqrt(length)

    def cosine_score(self, query):
        flipped_index = self.flip_index(self.indexer.index)
        scores = {}
        lengths = {}

        # calculate the length of each document
        for document, terms in flipped_index.items():
            lengths[document] = self.vector_length(terms, document)

        print(lengths)

        for query_term in query:
            posting_list = self.indexer.find(query_term)

            # calculate w t,q
            wtq = self.term_weight(1, len(weight_list[query_term]))

            # Go over every weighted term
            for word in weight_list:
                # Go over every document that contains the weighted term
                for doc in weight_list[word]:
                    # Read the weight of the term in that specific doc from the list
                    term_weight_doc = weight_list[word][doc]

                    # Use this to calculate wtd
                    wtd = self.term_weight(term_weight_doc, len(weight_list[query_term]))

                    scores[doc] = scores.get(doc, 0) + wtq * wtd

        # adjust length
        # for doc in scores:
        #     if self.indexer.doc_lengths.get(doc):
        #         scores[doc] /= self.indexer.doc_lengths.get(doc)
        #     else:
        #         scores[doc] = 0

        sorted_scores = sorted(scores.items(), key=operator.itemgetter(1))
        return sorted_scores

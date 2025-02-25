from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_document(self, doc_id, text):
        for word in text.split():
            self.index[word].add(doc_id)

    def search(self, word):
        return self.index.get(word, set())

index = InvertedIndex()
index.add_document(1, "estrutura de dados e algoritmos")
index.add_document(2, "dados são fundamentais para machine learning")
print(index.search("dados"))

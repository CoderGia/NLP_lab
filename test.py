from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


stemmer = PorterStemmer()
text = "on the other hand takes into consideration the morphological analysis of the words"

text = word_tokenize(text)
print(text)

for t in text:
    print(stemmer.stem(t))

# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# ps = PorterStemmer()
# example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
# for w in example_words:
#     print(ps.stem(w))

Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["London Paris London","Paris Paris London"]
cv = CountVectorizer()

count_matrix = cv.fit_transform(text)

#print count_matrix.toarray()
similarity_scores = cosine_similarity(count_matrix)

print similarity_scores

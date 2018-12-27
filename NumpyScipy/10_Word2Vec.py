import numpy as np
import matplotlib.pylab as plt

# Word2Vec
# Word2vec is a two-layer neural net that processes text.
# Its input is a text corpus and its output is a set of vectors: feature vectors for words in that corpus.
# While Word2vec is not a deep neural network, it turns text into a numerical form that deep nets can understand.

# The purpose and usefulness of Word2vec is to group the vectors of similar words together in vectorspace.
# Word2vec creates vectors that are distributed numerical representations of word features, features such as the context of individual words.

#Given enough data, usage and contexts, Word2vec can make highly accurate guesses about a word’s meaning based on past appearances.
# Those guesses can be used to establish a word’s association with other words
# (e.g. “man” is to “boy” what “woman” is to “girl”),
# or cluster documents and classify them by topic.

# DD = CC + (AA - BB) 를 표현한 것

a = np.array([3,4])
b = np.array([4,3])
c = a+b
plt.annotate('',a,(2,2),arrowprops=dict(facecolor='blue',ls='dashed'))
plt.annotate('',(5,5),b,arrowprops=dict(facecolor='blue',ls='dashed'))

plt.plot(0,0,'go',ms=15)
plt.plot(2,2,'bo',ms=20)
plt.plot(a[0],a[1],'ko',ms=17)
plt.plot(b[0],b[1],'yo',ms=12)
plt.plot(c[0],c[1],'ro',ms=12)

plt.grid(True)
plt.show()
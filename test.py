from gensim.models.keyedvectors import KeyedVectors

print("Loading word2vec...")
word_vectors = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
# dog = word_vectors['man']
x = word_vectors.similarity('woman', 'man')
print(x)

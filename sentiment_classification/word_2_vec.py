from gensim.models.word2vec import Word2Vec
import string 
import numpy as np 
from nltk.corpus import stopwords 
from nltk.stem.snowball import SnowballStemmer 

def build_word2vec_vec(sentences,remove_stopwords = False, use_stemmer = True):
	# input sentences are string list. each string is a preprocessed document. 
	#corpus = [setence.split() for setence in sentences]

	stop = stopwords.words('english')
	#print stop
	# delete punctuation 
	delset = string.punctuation
	new_corpus = []
	for z in sentences:
		item = z.translate(None,delset)
		if remove_stopwords:
			se = [i for i in item.replace("\n",'').split() if i not in stop]
		else:
			se = item.replace("\n",'').split()
		if use_stemmer:
			stemmer = SnowballStemmer("english")
			se = [stemmer.stem(i) for i in se]

		new_corpus.append(se)

	#print len(new_corpus[0])
	#print new_corpus[1]
	return new_corpus 

'''
build word vector for training set by using the average value of 
all word vectors in the review, then scale
'''

def buildWordVector(w2v_model,text,size):
	vec = np.zeros(size).reshape((1,size))
	count = 0
	for word in text:
		try:
			vec += w2v_model[word].reshape((1,size))
			count += 1
		except KeyError:
			continue
	if count != 0:
		vec /= count
	return vec

def word2vec_model(train_sentences,test_sentense):
	
	train_corpus = build_word2vec_vec(train_sentences)
	
	test_corpus = build_word2vec_vec(test_sentense)


	n_dim = 200

	w2v = Word2Vec(size=n_dim,min_count = 5)

	w2v.build_vocab(train_corpus)
	
	print 'training w2v model...'	
	w2v.train(train_corpus)

	train_vecs = np.concatenate([buildWordVector(w2v,z,n_dim) for z in train_corpus],axis = 0)
	test_vecs =  np.concatenate([buildWordVector(w2v,z,n_dim) for z in test_corpus],axis = 0)

	return (train_vecs,test_vecs)
'''
def word2vec_pipleline(train_sentences,test_sentense):
	train_corpus = build_word2vec_vec(train_sentences)
	test_corpus = build_word2vec_vec(test_sentense)
	return word2vec_model(train_corpus,test_corpus)
'''
import numpy as np

'''
Gensim's Doc2Vec implementation requires each document/paragraph to have a label associated with it.
Here we use LabeledSentence method. The format will be "TRAIN_i" or "TEST_i" whre "i" is a 
dummy index of the review.
'''
from gensim.models.doc2vec import LabeledSentence
def labelizedCorpus(corpus,label_type):
	labelized = []
	for i,v in enumerate(corpus):
		label = "%s_%s"%(label_type,i)
		labelized.append(LabeledSentence(v,[label]))
	return labelized


def get_doc_vecs(model,key_type,corpus_size,dim_size):
	vecs = []
	for i in range(corpus_size):
		key = "%s_%s"%(key_type,i)
		try:
			vecs.append(model.docvecs[key].reshape((1,dim_size)))
		except KeyError:
			continue
	return np.concatenate(vecs,axis = 0)

from gensim.models.doc2vec import Doc2Vec

def doc2vec_model(train_corpus,test_corpus):

	

	labelized_train = labelizedCorpus(train_corpus,"TRAIN")

	labelized_test = labelizedCorpus(test_corpus,"TEST")
	
	#labelized_corpus = np.concatenate((labelized_train,labelized_test),axis = 0)
	vocab = []

	for item in labelized_train:
		vocab.append(item)
	for item in labelized_test:
		vocab.append(item)

	#print 'length of labelized corpus :' + str(len(vocab))

	dim_size = 300

	#instantiate DM and DBOW models
	model_dm = Doc2Vec(min_count = 5, window = 10, size = dim_size, sample = 1e-3, negative = 5, workers = 3, alpha = 0.025, min_alpha = 0.025)
	model_dbow = Doc2Vec(min_count = 5, window = 10, size = dim_size, sample = 1e-3, negative = 5, workers = 3, alpha = 0.025, min_alpha = 0.025,dm = 0)

	model_dm.build_vocab(vocab)
	model_dbow.build_vocab(vocab)

	from progressbar import ProgressBar

	pbar = ProgressBar()

	# change learning rate to get a better performance
	for epoch in pbar(xrange(10)):
		model_dm.train(vocab)
		#model_dm.train(labelized_train)
		model_dm.alpha -= 0.002
		model_dm.min_alpha = model_dm.alpha

		model_dbow.train(vocab)
		#model_dbow.train(labelized_train)
		model_dbow.alpha -= 0.002
		model_dbow.min_alpha = model_dbow.alpha

	#print model_dm.most_similar("good")

	train_vec_dm = get_doc_vecs(model_dm,"TRAIN",len(labelized_train),dim_size)
	test_vec_dm = get_doc_vecs(model_dm,"TEST",len(labelized_test),dim_size)

	train_vec_dbow = get_doc_vecs(model_dbow,"TRAIN",len(labelized_train),dim_size)
	test_vec_dbow = get_doc_vecs(model_dbow,"TEST",len(labelized_test),dim_size)

	if len(train_vec_dbow) != len(labelized_train) or len(test_vec_dbow) != len(labelized_test):
		print "length error"
		return None
	if len(train_vec_dm) != len(labelized_train) or len(test_vec_dm) != len(labelized_test):
		print "length error"
		return None
	train_vec = np.concatenate((train_vec_dm,train_vec_dbow),axis =1)
	print str(len(train_vec)) + "****" + str(len(train_vec[0]))
	test_vec = np.concatenate((test_vec_dm,test_vec_dbow),axis =1)

	from sklearn.decomposition import PCA 
	pca = PCA(n_components = 300)
	train_vec = pca.fit_transform(train_vec)
	test_vec = pca.fit_transform(test_vec)

	return (train_vec,test_vec)


	#model_dbow.train(vocab)
		#model_dbow.train(X_train)
		#model_dbow.alpha -= 0.002
		#model_dbow.min_alpha = model_dbow.alpha

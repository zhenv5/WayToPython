'''
Movie review data: http://www.cs.cornell.edu/people/pabo/movie-review-data/
Sentiment prediction/classification
Author: Jiankai Sun
Date: 2016.02.03
'''

import os
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics import classification_report

from classification_models import sgd, svm_rbf,svm_linear,random_forest,lr,model_ensemble
from classification_models import evaluate_model

# read the data 
def read_files(path,label):
	vector = []
	labels = []
	for dirpath,dirnames,filenames in os.walk(path):
		for file_name in filenames:
			f = open(os.path.join(path,file_name),"r")
			content = f.read()
			vector.append(content)
			labels.append(label)
	return (vector,labels)

# get tf-idf feature vector for training and testing dataset. 
def tf_idf_vectorizer(train,test):

	vectorizer = TfidfVectorizer(max_df = 0.8, min_df = 2, use_idf = True, sublinear_tf = True)
	train_vec = vectorizer.fit_transform(train)
	test_vec = vectorizer.transform(test)
	return (train_vec,test_vec)






if __name__ == "__main__":

	pos_path = "/home/jiankai/Documents/dataset/review_polarity/txt_sentoken/pos"
	neg_path = "/home/jiankai/Documents/dataset/review_polarity/txt_sentoken/neg"
	pos_vec,pos_labels = read_files(pos_path,1)
	neg_vec, neg_labels = read_files(neg_path,0)
	
	X = np.concatenate((pos_vec,neg_vec),axis = 0)
	y = np.concatenate((pos_labels,neg_labels), axis = 0)

	X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.33, random_state = 42)

	train_vec,test_vec = tf_idf_vectorizer(X_train,X_test)

	models = [sgd,svm_linear,random_forest,lr]

	pre_labels = []
	for model in models:
		clf = model(train_vec,y_train)
		pre_labels.append(clf.predict(test_vec))
		print evaluate_model(clf,test_vec,y_test)

	# model ensemble 
	
	new_prediction = model_ensemble(pre_labels,2)
	print 'Model Ensemble'
	print classification_report(y_test,new_prediction)


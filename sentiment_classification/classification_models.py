from sklearn import linear_model 
from sklearn.metrics import classification_report
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier
import numpy as np
# SGD Classifier 
def sgd(train_vec,train_label):
	clf = linear_model.SGDClassifier()
	clf.fit_transform(train_vec,train_label)
	pred_y = clf.predict(train_vec)
	#print 'SGDClassifier Training Accu: ' + str(clf.score(train_vec,train_label))
	return clf 

# svm with rbf kernel
def svm_rbf(train_vec,train_label):
	
	svc = SVC(kernel = "rbf")
	svc.fit(train_vec,train_label)
	pred_y = svc.predict(train_vec)
	#print 'SVC_RBF Training Accu: ' + str(svc.score(train_vec,train_label))
	#print evaluate_model(svc,train_vec,train_label)
	return svc 

# svm with linear kernel
def svm_linear(train_vec,train_label):
	svc = SVC(kernel = "linear")
	svc.fit(train_vec,train_label)
	
	print 'SVC_Linear Training Accu: ' + str(svc.score(train_vec,train_label)) 
	return svc 

# random forest classifier
def random_forest(train_vec,train_label, n_estimators = 10, min_samples_split = 2, min_samples_leaf = 1, criterion = "entropy"):
	model = RandomForestClassifier(n_estimators = 15, min_samples_split = 2, min_samples_leaf = 2,criterion = "gini")
	model.fit_transform(train_vec,train_label)
	
	print 'Random Forest Classification Accu: ' + str(model.score(train_vec,train_label))
	
	return model  

# logistic regression classifier
def lr(train_vec,train_label):
	clf = linear_model.LogisticRegression()
	clf.fit_transform(train_vec,train_label)
	print "Linear Regression Train Accu: " + str(clf.score(train_vec,train_label))
	return clf 


# model ensemble 
def model_ensemble(pre_labels,thresold):
	
	arr = np.array(pre_labels)
	model_nums, data_size = arr.shape	
	new_prediction = [1 if sum(arr[:,i]) >= thresold else 0 for i in xrange(data_size)]

	return new_prediction




# print classification report given model
def evaluate_model(model,test_vec,test_label):

	predict_test = model.predict(test_vec)
	print '********'
	print model
	print 'Classification Report'
	print classification_report(test_label,predict_test)
	return [i for i in range(len(test_label)) if test_label[i] != predict_test[i]]
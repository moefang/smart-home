'''
Created on 10/2015

@author: fan03d

Run example: python classification_PCA4uwb data.csv 3
'''
import csv
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier
import sys
from sklearn.decomposition import PCA


def extractDataWithIndex(fname, featureSta, featureEnd):
	X=[]
	Y=[]
	with open(fname, 'rb') as csvfile:
		rd = csv.reader(csvfile, delimiter=',')
		for row in rd:
			
			temp = np.array(map(float, row))
			
			num=temp.size
			xrow= temp[featureSta:featureEnd]
			
			yrow=temp[num-1]
			X.append(xrow)
			Y.append(int(yrow))
	

	return X, Y

def extractData(fname):
	X=[]
	Y=[]
	with open(fname, 'rb') as csvfile:
		rd = csv.reader(csvfile, delimiter=',')
		for row in rd:
			
			temp = np.array(map(float, row))
			
			num=temp.size
			xrow= temp[0:num-1]
			
			yrow=temp[num-1]
			X.append(xrow)
			Y.append(int(yrow))
			

	return X, Y

if __name__=="__main__":			
	
	fdata = sys.argv[1]

	fcomps= int(sys.argv[2])	
	
	#Input data
	X,Y = extractData(fdata)
	
	print '# of features ', len(X[0])
	print '# of examples ', len(Y)

	#Feature selection by the defined number of components	
	pca=PCA(n_components=fcomps)
	Xn=pca.fit_transform(X)
	
	print '# of selected features ', len(Xn[0])
	
	print '3 folds cross-validation'
	clf=svm.SVC()
	scores = cross_validation.cross_val_score(clf, Xn,Y,cv=3)

	print 'SVM', sum(scores)/3

	clf=GaussianNB()

	scores = cross_validation.cross_val_score(clf, Xn,Y,cv=3)

	print 'NB', sum(scores)/3

	clf = KNeighborsClassifier(n_neighbors=1)

	scores = cross_validation.cross_val_score(clf, Xn,Y,cv=3)

	print 'KNN(k=1)', sum(scores)/3

	clf = DecisionTreeClassifier()

	scores = cross_validation.cross_val_score(clf, Xn,Y,cv=3)

	print 'Decision tree', sum(scores)/3


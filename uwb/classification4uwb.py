'''
Created on 10/2015

@author: fan03d

Run example: python classification_PCA4uwb train.csv test.csv
'''
import csv
import sys
import numpy as np
from sklearn import svm
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score



def extractData(fname):
	X=[]
	Y=[]
	with open(fname, 'rb') as csvfile:
		rd = csv.reader(csvfile, delimiter=',')
		for row in rd:
			#print type(row)
			temp = np.array(map(float, row))
			#print type(tmp.tolist())
			num=temp.size
			xrow= temp[0:num-1]
			#print xrow
			yrow=temp[num-1]
			X.append(xrow)
			Y.append(int(yrow))
			#Y.append(yrow[0])

	return X, Y




if __name__=="__main__":			

	ftrain = sys.argv[1]

	ftest = sys.argv[2]	
	
	X,Y = extractData(ftrain)
	
	print 'Train:'
	print '# of features ', len(X[0])
	print '# of examples ', len(Y)
	
	Xt, Yt=extractData(ftest)	
	
	print 'Test: ', len(Xt[0]), len(Yt)	
	
	clf=svm.SVC()
	clf.fit(X,Y)
	pred=clf.predict(Xt)
	scores = accuracy_score(Yt, pred)

	print 'SVM ', scores

	clf=GaussianNB()

	clf.fit(X,Y)
	pred=clf.predict(Xt)

	scores = accuracy_score(Yt, pred)

	print 'NB ', scores

	clf = KNeighborsClassifier(n_neighbors=1)
	
	clf.fit(X,Y)
	pred=clf.predict(Xt)

	scores = accuracy_score(Yt, pred)

	print 'KNN(k=1) ', scores

	clf = DecisionTreeClassifier()
	clf.fit(X,Y)
	pred=clf.predict(Xt)

	scores = accuracy_score(Yt, pred)

	print 'Decision tree ', scores


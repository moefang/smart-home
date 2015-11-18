'''
Created on 9/2015

@author: fan03d

Run multi-tracker with NB.
'''
import numpy as np
import preprocess as pp
import simplehmm
import itertools
import math
import nbtracker

fsName=['./20150501.csv','./20150502.csv','./20150503.csv','./20150504.csv','./20150504.csv','./20150506.csv', './20150507.csv']

data=pp.getDataAll(fsName)

results=0.0

rid = 0

print 'Tracker ', rid

priors, locations_counts = nbtracker.tracker(data,rid)

locations=['1','2','3','4','5']

train_data = pp.getData4Rid(data, rid)

test_data=[]
test_label=[]
for item in train_data:
	test_data.append(item[1])
	test_label.append(item[0])

bingo=0
for test_rec,label in itertools.izip(test_data,test_label):
	pred_label ='0'
	cur=0.0
	for item in locations:
		pred = priors[item]*locations_counts[label][test_rec]
		if pred > cur:
			pred_label = item
			cur = pred
	
	
	if pred_label == label:
		
		bingo +=1

print 'Accuracy ', bingo*1.0/len(test_data)
results += bingo*1.0/len(test_data)

rid = 1
print 'Tracker ', rid

priors, locations_counts = nbtracker.tracker(data,rid)

locations=['1','2','3','4','5']

train_data = pp.getData4Rid(data, rid)
test_data=[]
test_label=[]
for item in train_data:
	test_data.append(item[1])
	test_label.append(item[0])

bingo=0
for test_rec,label in itertools.izip(test_data,test_label):
	pred_label ='0'
	cur=0.0
	for item in locations:
		pred = priors[item]*locations_counts[label][test_rec]
		if pred > cur:
			pred_label = item
			cur = pred
	
	if pred_label == label:
		bingo +=1


print 'Accuracy ', bingo*1.0/len(test_data)

print 'Accuracy (all): '
results += bingo*1.0/len(test_data)
results = results/2
print results

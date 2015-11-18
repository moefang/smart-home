'''
Created on 9/2015

@author: fan03d

Run multi-tracker with HMM.
'''
import numpy as np
import preprocess as pp
import simplehmm
import itertools
import hmmtracker


fsName=['./20150501.csv','./20150502.csv','./20150503.csv','./20150504.csv','./20150504.csv','./20150506.csv', './20150507.csv']

data=pp.getDataAll(fsName)

results=0.0

rid = 0

trange =6

print 'Tracker ', rid

hmm1 = hmmtracker.tracker(data,rid, trange)

train_data = pp.getSeqData4Rid(data, rid, trange)
test_data=[]
test_label=[]
for item in train_data:
	temp=[]
	templabel=[]
	for item2 in item:	
		temp.append(item2[1])
		templabel.append(item2[0])
	test_data.append(temp)
	test_label.append(templabel)

bingo=0
for test_rec,label in itertools.izip(test_data,test_label):
	[state_seq, seq_prob] = hmm1.viterbi(test_rec)
	if state_seq == label:
		bingo +=1
 	
print 'Accuracy ', bingo*1.0/len(test_data)
results += bingo*1.0/len(test_data)

rid = 1

print 'Tracker ', rid

hmm1 = hmmtracker.tracker(data,rid, trange)

train_data = pp.getSeqData4Rid(data, rid, trange)
test_data=[]
test_label=[]
for item in train_data:
	temp=[]
	templabel=[]
	for item2 in item:	
		temp.append(item2[1])
		templabel.append(item2[0])
	test_data.append(temp)
	test_label.append(templabel)

bingo=0
for test_rec,label in itertools.izip(test_data,test_label):
	[state_seq, seq_prob] = hmm1.viterbi(test_rec)
	if state_seq == label:
		bingo +=1
 	
print 'Accuracy ', bingo*1.0/len(test_data)

print 'Accuracy (all): '
results += bingo*1.0/len(test_data)
results = results/2
print results

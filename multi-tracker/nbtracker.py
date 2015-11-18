'''
Created on 9/2015

@author: fan03d

A tracker implemented by NB.
'''
import numpy as np
import preprocess as pp
import simplehmm
import itertools
import math

def tracker(data, rid):
	train_data=[]

	total=len(data)
	for i in range(total):
		train_data.append((data[i][rid],data[i][2]))

	locations=['1','2','3','4','5']

	observs=["".join(seq) for seq in itertools.product("01", repeat=5)]


	locations_counts = {
    		"1": {},
    		"2": {},
		"3": {},
		"4": {},
		"5": {}
	}	

	for item in locations_counts:
		for item2 in observs:
			locations_counts[item][item2] = 0.


	priors = {
    		"1": 0.,
    		"2": 0.,
		"3": 0.,
    		"4": 0.,
    		"5": 0.
	}

	for item in train_data:
		loc = item[0]
		observ= item[1]
		locations_counts[loc][observ] +=1
		priors[loc] += 1


	return priors, locations_counts


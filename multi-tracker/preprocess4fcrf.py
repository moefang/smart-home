import numpy as np
import preprocess as pp
import simplehmm
import itertools
import math
import nbtracker


fsName=['./20150501.csv','./20150502.csv','./20150503.csv','./20150504.csv','./20150504.csv','./20150506.csv', './20150507.csv']

sensors=['Clothing', 'Living', 'Bedroom', 'Kitchen', 'Laundary']

data=pp.getDataAll(fsName)

fname = 'bluetooth.test12.fcrf'

writer = open(fname,'w')

inte=0
irang=12
# or 6

for record in data:
	label1=record[0]
	label2=record[1]
	features=record[2]
	row=label1+' '+label2+' ----' 
	for i in range(len(features)):
		row=row+' '+features[i]+'@'+sensors[i]

	inte=inte +1
	if inte % irang ==0:
		row = row +'\n'
	print row
	writer.write(row+'\n')

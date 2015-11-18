'''
Created on 09/2015

@author: fan03d

Preprocess for multi-tracker data.
'''
import csv
import numpy as np

def getData(fName):
	data=[]

	with open(fName, 'rb') as csvfile:
		reader=csv.reader(csvfile)
		for i,row in enumerate(reader):
			if i ==0:
				continue
			
			line = [int(item) for item in row]		
			data.append(line)

	return data

def getDataAll(fsName):
	data=[]
	for fName in fsName:
		x=getData(fName)
		x=np.array(x,np.str)
		x2=x.transpose()
		for i in range(len(x2)):
			if x2[i][0]=='0' or x2[i][1]=='0':
				continue
			
			temp=x2[i,[2,3,4,5,6]]
			oberv=''.join(temp)
			row=(x2[i][0], x2[i][1], oberv)
			data.append(row)

	return data

def getData4Rid(data, rid):
	train_data=[]
	total=len(data)
	for i in range(total):
		train_data.append((data[i][rid], data[i][2]))

	return train_data	

def getSeqData4Rid(data, rid, trange):

	train_data=[]
	i=0
	while i< len(data):
		pre=[]
		for j in range(trange):
			i=i+j
			if i >= len(data):
				break
			else:
				pre.append((data[i][rid],data[i][2]))
		
		train_data.append(pre)
		
	return train_data

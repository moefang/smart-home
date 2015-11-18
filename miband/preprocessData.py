'''
Created on 10/2015

@author: fan03d

Run example: python preprocessData.py labels rawdata newdata
'''
import sys
import csv
import datetime
from datetime import timedelta
import itertools
import collections


feInd={'bedroom':0, 'bathroom':1, 'guest':2, 'entertainment':3, 'study':4, 'laundry':5, 'kitchen':6, 'lounge':7}

def genLabels(fname,trange):
	labels=[]
	with open(fname, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			label=row[2]
			stt=str2t(row[0])
			ent=str2t(row[1])
			tmp=stt
			while tmp <= ent:
				labels.append([t2str(tmp),label])
				tmp = tmp +timedelta(seconds=trange)

	return labels

def str2t(tstr):
	return datetime.datetime.strptime(tstr, '%Y%m%d%H%M%S')

def t2str(t):
	return t.strftime('%Y%m%d%H%M%S')


def genData(labels,srawdata,trange):
	data=[]
	for it in labels:
		record=[it[0]]
		features=[0,0,0,0,0,0,0,0]
		n_re =[0,0,0,0,0,0,0,0]
		for i in range(trange):
			tmp=str2t(it[0])+timedelta(i)
			rid=int(t2str(tmp))
			if rid in srawdata:
				values= srawdata[rid]
				for val in values:
					features[feInd[val[0]]] += int(val[1])
					n_re[feInd[val[0]]] +=1
		
		for i in range(len(features)):
			if features[i]==0:
				features[i] =-120
			else:
				features[i] = features[i]*1./n_re[i]
		
		record.extend(features)
		record.append(feInd[it[1]])
		data.append(record)
		
	return data

def genSortedRawData(fname):
	rawdata=dict()
	with open(fname, 'rb') as f:
		reader=csv.reader(f)
		for row in reader:
			rowid = int(row[0])
			try:
				val=int(row[2])
				if val >=0:
					val=-120
			except ValueError:
				val=-120
				pass

			if rowid in rawdata:
				rawdata[rowid].append([row[1], val])			
			else:
				rawdata[rowid]=[[row[1], val]]

	sortedrawdata=collections.OrderedDict(rawdata)
	return sortedrawdata


def saveData(alldata,fname):
	writer=csv.writer(open(fname,'w'))
	for record in alldata:
		writer.writerow(record)

if __name__=="__main__":

	flabel = sys.argv[1]

	fdata = sys.argv[2]

	fnew = sys.argv[3]
	
	trange =5
	
	print 'Load labels ..'
	labels = genLabels(flabel,trange)
	
	print 'Load raw data ..'
	sortedData=genSortedRawData(fdata)
	
	print 'Preprocessing ..'
	alldata=genData(labels, sortedData,trange)
	
	saveData(alldata,fnew)
		
	print 'Good done.'

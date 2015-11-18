'''
Created on 08/2015

@author: fan03d

Download data according to the query.
Run example: python getDataFromDB.py "select scannerPos, local_time_string, rssi_string from acbi.estimote_beaconrecord where local_time_string like '20151024%'" rawdata
'''
import datetime
from datetime import timedelta
import mysql.connector
import csv
import sys

def download(query_str, fname):
	cnx = mysql.connector.connect(user='fan03d', password='acbifan03dmoe', host='Mysqlprd-cdc.it.csiro.au', database='acbi')
	cursor = cnx.cursor()

	query=(query_str)

	cursor.execute(query)

	writer = csv.writer(open(fname, 'w'))

	num_row =0
	for (sp, lt, rssi_string) in cursor:
	
		time=datetime.datetime.strptime(lt, '%Y%m%d%H%M%S')
	
		rssi_str=rssi_string.encode('ascii')
		
		offsets=rssi_str.rstrip("|").split("|")
	
		for item in offsets:
		
			try:
				it, ival = item.rstrip().split()
			except ValueError:
				print offsets
				print item
				pass

					
			tstamp = time + timedelta(seconds=int(it))	
			writer.writerow([tstamp.strftime("%Y%m%d%H%M%S"), sp.rstrip(), ival])
	
		num_row = num_row +1
		print "# of records ", num_row


	cursor.close()
	cnx.close()

if __name__=="__main__":

	query = sys.argv[1]
	foutput = sys.argv[2]

	download(query, foutput)

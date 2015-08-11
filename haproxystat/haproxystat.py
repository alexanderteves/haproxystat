# encoding: utf-8

from __future__ import print_function

import csv
import requests
import StringIO

class HAProxyStat(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def __getCsv(self):
		response = requests.get('http://{}:{}/;csv'.format(self.host, self.port))
		if not response.ok:
			raise Exception('HTTP response code was {}'.format(response.status_code))
		return StringIO.StringIO(response.text)

	def __prettyPrint(self, statisticsDict, padding):
		for key in statisticsDict.iterkeys():
			print('{} {}'.format(key.ljust(padding), statisticsDict[key]))

	def printCsv(self):
		print(self.__getCsv().read())

	def printStatistic(self, statistic):
		columns = statistic.split('.')
		if(len(columns) < 3):
			raise Exception('Parameter \'{}\' is not formatted pxname.svname.value')
		pxname = columns[0]
		svname = columns[1]
		value = columns[2]
		csvFile = self.__getCsv()
		reader = csv.DictReader(csvFile)
		for row in reader:
			if((row['# pxname'].lower() == pxname) and (row['svname'].lower() == svname)):
				print(row[value])

	def printAllStatistics(self):
		csvFile = self.__getCsv()
		reader = csv.DictReader(csvFile)
		statisticsDict = dict()
		padding = 0
		for row in reader:
			for key in row.iterkeys():
				if((key != '# pxname') and (key != 'svname') and key):
					statisticName = '{}.{}.{}'.format(row['# pxname'].lower(), row['svname'].lower(), key)
					if len(statisticName) > padding:
						padding = len(statisticName)
					if(row[key]):
						statisticsDict[statisticName] = row[key]
						#print('{}.{}.{}\t{}'.format(row['# pxname'].lower(), row['svname'].lower(), key, row[key]))
					else:
						statisticsDict[statisticName] = 'n/a'
						#print('{}.{}.{}\tn/a'.format(row['# pxname'].lower(), row['svname'].lower(), key))
		self.__prettyPrint(statisticsDict, padding)

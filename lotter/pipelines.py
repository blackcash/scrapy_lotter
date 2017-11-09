# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class LotterPipeline(object):

	def __init__(self):
	    self.fileCsv1 = open('lotte.csv', 'w')
	    self.fieldnames1 = ['per','date','num1','num2','num3','num4','num5','num6','num7']
	    self.writer1 = csv.DictWriter(self.fileCsv1, fieldnames=self.fieldnames1)
	    self.writer1.writeheader()
	    self.fileCsv2 = open('total.csv', 'w')
	    self.fileCsv2.write("nums,counts\n")

	def process_item(self,item,spider):
		dictionary = dict(item)
		print (dictionary,'*****')
		if 'num1' in dictionary:
			self.writer1.writerow(dictionary)
		else:
			for num in dictionary['nums']:
				self.fileCsv2.write(str(num)+","+str(dictionary['counts'][num-1])+"\n")
		return item

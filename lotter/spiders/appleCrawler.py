import scrapy
from bs4 import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider
from lotter.items import LotterItem
from lotter.items import TotalItem

class AppleCrawler(CrawlSpider):
	domains = ['www.9800.com.tw']
	name = 'lotter'
	start_urls = [
	'http://www.9800.com.tw/lotto649/statistics50.html',
	]

	def parse(self,response):
		#num = []
		res = BeautifulSoup(response.body,'lxml')
		tbodys = res.select('tbody')
		trs = tbodys[4].select('tr')

		nums = []
		counts = []
		for i in range(1,50):
			nums.append(i)
			counts.append(0)
		for tr in trs:
			dic = LotterItem()
			for n in range(0,9):
				data = tr.select('td')[n].text
				if n == 0:
					dic['per'] = data
				elif n == 1:
					dic['date'] = data
				else:
					dic['num'+str(n-1)] = data
					print ('----',data)
					counts[int(data)-1] += 1
					'''
					if data in cou:
						cou[data] += 1
					else:
						cou[data] = 0
					'''	
				#print (tr.select('td')[n].text)
			yield dic
		cou = TotalItem()
		cou['nums'] = nums
		cou['counts'] = counts
		print ('=========',cou)
		yield cou
			#num.append(dic)

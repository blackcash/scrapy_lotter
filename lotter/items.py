# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotterItem(scrapy.Item):
    # define the fields for your item here like:
    num1 = scrapy.Field()
    num2 = scrapy.Field()
    num3 = scrapy.Field()
    num4 = scrapy.Field()
    num5 = scrapy.Field()
    num6 = scrapy.Field()
    num7 = scrapy.Field()
    per = scrapy.Field()
    date = scrapy.Field()

class TotalItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    finish = scrapy.Field()
    

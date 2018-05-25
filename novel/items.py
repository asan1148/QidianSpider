# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ExampleItem(scrapy.Item):
	file_urls = scrapy.Field()#小说下载地址
	
	files = scrapy.Field()#小说文件
	
	file_name = scrapy.Field()#小说名字
	
	novel_author =scrapy.Field()#小说作者

	novel_type = scrapy.Field()#小说类型
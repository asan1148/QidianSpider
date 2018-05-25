#coding=utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import ExampleItem
import time
class novelSpider(scrapy.Spider):
	name = "mynovel"
	allowed_domains = ["qidian.com","read.qidian.com","book.qidian.com","download.qidian.com",'matplotlib.org']
	start_urls = ['https://www.qidian.com/all']	
	
	
	def parse(self,response):
		novellist =  response.xpath('//ul[@class="all-img-list cf"]/li')#找到小说列表
		example = ExampleItem()  #对小说信息进行处理
		example['file_urls'] = []
		example['file_name'] = []
		example['novel_author'] = []
		example['novel_type'] = []
		for novel in novellist:
			novelbid = novel.xpath('div[2]/h4/a/@data-bid').extract()[0]#小说信息根据xpath提取
			novelname = novel.xpath('div[2]/h4/a/text()').extract()[0]
			novelauthor = novel.xpath('div[2]/p/a/text()').extract()[0]
			noveltype = novel.xpath('div[2]/p/a[2]/text()').extract()[0]
			url = 'http://download.qidian.com/epub/'+novelbid+'.epub' #小说url的拼装
			example['file_urls']=[url]  #小说信息的各个赋值
			example['file_name']=[novelname]
			example['novel_author']=[novelauthor]
			example['novel_type']=[noveltype]  
			yield example   #送入下一步处理

		nexturl = response.xpath('//*[@id="page-container"]/div/ul/li[last()]/a/@href').extract()[0] #对下一页的连接发送请求
		nexturl =  response.urljoin(nexturl)
		print nexturl + '-----------------------------------------------------------------------------------'
		if nexturl:#如果存在  对下一步连接请求
			yield scrapy.Request(nexturl,callback=self.parse)

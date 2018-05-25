# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from urlparse import urlparse
from os.path import basename,dirname,join
from scrapy import Request
import re

class NovelPipeline(object):
    def process_item(self, item, spider):
        return item
class FileDownloadPipeline(FilesPipeline):

	def get_media_requests(self, item, info):
		listlen = len(item['file_urls'])
		for num in range(0,listlen):
			file_url = item['file_urls'][num]
			novelname = item['file_name'][num]
			novelauthor=item['novel_author'][num]
			file_name = novelauthor+'-'+novelname
			yield Request(file_url,meta={'name':file_name})			
	def file_path(self, request, response=None, info=None):

		path=urlparse(request.url).path
		temp=join(basename(dirname(path)),basename(path))
		name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
		name = re.sub(r'[？\\*|“<>:/]', '', name)

		return '%s/%s' % (basename(dirname(path)), name+'.epub')

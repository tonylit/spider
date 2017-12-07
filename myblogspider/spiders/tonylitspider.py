# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append("..")
from items import MyblogspiderItem

class TonylitspiderSpider(scrapy.Spider):
    
    #爬虫名称
    name = 'tonylitspider'
    
    #爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['tonylit.me']
    
    baseURL = "http://tonylit.me/"
    #页码
    offset = 2
    #从此url开始爬取
    start_urls = ['http://tonylit.me/']

    def parse(self, response):
	
        #获取文章标题
	title_list = response.xpath("//a[@class='article-title']/text()").extract()
	
        #获取文章标签
        tag_list = response.xpath("//ul[@class='article-tag-list']/li/a/text()").extract()

	#获取文章链接
        link_list = response.xpath("//a[@class='article-title']/@href").extract()

	#获取发布时间
        time_list =  response.xpath("//time/@datetime").extract()

	#创建items对象-orm
	items = MyblogspiderItem()

	try:
		#每页8篇文章
		for temp in range(1,8):
	        	#存储文章标题到item	
        		items['title'] = title_list[temp].encode("utf-8")

        		#存储文章标签到item 
			items['tag'] = tag_list[temp].encode("utf-8")
	
        		#存储文章链接到item 
			items['link'] = str("http://tonylit.me") + link_list[temp].encode("utf-8")

        		#存储发布时间到item 
			items['time'] = time_list[temp].encode("utf-8")

			yield items

	except :
		print "error"
	else:
		#取前11页，进行翻页处理
		if self.offset < 11:
			self.offset += 1
			nextURL = 'http://tonylit.me/page/'+str(self.offset) 
		
			#递归调用parse
			yield scrapy.Request(nextURL,callback = self.parse)


if __name__ == "__main__" : 
	pass

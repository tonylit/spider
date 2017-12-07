# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #文章标题
    title = scrapy.Field()
    #文章标签
    tag = scrapy.Field()
    #文章链接
    link = scrapy.Field()
    #发布时间
    time = scrapy.Field()
	
    

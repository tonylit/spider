# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyblogspiderPipeline(object):


    #初始化，打开tonylit.json文件，用来写入items
    def __init__(self):
	self.f = open("tonylit.json","w")

    def process_item(self, item, spider):
        
	#把item转成字典，写入文件中
     	content = json.dumps(dict(item)) + ", \n"
        self.f.write(content)
        
 	return item
    
    
    #spider全部结束后，关闭文件
    def close_spider(self,spider):
	self.f.close()

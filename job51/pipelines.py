# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from pymongo import MongoClient


class Job51Pipeline(object):
    def __init__(self):
        self.client=MongoClient()
        self.collection = self.client["job51"]["Java"]

    def process_item(self, item, spider):
         # ===============================日志记录==================================
         print("item::::%s" %item)
         logging.warning("item::::::: %s" %item)
         # 转换为字典,并保存到mongodb
         self.collection.insert(dict(item))
         return item

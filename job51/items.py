# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义数据的字段
    jobName=scrapy.Field()     #职位名称
    jobInfo=scrapy.Field()     #职位信息
    jobRequest=scrapy.Field()  #职位要求
    jobYearRequest=scrapy.Field() #工作年限要求
    jobCompany=scrapy.Field()     #公司名称
    jobSalary=scrapy.Field()      #薪资待遇
    jobErea=scrapy.Field()    #工作地点
    date=scrapy.Field()    #招聘时间
    jobHref=scrapy.Field()
    pass

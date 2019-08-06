# -*- coding: utf-8 -*-
import scrapy
from job51.items import Job51Item
import logging
import re
class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']
    start_urls = ['https://m.51job.com/search/joblist.php?keyword=Java+开发工程师&keywordtype=2&jobarea=040000&landmark=&issuedate=&saltype=&degree=&funtype=&indtype=&jobterm=&cotype=&workyear=&cosize=&lonlat=&tubename=&tubeline=&radius=&filttertype=']


    def parse(self, response):
        """首页解析的方法"""
        # 1.爬取起始页的数据
        item=Job51Item()
        job_list=response.xpath("//div[@id='pageContent']/div[@class='items']/a")
        for job_one in job_list:
            # 职位信息详情url
            item["jobHref"]=job_one.xpath("./@href").extract_first()
            # 工作地点
            item["jobErea"]=job_one.xpath("./i/text()").extract_first()
            # 公司名称
            item["jobCompany"]=job_one.xpath("./aside/text()").extract_first()
            # 薪资待遇
            item["jobSalary"]=job_one.xpath("./em/text()").extract_first()
            # ===============================日志记录==================================
            # logging.warning("item::::::: %s" %item)
            yield scrapy.Request(
                # 职位详情url
                item["jobHref"],
                # 回调函数
                callback=self.parse_detail,
                meta={"item":item}
            )
        # 2.爬取下一页的数据
        next_url=response.xpath("//div[@id='pageContent']/form[@id='turnpage']/div[@class='paging']/a[@class='next']/@href").extract_first()
        # 如果存在下一页就需要继续爬取
        # javascript:void(0);
        if not next_url.find("javascript")>=0:
            yield scrapy.Request(
                # 下一页
                next_url,
                # 回调函数
                callback=self.parse
            )
        yield item

    def parse_detail(self,response):
        """详情解析的url"""
        item=response.meta["item"]
        # 职位名称 ,例如中级开发工程师
        item["jobName"]=response.xpath("//div[@id='pageContent']/div[@class='mod m1']/div[@class='jt']/p/text()").extract_first()
        # 发布时间
        item["date"]=response.xpath("//div[@id='pageContent']/div[@class='mod m1']/div[@class='jt']/span/text()").extract_first()
        # 岗位jd-岗位jd有多余字符 ,需要处理
        item["jobRequest"]=response.xpath("//div[@id='pageContent']/div[@class='mod']/div[@class='ain']/article/p/text()").extract()
        # 处理特殊字符
        item["jobRequest"]=[re.sub(r"\xa0|' '|\xa0|\s|\n","",i) for i in  item["jobRequest"]]
        # 处理空格
        item["jobRequest"]=[i for i in item["jobRequest"] if len(i)>0]
        yield item

# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
import time

class MeishijieSpider(CrawlSpider):
    name = 'meishijie'
    allowed_domains = ['meishij.net']
    start_urls = ['http://www.meishij.net']

    num = 0
    next_page = 0

    rules = (
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/$')), callback= 'test', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/\?&page=\d+$')), callback= 'next', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/zuofa/\w+\.html')), callback='save')
    )

    def next(self, response):
        self.next_page += 1
        print("next++++++++++++++++++++++++++++++++++++++++++", self.next_page)

    def save(self, response):
        self.num += 1
        print(response.xpath(".//*[@id='tongji_title']/text()").extract(), self.num)
        #time.sleep(1)

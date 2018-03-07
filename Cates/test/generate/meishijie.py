
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
import time

class Spider_meishijie(CrawlSpider):
    name = 'meishijie'
    allowed_domains = ['meishij.net']
    start_urls = ['http://www.meishij.net']

    num = 0
    next_page = 0

    rules = (Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/$')), callback= 'test', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/\?&page=\d+$')), callback= 'next', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/zuofa/\w+\.html')), callback='save')
    )


    def save(self, response):
        self.num += 1
        print(self.num)


import os

spider_temp = \
"""
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
import time

class Spider_%s(CrawlSpider):
    name = '%s'
    allowed_domains = ['%s']
    start_urls = ['%s']

    num = 0
    next_page = 0

    rules = (%s)


    def save(self, response):
        self.num += 1
        print(self.num)

"""

arr = (
    'meishijie',
    'meishijie',
    'meishij.net',
    'http://www.meishij.net',
    '''Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/$')), callback= 'test', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/china-food/xiaochi/\?&page=\d+$')), callback= 'next', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.meishij.net/zuofa/\w+\.html')), callback='save')
    ''',

)

ok = spider_temp % arr
filename = os.getcwd() + '\generate\meishijie.py'
#if not os.path.exists(filename):
#    os.makedirs(filename)
with open(filename, 'w') as f:
    f.write(ok)
    print('success')


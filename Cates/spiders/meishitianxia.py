from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractor import LinkExtractor
import time

class MstxSpider(CrawlSpider):
    name = 'mstx'
    allowed_domains = ['home.meishichina.com']
    start_urls = ['http://home.meishichina.com/recipe-type.html']
    num = 0

    rules = (
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe/\w+/page/\d+/$')), follow=True),
        Rule(LinkExtractor(allow=(r'http://home.meishichina.com/recipe-\d+.html$')), callback='test')
    )

    def test(self, response):
        self.num += 1
        print(response.xpath(".//*[@id='recipe_title']/text()").extract(), self.num)
        print(response)
        time.sleep(60)
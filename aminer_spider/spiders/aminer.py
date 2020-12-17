import scrapy


class AminerSpider(scrapy.Spider):
    name = 'aminer'
    allowed_domains = ['www.aminer.cn']
    start_urls = ['http://www.aminer.cn/']

    def parse(self, response):
        pass

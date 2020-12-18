from scrapy.crawler import CrawlerProcess
from aminer_spider.spiders.aminer import AminerSpider
from aminer_spider.spiders.fund import FundSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    # process.crawl(AminerSpider)
    process.crawl(FundSpider)
    process.start()
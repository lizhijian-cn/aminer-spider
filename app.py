from scrapy.crawler import CrawlerProcess
from aminer_spider.spiders.aminer import AminerSpider


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(AminerSpider)
    process.start()
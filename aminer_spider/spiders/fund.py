import scrapy
import json
import time
from scrapy.http import JsonRequest
from aminer_spider.items import FundItem

class FundSpider(scrapy.Spider):
    name = 'fund'

    def start_requests(self):
        fund_url = 'https://apiv2.aminer.cn/magic?a=GetFundsByPersonID__person.GetFundsByPersonID___'
        data = [
            {
                "action": "person.GetFundsByPersonID",
                "parameters": {
                    "id": "560d166a45cedb33975a4f0e",
                    "end": 20,
                    "start": 0
                }
            }
        ]

        with open("data/a.txt", "r") as file:
            for line in file:
                author = json.loads(line)
                data[0]['parameters']['id'] = author['id']
                time.sleep(0.5)
                yield JsonRequest(fund_url, callback=self.parse, data=data,
                                  meta={'author_id': author['id']})

    def parse(self, response):
        res = json.loads(response.text)
        if not res['data'][0]['succeed'] or not 'items' in res['data'][0]:
            return
        fund_list = res['data'][0]['items']
        for fund_info in fund_list:
            print(fund_info)
            fund = FundItem()
            fund['id'] = fund_info['id']
            fund['author_id'] = response.meta['author_id']
            fund['title'] = fund_info['title']
            fund['title_zh'] = fund_info['title_zh']
            fund['abstract'] = fund_info['abstract']
            fund['abstract_zh'] = fund_info['abstract_zh']
            fund['desc_zh'] = fund_info['desc_zh'] if 'desc_zh' in fund_info else ''
            fund['start_year'] = fund_info['start_year']
            fund['end_year'] = fund_info['end_year']
            fund['end_date'] = fund_info['end_date']
            fund['lang'] = fund_info['lang']
            fund['results'] = fund_info['results'] if 'results' in fund_info else []
            fund['src'] = fund_info['src']
            fund['type'] = fund_info['type']
            fund['url'] = fund_info['url'][0]
            yield fund
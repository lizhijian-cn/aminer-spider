import json
import time

import scrapy
from scrapy.http import JsonRequest

from aminer_spider.items import AuthorItem, PaperItem


class AminerSpider(scrapy.Spider):
    name = 'aminer'

    # start_urls = ['http://www.aminer.cn/']
    def start_requests(self):
        personal_info_url = 'https://apiv2.aminer.cn/magic?a=getPerson__personapi.get___'
        data = [
            {
                "action": "personapi.get",
                "parameters": {
                    "ids": [
                        "5444ce9cdabfae87074e88e6"
                    ]
                },
                "schema": {
                    "person": [
                        "id",
                        "name",
                        "name_zh",
                        "avatar",
                        "num_view",
                        "is_follow",
                        "work",
                        "hide",
                        "nation",
                        "language",
                        "bind",
                        "acm_citations",
                        "links",
                        "educations",
                        "tags",
                        "tags_zh",
                        "num_view",
                        "num_follow",
                        "is_upvoted",
                        "num_upvoted",
                        "is_downvoted",
                        "is_lock",
                        {
                            "indices": [
                                "hindex",
                                "pubs",
                                "citations"
                            ]
                        },
                        {
                            "profile": [
                                "position",
                                "position_zh",
                                "affiliation",
                                "affiliation_zh",
                                "work",
                                "gender",
                                "lang",
                                "homepage",
                                "phone",
                                "email",
                                "fax",
                                "bio",
                                "bio_zh",
                                "edu",
                                "address",
                                "note",
                                "homepage",
                                "title",
                                "titles"
                            ]
                        }
                    ]
                }
            }
        ]
        with open("data/a.txt", "r") as file:
            for line in file:
                author = json.loads(line)
                data[0]['parameters']['ids'][0] = author['id']
                meta = {'orgs': ''}
                if 'orgs' in author:
                    meta['orgs'] = author['orgs']
                time.sleep(0.5)
                yield JsonRequest(personal_info_url, callback=self.parse, data=data, meta=meta)

    # parse author
    def parse(self, response, **kwargs):
        paper_url = 'https://apiv2.aminer.cn/magic?a=GetPersonPubs__person.GetPersonPubs___'
        data = [
            {
                "action": "person.GetPersonPubs",
                "parameters": {
                    "offset": 0,
                    "size": 20,
                    "sorts": [
                        "!year"
                    ],
                    "ids": [
                        "560d166a45cedb33975a4f0e"
                    ],
                    "searchType": "all"
                },
                "schema": {
                    "publication": [
                        "id",
                        "year",
                        "title",
                        "title_zh",
                        "authors._id",
                        "authors.name",
                        "authors.name_zh",
                        "num_citation",
                        "venue.info.name",
                        "venue.volume",
                        "venue.info.name_zh",
                        "venue.issue",
                        "pages.start",
                        "pages.end",
                        "lang",
                        "pdf",
                        "doi",
                        "urls",
                        "versions"
                    ]
                }
            }
        ]
        res = json.loads(response.text)
        if not res['data'][0]['succeed']:
            raise RuntimeError('author not found')

        author_info = res['data'][0]['data'][0]
        author = AuthorItem()
        author['id'] = author_info['id']
        author['name'] = author_info['name']
        author['name_zh'] = author_info['name_zh']
        author['orgs'] = response.meta['orgs']
        author['avatar'] = author_info['avatar'] if 'avatar' in author_info else ''
        author['h_index'] = author_info['indices']['hindex']
        author['n_pubs'] = author_info['indices']['pubs']
        author['n_citation'] = author_info['indices']['citations']
        yield author

        data[0]['parameters']['ids'][0] = author_info['id']
        # paper_count = author_info['indices']['pubs']
        paper_count = 10
        for offset in range(0, paper_count, 20):
            data[0]['parameters']['offset'] = offset
            time.sleep(0.5)
            yield JsonRequest(paper_url, callback=self.parse_paper, data=data)

    def parse_paper(self, response):
        res = json.loads(response.text)
        if not res['data'][0]['succeed']:
            raise RuntimeError('paper not found')

        paper = PaperItem()
        paper_info = res['data'][0]['data'][0]

        # paper['id'] =
        # paper['title'] =
        # paper['authors'] =    # list
        # paper['abstract'] =
        # paper['venue'] =
        # paper['year'] =
        # paper['n_citation'] =
        # paper['doi'] =
        # paper['lang'] =
        # paper['page_start'] =
        # paper['page_end'] =
        # paper['volume'] =
        # paper['issue'] =
        # paper['issn'] =
        # paper['isbn'] =
        # paper['pdf'] =
        # paper['url'] =

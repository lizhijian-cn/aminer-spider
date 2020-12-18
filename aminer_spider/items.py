# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AminerSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class AuthorItem(scrapy.Item):
    id = Field()
    avatar = Field()
    name = Field()
    name_zh = Field()
    orgs = Field()
    h_index = Field()
    n_pubs = Field()
    n_citation = Field()


class PaperItem(scrapy.Item):
    id = Field()
    title = Field()
    authors = Field()   # list
    abstract = Field()
    venue = Field()
    year = Field()
    n_citation = Field()
    doi = Field()
    lang = Field()
    page_start = Field()
    page_end = Field()
    volume = Field()
    issue = Field()
    issn = Field()
    isbn = Field()
    pdf = Field()
    url = Field()


class FundItem(scrapy.Item):
    id = Field()
    author_id = Field()
    title = Field()
    title_zh = Field()
    abstract = Field()
    abstract_zh = Field()
    desc_zh = Field()
    start_year = Field()
    end_year = Field()
    end_date = Field()
    lang = Field()
    results = Field()
    src = Field()
    type = Field()
    url = Field()
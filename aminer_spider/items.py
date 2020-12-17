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
    indices = Field()
    homepage = Field()
    name = Field()
    name_zh = Field()
    profile = Field()


class PaperItem(scrapy.Item):
    authors = Field()
    title = Field()
    url = Field()
    venue = Field()
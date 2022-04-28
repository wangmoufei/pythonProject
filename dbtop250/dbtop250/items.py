# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Dbtop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    score = scrapy.Field()
    comments = scrapy.Field()


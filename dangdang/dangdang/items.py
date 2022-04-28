# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 图书标题、图片、作者,出版时间、价格、评论条数
class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 图书标题
    pic = scrapy.Field()  # 图片
    author = scrapy.Field()  # 作者
    publish = scrapy.Field()  # 出版时间
    price = scrapy.Field()  # 价格
    comment = scrapy.Field()  # 评论条
    image_urls = scrapy.Field()
    images = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    playlistID = scrapy.Field()  # 播放列表ID
    name = scrapy.Field()  # 歌单名字
    tags = scrapy.Field()  # 标签
    createTime = scrapy.Field()  # 创建时间
    playCount = scrapy.Field()  # 播放次数
    subscribedCount = scrapy.Field()  # 订阅计数
    nickname = scrapy.Field()  # 昵称
    gender = scrapy.Field()  # 性别
    userType = scrapy.Field()  # 用户类型
    vipType = scrapy.Field()  # vip类型
    province = scrapy.Field()  # 省
    city = scrapy.Field()  # 城市

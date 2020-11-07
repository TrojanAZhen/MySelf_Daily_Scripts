# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AqiItem(scrapy.Item):
    city = scrapy.Field()      # 城市名
    date = scrapy.Field()      # 日期
    aqi = scrapy.Field()       # 空气质量指数
    level = scrapy.Field()     # 质量等级
    pm2_5 = scrapy.Field()     # pm2.5 小于2.5微米的颗粒物
    pm10 = scrapy.Field()      # pm10 小于10微米的颗粒物
    so2 = scrapy.Field()       # 二氧化硫
    co = scrapy.Field()        # 一氧化碳
    no2 = scrapy.Field()       # 二氧化氮
    o3 = scrapy.Field()        # 臭氧
    rank = scrapy.Field()      # 当天的全国排名
    spider = scrapy.Field()    # 爬虫名

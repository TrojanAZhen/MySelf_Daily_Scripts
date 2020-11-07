# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class IqiyiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # fenlei = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()


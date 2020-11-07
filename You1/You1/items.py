# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class You1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fenlei_name = scrapy.Field()
    fenlei_url = scrapy.Field()
    movie_name = scrapy.Field()
    movie_url = scrapy.Field()
    movie_image = scrapy.Field()

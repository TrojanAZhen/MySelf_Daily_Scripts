# -*- coding: utf-8 -*-
import scrapy
from iqiyi_spider.items import IqiyiSpiderItem


class IqiyiSpider(scrapy.Spider):
    name = 'iqiyi'
    # allowed_domains = ['iqiyi.com']
    start_urls = ['http://www.iqiyi.com/weidianying/']

    def parse(self, response):
        texts = response.xpath('//div[@class="site-piclist_pic"]/a')
        for text in texts:
            item = IqiyiSpiderItem()
            # 大分类
            # text.xpath = response.xpath('//span[@rseat="title"]').extract()
            # 电影名字
            item['name'] = text.xpath('./@title').extract()[0]
            # 电影链接
            item['url'] = text.xpath('./@href').extract()[0]
            # 电影宣传画
            item['image'] = text.xpath('./img/@src').extract()[0]
            yield item

# -*- coding: utf-8 -*-
import scrapy
from Vimeo.items import VimeoItem


class VimeoSpider(scrapy.Spider):
    name = 'vimeo'
    #allowed_domains = ['vimeo.com']
    start_urls = ['https://vimeo.com/']

    def parse(self, response):
        #print "-" * 50
        texts = response.xpath('//div[@class="iris_video-vital iris_video-vital--browse iris_video-vital--reveal"]')
        for text in texts:
            print "-" * 50
            item = VimeoItem()
            item["fenlei_name"] = text.xpath('.//a[@class="iris_userinfo user-vital-item iris_link iris_link--gray-4"]/span/text()').extract()[0]
            item["fenlei_url"] = "https://vimeo.com" + text.xpath('.//div[@class="iris_uservital-content"]/a/@href').extract()[0]
            item["movie_name"] = text.xpath('.//h5[@class="l-ellipsis"]/span/text()').extract()[0]
            item["movie_url"] = "https://vimeo.com" + text.xpath('./a/@href').extract()[0]
            item["movie_image"] = text.xpath('.//div/img/@src').extract()[0]
            item["movie_play"] = text.xpath('.//span[@class="user-vital-item"]//span/text()').extract()[0]
            print "-" * 50
            print item["fenlei_url"]
            # yield item

# -*- coding: utf-8 -*-
import scrapy
from You1.items import You1Item


class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    allowed_domains = ['youtube.com']
    start_urls = ['http://youtube.com/']

    def parse(self, response):
        texts = response.xpath('//div[@class="yt-lockup-dismissable"]')
        for text in texts:
            item = You1Item()
            item["fenlei_name"] = text.xpath('.//div[@class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"]/a/text()').extract()[0]
            item["fenlei_url"] = "https://www.youtube.com" + text.xpath('.//div[@class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"]/a/@href').extract()[0]
            item["movie_name"] = text.xpath('.//div[@class="yt-lockup-content"]//a/@title').extract()[0]
            item["movie_url"] = "https://www.youtube.com" + text.xpath('.//div[@class="yt-lockup-content"]//a/@href').extract()[0]
            item["movie_image"] = text.xpath('.//span[@class="yt-thumb-simple"]/img/@src').extract()[0]
            print "-" * 50
            print item["movie_url"]
            yield item

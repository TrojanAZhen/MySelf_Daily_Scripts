# -*- coding: utf-8 -*-
import scrapy
from Youtube.items import YoutubeItem

class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    allowed_domains = ['youtube.com']
    start_urls = ['http://youtube.com/']

    def parse(self, response):
        texts = response.xpath('//div[@class="yt-lockup-content"]')
        for text in texts:
            item = YoutubeItem()
            item["fenlei"] = text.xpath('.//div[@class="yt-lockup-byline yt-ui-ellipsis yt-ui-ellipsis-2"]/a/text()').extract()[0]
            item["movie_name"] = text.xpath('./h3/a/@title').extract()[0]
            item["movie_url"] = "https://www.youtube.com/" + text.xpath('./h3/a/@href').extract()[0]
            print "-" * 20
            print item["movie_url"]
            yield item


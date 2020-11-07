# -*- coding: utf-8 -*-
import scrapy
from KongQiZhiLiang.items import KongqizhiliangItem

class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    base_url = "https://www.aqistudy.cn/historydata/"

    def parse(self, response):
        city_url_list = response.xpath("//div[@class='all']/div[@class='bottom']//li/a/@href").extract()
        for city_url in city_url_list:
            url = self.base_url + city_url
            yield scrapy.Request(url, callback=self.parse_mouth)

    def parse_mouth(self, response):
        mouth_url_list = response.xpath("//td[@align='center']/a/@href").extract()
        for mouth_url in mouth_url_list:
            url = self.base_url + mouth_url
            yield scrapy.Request(url, callback=self.parse_day)

    def parse_day(self, response):
        day_list = response.xpath("//table[@class='table table-condensed table-bordered table-striped table-hover table-responsive']//tr")
        city = response.xpath("/html/head/title/text()").extract()[0][8:-39]
        day_list.pop(0)
        for day in day_list:
            item = KongqizhiliangItem()
            item['city'] = city
            item['date'] = day.xpath("./td[1]/text()").extract_first() if not "" else "0"
            item['aqi'] = day.xpath("./td[2]/text()").extract_first() if not "" else "0"
            item['level'] = day.xpath("./td[3]/text()").extract_first() if not "" else "0"
            item['pm2_5'] = day.xpath("./td[4]/text()").extract_first() if not "" else "0"
            item['pm10'] = day.xpath("./td[5]/text()").extract_first() if not "" else "0"
            item['so2'] = day.xpath("./td[6]/text()").extract_first() if not "" else "0"
            item['co'] = day.xpath("./td[7]/text()").extract_first() if not "" else "0"
            item['no2'] = day.xpath("./td[8]/text()").extract_first() if not "" else "0"
            item['o3'] = day.xpath("./td[9]/text()").extract_first() if not "" else "0"
            item['rank'] = day.xpath("./td[10]/text()").extract_first() if not "" else "0"
            yield item

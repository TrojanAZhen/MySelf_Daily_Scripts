# -*- coding: utf-8 -*-
import scrapy
import urllib
from AQI.items import AqiItem

class AqiSpider(scrapy.Spider):
    name = 'aqi'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    baseURL = "https://www.aqistudy.cn/historydata/"

    # 提取每个城市的链接，并发送请求
    def parse(self, response):
        cityURL_list = response.xpath("//div[@class='all']/div[@class='bottom']//li/a/@href").extract()

        for cityURL in cityURL_list:
            url = self.baseURL + cityURL
            yield scrapy.Request(url, callback = self.parse_month)

    # 提取每个城市的每个月的链接，并发送请求
    def parse_month(self, response):
        monthURL_list = response.xpath("//td[@align='center']/a/@href").extract()

        for monthURL in monthURL_list:
            url = self.baseURL + monthURL
            yield scrapy.Request(url, callback = self.parse_day)

    # 提取每一天的历史数据
    def parse_day(self, response):
        day_list = response.xpath("//table[@class='table table-condensed table-bordered table-striped table-hover table-responsive']//tr")
            # 获取城市
        city = response.xpath("/html/head/title/text()").extract()[0][8:-39]

        day_list.pop(0)
        for day in day_list:
            item = AqiItem()

            item['city'] = city
            # date = day.xpath("./td[1]/text()").extract_first()
            # aqi = day.xpath("./td[2]/text()").extract_first()
            # level = day.xpath("./td[3]/div/text()").tract_first()
            # pm2_5 = day.xpath("./td[4]/text()").extract_first()
            # pm10 = day.xpath("./td[5]/text()").extract_first()
            # so2 = day.xpath("./td[6]/text()").extract_first()
            # co = day.xpath("./td[7]/text()").extract_first()
            # no2 = day.xpath("./td[8]/text()").extract_first()
            # o3 = day.xpath("./td[9]/text()").extract_first()
            # rank = day.xpath("./td[10]/text()").extract_first()

            item['date'] = day.xpath("./td[1]/text()").extract_first() if not "" else "0"
            item['aqi'] = day.xpath("./td[2]/text()").extract_first() if not "" else "0"
            item['level'] = day.xpath("./td[3]/div/text()").extract_first() if not "" else "0"
            item['pm2_5'] = day.xpath("./td[4]/text()").extract_first() if not "" else "0"
            item['pm10'] = day.xpath("./td[5]/text()").extract_first() if not "" else "0"
            item['so2'] = day.xpath("./td[6]/text()").extract_first() if not "" else "0"
            item['co'] = day.xpath("./td[7]/text()").extract_first() if not "" else "0"
            item['no2'] = day.xpath("./td[8]/text()").extract_first() if not "" else "0"
            item['o3'] = day.xpath("./td[9]/text()").extract_first() if not "" else "0"
            item['rank'] = day.xpath("./td[10]/text()").extract_first() if not "" else "0"

            yield item







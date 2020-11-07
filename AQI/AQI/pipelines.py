# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import redis
import pymongo
from scrapy.exporters import CsvItemExporter

class AqiJsonPipeline(object):
    def open_spider(self, spider):
        self.f = open("aqi.json", "w")

    def process_item(self, item, spider):
        item["spider"] = spider.name
        content = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()


class AqiCSVPipeline(object):
    def open_spider(self, spider):
        # 创建csv文件对象，拥有写权限
        self.csv = open("aqi.csv", "w")
        # 查创建一个Csv文件读写对象，参数是csv文件对象
        self.csvexporter = CsvItemExporter(self.csv)
        # 指定读写权限，可以开始写入数据
        self.csvexporter.start_exporting()

    def process_item(self, item, spider):
        # 将item数据写入到csv文件里
        self.csvexporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表述数据写入结束
        self.csvexporter.finish_exporting()
        self.csv.close()

class AqiRedisPipeline(object):
    def open_spider(self, spider):
        # 创建Redis数据库连接对象
        self.redis_cli = redis.Redis(host = "127.0.0.1", port = 6379)

    def process_item(self, item, spider):
        # 将item转换成json格式
        content = json.dumps(dict(item), ensure_ascii = False)
        # 将数据写入到list里，key AQI， value content
        self.redis_cli.lpush("AQI", content)
        return item

class AqiMongoPipeline(object):
    def open_spider(self, spider):
        # 创建MongoDb数据库链接对象
        self.mongo_cli = pymongo.MongoClient(host = "127.0.0.1", port = 27017)
        # 创建MongoDB的数据库
        self.dbname = self.mongo_cli["AQI"]
        # 创建数据库的表
        self.sheet = self.dbname["AQI_data"]

    def process_item(self, item, spider):
        # 将数据插入到表里
        self.sheet.insert(dict(item))
        return item













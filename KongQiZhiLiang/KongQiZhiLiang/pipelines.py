# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import redis
import pymongo
from scrapy.exporters import CsvItemExporter

#class KongqizhiliangPipeline(object):
#    def process_item(self, item, spider):
#        return item

class AqiJsonPip(object):
    def open_spider(self, spider):
        self.f = open("aqi.json", "w")

    def process_item(self, item, spider):
        item["spider"] = spider.name
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.f.close()


class AqiCSVPip(object):
    def open_spider(self, spider):
        self.csv = open("aqi.csv", "w")
        self.csvexporter = CsvItemExporter(self.csv)
        self.csvexporter.start_exporting()

    def process_item(self, item, spider):
        self.csvexporter.export_item(item)
        return item

    def close_spider(self, spider):
        slef.csvexporter.finish_exporting()
        self.f.close()

class AqiRedisPip(object):
    def open_spider(self, spider):
        self.redis_cli = redis.Redis(host="127.0.0.1", port=6379)

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.redis_cli.lpush("AQI", content)
        return item

class AqiMongoPip(object):
    def open_spider(self, spider):
        self.mongo_cli = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.dbname = self.mongo_cli["AQI"]
        self.sheet = self.dbname["AQI_data"]

    def process_item(self, item, spider):
        self.sheet.insert(dict(item))
        return item

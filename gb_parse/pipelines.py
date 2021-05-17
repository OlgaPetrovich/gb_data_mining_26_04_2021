# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from . import settings
from pymongo import MongoClient


class GbParsePipeline:
    def process_item(self, item, spider):
        return item


class GbMongoPipeLine:

    def __init__(self):
        client = MongoClient()
        self.db = client[settings.BOT_NAME]

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(item)
        return item
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import engine, Repository


class ShiyanlouPipeline(object):
    def process_item(self, item, spider):
        s = item['update_time'].split('T')[0] + ' ' + item['update_time'].split('T')[1][:-1]
        item['update_time'] = datetime.strptime(s, '%Y-%m-%d %H:%M:%S') 
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

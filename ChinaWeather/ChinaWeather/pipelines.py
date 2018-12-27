# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import redis
from scrapy.exceptions import DropItem


class ChinaweatherPipeline(object):
    def process_item(self, item, spider):
        return item

class RedisPipeline(object):
    def open_spider(self, spider):
        # 需要修改
        self.r = redis.StrictRedis(host='www.fand.wang',port=6379,password='fanding',db=8)


    # def close_spider(self, spider):
    #     self.r.close()


    def process_item(self, item, spider):
        # 此处的name需要修改
        if self.r.sadd(spider.name, item['code']):
            return item
        raise DropItem


class MysqlPipeline(object):
    def open_spider(self, spider):
        # 此处需要修改
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='CHINA_WEATHER',
            user='root',
            password='102487',
            charset='utf8mb4',
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        keys = item.keys()
        values = [item[k] for k in keys]
        # keys, values = zip(*item.items())
        sql = "insert into `{}` ({}) values ({}) " \
              "ON DUPLICATE KEY UPDATE {}".format(
            item.table_name,
            ','.join(keys),
            ','.join(['%s'] * len(values)),
            ','.join(['`{}`=%s'.format(k) for k in keys])
        )
        self.cur.execute(sql, values * 2)
        self.conn.commit()
        print(self.cur._last_executed)
        return item


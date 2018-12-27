# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaweatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WeatherCase(scrapy.Item):
    table_name = 'weather'
    code = scrapy.Field()
    name = scrapy.Field()
    alins = scrapy.Field()
    als = scrapy.Field()
    date = scrapy.Field()
    hmax = scrapy.Field()
    hmin = scrapy.Field()
    nl = scrapy.Field()
    nlyf = scrapy.Field()
    hgl = scrapy.Field()


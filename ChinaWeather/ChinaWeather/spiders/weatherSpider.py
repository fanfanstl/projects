# -*- coding: utf-8 -*-
import json
import scrapy
import time


from ChinaWeather.items import WeatherCase
from ChinaWeather.spiders.tils import get_str, create_city_code


class WeatherspiderSpider(scrapy.Spider):
    name = 'weatherSpider'
    allowed_domains = ['d1.weather.com.cn','www.weather.com.cn', 'toy1.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/']


    def parse(self, response):
        headers = {
            # 'Accept': "*/*",
            # 'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Connection': "keep-alive",
            # 'Cookie': "vjuids=-769777dbc.1674b3d52f8.0.55c07f6ae1a64; vjlast=1543155569.1543155569.30; UM_distinctid=1674b3d53de1c-015b0420c8728f-4313362-144000-1674b3d53df2e8; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1543155570; f_city=%E5%A4%A9%E6%B4%A5%7C101030100%7C; Wa_lvt_1=1543155570; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1543155649; Wa_lpvt_1=1543155650",
            'Host': "d1.weather.com.cn",
            'Referer': "http://www.weather.com.cn/weather40d/101010100.shtml",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            'Cache-Control': "no-cache",
        }

        url_17 = 'http://d1.weather.com.cn/calendar_new/2017/%s_2017%s.html?_=%s'
        url_18 = 'http://d1.weather.com.cn/calendar_new/2018/%s_2018%s.html?_=%s'

        # 获取城市code，和城市名称
        city_code = create_city_code()
        for item in city_code:
            for j in range(1, 13):
                num = get_str(j)
                tim = str(int(time.time()*1000))

                code = list(item.keys())[0]
                url_2017 = url_17 % (code, num,tim)
                url_2018 = url_18 % (code, num,tim)

                yield response.follow(url=url_2017,headers=headers,callback=self.data_parse,meta={'code':code,'name':item[code]})
                yield response.follow(url=url_2018,headers=headers,callback=self.data_parse,meta={'code':code,'name':item[code]})
                # print("&"*40)

    def data_parse(self, response):
        case_item = WeatherCase()
        data_list = json.loads(response.text[11:])
        # print(type(data_list),'*'*50)
        # print(data_list)
        print(response.meta.get('code'),"*"*100)
        for item in data_list:
            case_item['code'] = response.meta.get('code')
            case_item['name'] = response.meta.get('name')
            case_item['alins'] = item.get('alins')
            case_item['als'] = item.get('als')
            case_item['date'] = item.get('date')
            case_item['hmax'] = item.get('hmax')
            case_item['hmin'] = item.get('hmin')
            case_item['nl'] = item.get('nl')
            case_item['hgl'] = item.get('hgl')
            case_item['nlyf'] = item.get('nlyf')
            yield case_item


import random

import redis
from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):

    def __init__(self, settings):
        # 2. 初始化配置及相关变量
        self.r = redis.StrictRedis(host='www.fand.wang',port=6379,password="fanding",db=10)
        self.proxy_key = settings.get('PROXY_REDIS_KEY')
        self.proxy_stats_key = self.proxy_key + '_stats'
        self.max_failed = 3

    @property
    def proxies(self):
        return [i.decode('utf-8') for i in self.r.lrange(self.proxy_key, 0, -1)]

    @classmethod
    def from_crawler(cls, crawler):
        # 1. 创建中间件对象
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured

        return cls(crawler.settings)

    def process_request(self, request, spider):
        # 3. 为每个request对象分配一个随机的IP代理
        print(self.proxies,"*"*20)
        if self.proxies and not request.meta.get('proxy') \
                and request.url not in spider.start_urls:
            print('use %s as current proxy' % request.meta['proxy'])

    def process_response(self, request, response, spider):
        # 4. 请求成功则调用process_response
        cur_proxy = request.meta.get('proxy')
        # 判断是否被对方封禁
        if response.status in (401, 403, 404):
            # 给相应的IP失败次数+1
            # self.stats[cur_proxy] += 1
            self.r.hincrby(self.proxy_stats_key, cur_proxy, 1)
            print('%s got wrong code %s times' % (cur_proxy, self.stats[cur_proxy]))
        # 当某个IP的失败次数累计到一定数量
        failed_times = self.r.hget(self.proxy_stats_key, cur_proxy) or 0
        if int(failed_times) >= self.max_failed:
            print('got wrong http code (%s) when use %s' \
                  % (response.status, cur_proxy))
            # 可以认为该IP被对方封禁了，从代理池中将该IP删除
            self.remove_proxy(cur_proxy)
            del request.meta['proxy']
            # 将该请求重新安排调度下载
            return request
        return response

    def process_exception(self, request, exception, spider):
        # 4. 请求失败则调用process_exception
        cur_proxy = request.meta.get('proxy')
        # 如果本次请求使用了代理，并且网络请求报错，认为该IP出现问题了
        if cur_proxy and isinstance(exception, (ConnectionRefusedError, TimeoutError)):
            print('error (%s) occur when use proxy %s' % (exception, cur_proxy))
            self.remove_proxy(cur_proxy)
            del request.meta['proxy']
            return request

    def remove_proxy(self, proxy):
        print('starting remove proxy: %s' % proxy)
        if proxy in self.proxies:
            self.r.lrem(self.proxy_key, proxy)
            self.r.hdel(self.proxy_stats_key, proxy)
            print('remove %s from proxy list' % proxy)
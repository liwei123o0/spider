# -*- coding: utf-8 -*-

# Scrapy settings for webbot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'webbot'

SPIDER_MODULES = ['webbot.spiders']
NEWSPIDER_MODULE = 'webbot.spiders'


USER_AGENT = 'Mozilla/5.0 (w3660t by Kev++)'

#代理中间件的添加
DOWNLOADER_MIDDLEWARES = {
            'ssfeng.randomproxy.RandomProxy': 100,
            'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
        }
#重试因代理错误爬取连接
RETRY_TIMES = 10
#重试的错误类型包括这些
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#代理地址
PROXY_LIST = '/path/to/proxy/list.txt'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webbot (+http://www.yourdomain.com)'

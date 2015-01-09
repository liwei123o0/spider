# -*- coding: utf-8 -*-
import scrapy
import json
from webbot.items import DmozItem
from webbot.items import WebbotItem
class TiebaSpider(scrapy.Spider):
    name='tieba'
    allowed_domains =['baidu.com']
    start_urls=['http://tieba.baidu.com/p/3515571358']

    def parse(self, response):
        loop=response.xpath('//div[contains(@class,"l_post l_post_")]')

        num=0
        for site in loop:
            item= WebbotItem()
            item['at']=site.xpath('//a[@class="p_author_name j_user_card"]/text()').extract()
            item['conten'] = site.xpath('//div[@class="p_content p_content_nameplate"]').extract()
            num+=1
            print ('#####################%s################################'%num)
            yield item


# class DmozSpider(scrapy.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = [
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
#         "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
#     ]
#
#     def parse(self, response):
#         num=0
#         for sel in response.xpath('//ul/li'):
#             item = DmozItem()
#             item['title'] = sel.xpath('a/text()').extract()
#             item['link'] = sel.xpath('a/@href').extract()
#             item['desc'] = sel.xpath('text()').extract()
#             num+=1
#             print('#####################%s################################'%num)
#             yield item

# -*- coding: utf-8 -*-
import scrapy
from webbot.items import WebbotItem

class TiebaSpider(scrapy.Spider):
    name='tieba'
    allowed_domains =['baidu.com']
    start_urls=['http://tieba.baidu.com/p/3515571358']

    def parse(self, response):
        # sel=scrapy.Selector(response,text='utf-8',type='html')
        loop=response.xpath('//div[contains(@class,"l_post l_post_")]')

        num=0
        for site in loop:
            item= WebbotItem()
            item['at']=site.xpath('//a[@class="p_author_name j_user_card"]/text()').extract()
            item['conten'] = site.xpath('//div[@class="p_content p_content_nameplate"]').extract()
            num+=1
            print ('#####################%s################################'%num)
            yield item
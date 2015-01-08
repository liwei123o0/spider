# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from
class TiebaSpider(scrapy.Spider):
    name='tieba'
    allowed_domains =['baidu.com']
    start_name=['http://tieba.baidu.com/f?kw=it&ie=utf-8']

    def parse(self, response):
        hxs =HtmlXPathSelector(response)
        sites = hxs.path('//li[@class="j_thread_list clearfix"]')
        items =[]
        for site in sites:
            item=WebbotItem()
            item['id']=site.path('.//div[@class="threadlist_rep_num"]/text()').extract()
            item['name'] = site.path('.//a[@class="j_th_tit"]')
            items.append(item)
        return items

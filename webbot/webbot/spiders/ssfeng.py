# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.selector import HtmlXPathSelector
from webbot.items import DoubanItem
import re

'根据xpath规则从列表页爬取新浪论坛的内容'

class TiebaSpider(CrawlSpider):
    name='ssfeng'
    allowed_domains =['ssfeng.com']
    start_urls=['http://bbs.ssfeng.com/bbs/']
    rules = [
        Rule(sle(restrict_xpaths=("//h2/a")),follow=True), #提取网页URL连接并进行跟进处理页面信息
        Rule(sle(restrict_xpaths=("//span[contains(@id,'thread')]/a")),callback='parse_item'), #纠结很久的问题，不能跟进采集原因是不能写parse函数，需要改名字
    ]
    def parse_item(self, response):
        hxs=HtmlXPathSelector(response)
        # items=[]
        item= DoubanItem()
        item['title']="".join(hxs.xpath("//h1/text()").extract())
        item['autho']="".join(hxs.xpath("(//div[@class='postinfo']/a/text())[1]").extract())
        item['date']="".join(hxs.xpath("(//div[@class='authorinfo']/em/text())[1]").extract())
        item['conten'] ="".join(hxs.xpath("(//td[@class='t_msgfont'])[1]/text()").extract())
        item['url']=response.url
        print('url:'+item['url'])
        print('title:'+item['title']).encode('gb2312')
        print('autho:'+item['autho']).encode('gb2312')
        print('date:'+item['date']).encode('gb2312')
        print('conten:'+item['conten']).encode('gb2312')

        # return item


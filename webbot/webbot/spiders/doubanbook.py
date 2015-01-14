# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.selector import HtmlXPathSelector

from webbot.items import DoubanItem
'根据xpath规则从列表页爬取新浪论坛的内容'

class TiebaSpider(CrawlSpider):
    name='sina'
    allowed_domains =['sina.com.cn']
    start_urls=['http://bbs.sina.com.cn/']
    rules = [
        Rule(sle(restrict_xpaths=("(//dl[@class='ws_list02 clearfix']//li[1]/a)[3]")),follow=True), #提取网页URL连接并进行跟进处理页面信息
        Rule(sle(restrict_xpaths=("//th[@class='new']/span/a")),callback='parse_item'), #纠结很久的问题，不能跟进采集原因是不能写parse函数，需要改名字
    ]
    def parse_item(self, response):
        hxs=HtmlXPathSelector(response)
        # items=[]
        item= DoubanItem()
        item['title']=hxs.xpath("//h1/text()").extract()
        item['autho']=hxs.xpath("(//a[@class='dropmenu'])[1]/text()").extract()
        item['date']=hxs.xpath("(//div[@class='postinfo'])[1]/text()").extract()
        item['conten'] =hxs.xpath("(//div[@class='t_msgfont'])[1]//text()").extract()
        # yield item
        # item['url']=response.url
        print repr(item['conten']).decode("unicode-escape",errors='ignore')
        # items.append(item)
        # print ('#####################%s################################'%num)
        #将爬取到的结果输出中文，unicode-escape反编译后得到其对应的汉字。


        # loop=sel.response.xpath('(//table[@class="tagCol"]//td/a)[1]')
        #
        # num=0
        # for site in loop:
        #     item= DoubanItem()
        #     item['title']=site.xpath("./h2/a").extract()
        #     item['autho']=site.xpath(".//div[@class='pub']/text()").extract()
        #     item['pingjia']=site.xpath(".//span[@class='pl']/text()").extract()
        #     item['conten'] = site.xpath(".//p").extract()
        #     item['jiage'] = site.xpath(".//span[@class='buy-info']/a/text()").extract()
        #     num+=1
        #     print ('#####################%s################################'%num)
        #     #将爬取到的结果输出中文，unicode-escape反编译后得到其对应的汉字。
        #     print repr(item).decode("unicode-escape") + '\n'
            # yield item

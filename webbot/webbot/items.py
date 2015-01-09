# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field
'items用于存储scrapy抓取到的数据，以及定义数据字段'
class WebbotItem(Item):
    # define the fields for your item here like:
    at = Field()
    conten = Field()


class DmozItem(Item):
    # define the fields for your item here like:
    title = Field()
    link = Field()
    desc = Field()
#
# '创建item并将所存储数据以两种方式打印出来'
# webbot =WebbotItem(name='牛奶吧',id=1)
# print(webbot)
# print(webbot).get('name')
# print(webbot['id'])
#
# '获取字段值'
# print webbot.get('title','标题')
# '获取所有获取到的值'
# print(webbot.keys())
# print(webbot.items())
#
# '''
# 扩展items可以通过继承item来扩展item
# 添加和修改原始item的字段
# '''
# class newsItem(WebbotItem):
#     title =scrapy.Field()
#     url = scrapy.Field()

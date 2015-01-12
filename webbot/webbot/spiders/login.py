# -*- coding: utf-8 -*-

import scrapy
from webbot.items import LoginItem
class LoginSpider(scrapy.Spider):
    name = 'csdn'
    start_urls = ['https://passport.csdn.net/account/login?ref=toolbar']

    def parse(self, response):
        a=scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'liwei123o0', 'password': 'liwei429'},
            callback=self.after_login
        )
        loop=a.response.xpath('//div[@class="box flow"]//li')
        num=0
        for site in loop:
            item= LoginItem()
            item['url']=site.xpath('.//a/@href').extract()
            num+=1
            print ('#####################%s################################'%num)
            yield item

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return

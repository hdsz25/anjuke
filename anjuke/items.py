# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Anjuke(scrapy.Item):
    addr1=scrapy.Field()
    addr2=scrapy.Field()
    addr3=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    price=scrapy.Field()
    pub_date=scrapy.Field()
    xiaoqu=scrapy.Field()
    year=scrapy.Field()
    fuxin=scrapy.Field()
    mianji=scrapy.Field()
    louchen=scrapy.Field()
    danjia=scrapy.Field()
    zhuanxiu=scrapy.Field()


    

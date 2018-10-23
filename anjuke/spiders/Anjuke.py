# -*- coding: utf-8 -*-
import scrapy
from anjuke.items import Anjuke
import re
import os
# 设置相应的代理用户名密码，主机和端口号
# os.environ["http_proxy"] = "http://user:password@proxy.internal.server.com:8080"
os.environ["http_proxy"] = "http://127.0.0.1:8087"
class AnjukeSpider(scrapy.Spider):
    name = 'Anjuke'
    start_urls =['https://yangzhou.anjuke.com/sale/?from=navigation']
    #headers可以在settings.py中设定后就不用在这个设定并且在每个爬取时加上headers。
    # allowed_domains = ['https://yangzhou.anjuke.com']
    # def start_requests(self):
    #     urls = ['https://yangzhou.anjuke.com/sale/?from=navigation']
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)
    #         # yield scrapy.Request(url=url, headers=self.headers,callback=self.parse)
    def parse(self, response):
        for li in response.xpath('//*[@id="houselist-mod-new"]/li'):
            items=Anjuke()
            items["title"]=li.xpath('./div[2]/div[1]/a/text()')[0].extract().strip()
            items['url']=li.xpath('./div[2]/div[1]/a/@href')[0].extract()
            items['price'] = li.xpath('./div[3]/span[1]/strong/text()')[0].extract()
            # items['pub_date'] =self.parse_date(items['url'])
            yield scrapy.Request(items['url'],callback=self.parse_date,meta={'key':items})
            # response.meta只能传递字典，因为meta本身也是字典，如果直接用meta=items，会带入很多程序运行参数到新赋值的items中。
            # yield items
        next_url = response.xpath('//a[@class="aNxt"]/@href').extract()
        if next_url:
            # next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield response.follow(next_url[0],callback=self.parse)#用response.follow代替request可以不用完整url。
    def parse_date(self,response):
        items=response.meta['key']
        items['addr1'] =response.xpath('//p[@class="loc-text"]/a[1]/text()').extract()[0]
        items['addr2'] =response.xpath('//p[@class="loc-text"]/a[2]/text()').extract()[0]
        items['addr3'] =response.xpath('//p[@class="loc-text"]/text()')[1].re('－\s*(\S*)')[0]
        items['pub_date'] = re.findall(u'\d{4}年\d\d月\d\d日',response.xpath('//span[@class="house-encode"]/text()').extract_first())[0]
        items['xiaoqu']=response.xpath('//div[@class="houseInfo-content"]/a/text()').extract_first()
        items['year']=response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[7]/div[2]/text()').extract_first()
        items['fuxin']=re.sub("[\s]","",response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[2]/div[2]/text()').extract_first())
        items['mianji']=response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[5]/div[2]/text()').extract_first()
        items['louchen']=re.sub('[\s]', "", response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[11]/div[2]/text()').extract_first())
        items['danjia']=response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[3]/div[2]/text()').extract_first()
        items['zhuanxiu']=response.xpath('//ul[@class="houseInfo-detail-list clearfix"]/li[12]/div[2]/text()').extract_first()
        yield items
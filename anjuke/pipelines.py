# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import re
import datetime
today=str(datetime.date.today()).replace('-','')

class AnjukePipeline(object):
    def __init__(self):
        self.f=open('扬州二手房价%s.csv'%today,'w', newline="",encoding='utf-8')
        self.writer=csv.writer(self.f)
        self.writer.writerow([u'标题',u'小区',u'年限',u'户型',u'面积',u'楼层',\
                              u'单价',u'装修',u'总价',\
                              u'地址1',u'地址2',u'地址3',u'发布日期','url'])
    def process_item(self, item, spider):
        item['year']=re.sub('[^\d]','',item['year'])
        item['danjia']=float(item['danjia'][:-4])
        item['mianji']=float(item['mianji'][:-3])

        self.writer.writerow((item['title'],item['xiaoqu'],item['year'],item['fuxin'],item['mianji'],item['louchen'],\
                              item['danjia'],item['zhuanxiu'],item['price'],\
                              item['addr1'],item['addr2'],item['addr3'],item['pub_date'],item['url']))
        return item
    def close_spider(self,spider):
        self.f.close()



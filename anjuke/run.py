# -*- coding: utf-8 -*-
# @Time     : 2017/1/1 17:51
# @Author   : woodenrobot


from scrapy import cmdline

name = 'Anjuke'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
# print(cmd.split())
# with open("h1.csv","rb") as f:
#     with open("h1_fix.csv","w") as f2:
#         f2.write(f.read().decode().replace("\r","")) # python 3
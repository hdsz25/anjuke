# -*- coding: utf-8 -*-

# Scrapy settings for anjuke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'anjuke'

SPIDER_MODULES = ['anjuke.spiders']
NEWSPIDER_MODULE = 'anjuke.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'anjuke (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     ":authority": "yangzhou.anjuke.com",
#     ":method": "GET",
#     ":path": "/ajax/aifang/tuangou/api/?num=5&cityId=72&adCode=SaleListing",
#     ":scheme": "https",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, sdch, br",
#     "accept-language": "zh-CN,zh;q=0.8",
#     "cookie": "als=0; ajk_member_name=%E6%89%8B%E6%9C%BA1971525324145; ajk_member_key=7ed37609c45e6b361efbd4febf54caaa; ajk_member_time=1556860140; aQQ_ajkauthinfos=K1vp9eYNafWQNcJdiN6zmvdRWJ4v7XnUxTE9BBEWNZ80wqezfKuV5S5OcmJus0hKZ4MiXDtmnTpHMGk6JUq7hAUmOAccZZ5WhNLP; lui=65617167%3A1; isp=true; ctid=72; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1525156114,1525186942,1525325430,1526130405; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttps%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26ie%3DUTF-8; sessid=593D7610-B6FB-BE0C-D045-DE3E9CA640A2; __ctd8857029538414931=1; __xsptplus8=8.15.1528177048.1528177048.1%233%7C%20https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26ie%3DUTF-8%7C%7C%7C%7C%23%23%23; ajk_member_id=65617167; ajk_member_captcha=c845c96ce7c6473a454b1b33907d270f; browse_comm_ids=1001769%7C940180%7C996342%7C815747%7C999162; propertys=kl0ps3-p9u93j_kwhd9t-p9u5p3_; _gat=1; __xsptplusUT_8=1; _ga=GA1.2.825203072.1525096499; _gid=GA1.2.1089178315.1528177136; __xsptplus8=8.16.1528185243.1528185243.1%233%7C%20https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26ie%3DUTF-8%7C%7C%7C%7C%23%23tUrVeuhfwUj5JTXt0-Ypj_bFo48Mzhdy%23; 58tj_uuid=5cf29120-2a3e-467b-8580-3e817901eb23; new_session=0; init_refer=https%253A%252F%252Fwww.baidu.com%252Fs%253Fwd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526ie%253DUTF-8; new_uv=17; aQQ_ajkguid=DC14E0A0-CA06-596B-E4DB-0DE7E426866E; twe=2",
#     "referer": "https://yangzhou.anjuke.com/sale/?from=navigation",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
#     "x-requested-with": "XMLHttpRequest"
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'anjuke.middlewares.AnjukeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'anjuke.middlewares.AnjukeDownloaderMiddleware': 543,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    'random_agents.RotateUserAgentMiddleware':400
}
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'anjuke.pipelines.AnjukePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

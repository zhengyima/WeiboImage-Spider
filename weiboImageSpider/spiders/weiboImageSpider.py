import scrapy

import random

from ..items import WeiboimagespiderItem

class weiboImageSpider(scrapy.Spider):

    name = "weiboImage"

    root_url = ["https://wx1.sinaimg.cn/mw690/","https://wx2.sinaimg.cn/mw690/","https://wx3.sinaimg.cn/mw690/","https://wx4.sinaimg.cn/mw690/"]

    tsvPath = "/home/dou/weiboSolrCrawler/imgs0603.tsv"

    imgIndex = 0

    start_urls = ["http://183.174.228.17:1241"]
    

    # def __init__(self):
    #     f = open(self.tsvPath,"r")
    #     lines = f.readlines()
    #     self.tsvLines = lines

    # start_urls = 
    def parse(self, response):

        # f = open(tsvPath,"r")
        # lines = f.readlines()
        f = open(self.tsvPath,"r")
        line = f.readline()

        while line: 
            # line = self.tsvLines[imgIndex]
            url, Id, text, imgKey, nickName, avatarUrl, uid = line.split("\t")
            imgKey = imgKey.replace("\n","")
            wxId = random.randint(0,3)
            imgUrl = self.root_url[wxId] + imgKey + ".jpg"

            item = WeiboimagespiderItem()
            # item['src'] = imgUrl
            item["images_urls"] = [imgUrl]
            item["image_urls"] = [imgUrl]
            item["url"] = url
            item["Id"] = Id
            item["Text"] = text
            item["nickName"] = nickName
            item["avatarUrl"] = avatarUrl
            item["uid"] = uid

            line = f.readline()
            yield item

        # for line in self.tsvLines:

        #     # line = self.tsvLines[imgIndex]
        #     url, Id, text, imgKey = line.split("\t")
        #     imgKey = imgKey.replace("\n","")
        #     wxId = random.randint(0,3)
        #     imgUrl = self.root_url[wxId] + imgKey + ".jpg"

        #     item = WeiboimagespiderItem()
        #     # item['src'] = imgUrl
        #     item["images_urls"] = [imgUrl]
        #     item["image_urls"] = [imgUrl]
        #     item["url"] = url
        #     item["Id"] = Id
        #     yield item

        #     # return {}

             



            
            
        

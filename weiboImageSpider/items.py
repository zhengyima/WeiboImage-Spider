# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboimagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # src = scrapy.Field()
    images_urls  = scrapy.Field()
    image_urls  = scrapy.Field()
    url = scrapy.Field()
    Id = scrapy.Field()
    Text = scrapy.Field()
    nickName = scrapy.Field()
    avatarUrl = scrapy.Field()
    uid = scrapy.Field()
    
    pass

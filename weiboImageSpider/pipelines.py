# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class WeiboimagespiderPipeline(ImagesPipeline):

    # def process_item(self, item, spider):

    #     # print(item)
    #     print("test1")
    #     return item

    # def get_media_requests(self, item, info):

    #     print("test2")
    #     request_objs = super(WeiboimagespiderPipeline,self).get_media_requests(item,info)
    #     for r_obj in request_objs:
    #         r_obj.item = item
        

    #     print("test2\n\n\n\n\n\n\n\n")
    #     return request_objs
    #     # print(item)
    #     # print("test2")
    #     # yield scrapy.Request(url=item['src'])
    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]

        # print(results)
        # try:
        for p in image_paths:

            f = open("/home/dou/weiboImageSpider2/img0603big.txt","a+")
            f.write(p + "\t" + item["Id"] + '\t' + item["url"] + '\t' +  item["images_urls"][0] + '\t' + item["Text"] +'\t'+ item["nickName"] + '\t'+ item["avatarUrl"] +'\t' + item["uid"] +  '\n' )
            f.close()
        # except:
        #     print("error!\n")

                
        if not image_paths:
            raise DropItem("Item contains no images")
        
        item["images_urls"] = image_paths

        return item

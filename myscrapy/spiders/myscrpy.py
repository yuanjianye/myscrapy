import scrapy
# -*- coding:utf-8 -*-  

#class myscrapy(scrapy.Spider):
    #name = "myscrapy"
    #allowed_domains = ["*"]
    #start_url = ["http://news.sina.com.cn/"]
    ##start_url = ["http://www.yuanjianye.com"]

    #def parse(self,response):
        #print response.body
        ##for sel in response.xpath('//ul/li'):
            ##title=sel.xpath('a/text()').extract()
        ##    print title
        ##print response
        ##filename=response.url.split("/")[-2]
        ##with open(filename,'wb') as f:
        ##    f.write(response.body)
        
import scrapy

class MyScrapySpider(scrapy.Spider):
    name = "myscrapy"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://news.sina.com.cn"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
#            print title, link, desc
            for i in title:
                print i

# -*- coding: utf-8 -*-
import scrapy
import csv

class YellowSpider(scrapy.Spider):
    name = "yellow"
    allowed_domains = ["yell.com"]
    start_urls = [
        'https://www.yell.com/ucs/UcsSearchAction.do?keywords=restaurants&location=United+Kingdom&pageNum=1',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=2',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=3',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=4',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=5',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=6',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=7',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=8',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=9',
        'https://www.yell.com/ucs/UcsSearchAction.do?location=United+Kingdom&keywords=restaurants&pageNum=10'
    ]
    filehandle4 = open('Rest.tsv','w')
    filehandle4.write("Name_of_Business\tTelephone\tStreet\tLocality\tPostcode\tRegion\tWebsite\n")    

    def parse(self, response):

        for i in range(0,15):
            elements = response.xpath('//div[@class="col-sm-24 businessCapsule businessCapsule-standard js-LocalBusiness"]')
            sample = elements[0]                        
            if True:
                url = None
                try:
                    if i == 0:
                        url = sample.xpath('//div[@class="businessCapsule--callToAction"]//a')[1].xpath('@href').extract()[0]
                    else:
                        url = sample.xpath('//div[@class="businessCapsule--callToAction"]//a')[(i-1)*3+1].xpath('@href').extract()[0]
                except:
                    pass
                try:
                    name = sample.xpath('//div[@class="col-sm-20"]/a/h2')[i].xpath('text()').extract()[0]
                except:
                    continue
                try:
                    telephone = sample.xpath('//div[@class="col-sm-12 col-md-11 col-lg-11 businessCapsule--telephone"]//strong[@class="businessCapsule--tel"]//text()')[i].extract()
                except:
                    telephone = ''

                try:
                    street = sample.xpath('//div[@class="col-sm-10 col-md-11 col-lg-12 businessCapsule--address"]//span[@itemprop="streetAddress"]//text()')[i].extract()
                except:
                    street = ''

                try:
                    locality = sample.xpath('//div[@class="col-sm-10 col-md-11 col-lg-12 businessCapsule--address"]//span[@itemprop="addressLocality"]//text()')[i].extract()
                except:
                    locality = ''

                try:
                    postcode = sample.xpath('//div[@class="col-sm-10 col-md-11 col-lg-12 businessCapsule--address"]//span[@itemprop="postalCode"]//text()')[i].extract()
                except:
                    postcode = ''

                try:
                    region = sample.xpath('//div[@class="col-sm-10 col-md-11 col-lg-12 businessCapsule--address"]//span[@itemprop="addressRegion"]//text()')[i].extract()
                except:
                    region = ''

                self.filehandle4.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(name,telephone,street,locality, postcode, region, url))


# -*- coding: utf-8 -*-
import scrapy


class CigabuySpiderSpider(scrapy.Spider):
    name = 'cigabuy_spider'
    allowed_domains = ['www.cigabuy.com']
    

    def start_requests(self):
        yield scrapy.Request(url = "https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html",callback=self.parse, headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36"
            })
        


    def parse(self, response):
        products = response.xpath("//div[@class='p_box_wrapper']")
        for product in products:
            title = product.xpath(".//div/a[2]/text()").get()
            url = product.xpath(".//a[2]/@href").get()
            orginal_price = product.xpath(".//div[@class='p_box_price cf']/span[2]/text()").get()
            discounted_price = product.xpath(".//div[@class='p_box_price cf']/span[1]/text()").get()

            yield {

                "Title":title,
                "URL":url,
                "Original Price": orginal_price,
                "Discounted_Price":discounted_price,
                "User-Agent": response.request.headers["User-Agent"]
            }

        next_page = response.xpath("(//a[@class='nextPage'])[2]/@href").get()

        if next_page:
            yield scrapy.Request(url= next_page, callback=self.parse, headers={
            "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36"
            })

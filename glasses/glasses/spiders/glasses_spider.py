# -*- coding: utf-8 -*-
import scrapy


class GlassesSpiderSpider(scrapy.Spider):
    name = 'glasses_spider'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div")

        for product in products:
            yield {
                "product_url": product.xpath(".//div[@class='product-img-outer']//a/@href").get(),
                "product_img_link": product.xpath(".//div[@class='product-img-outer']//img[1]/@src").get(),
                "product_name" : product.xpath(".//div[@class='p-title']/a/text()").get(),
                "product_price":product.xpath(".//span/text()").get()
                
            }
    


        next_page = response.xpath("//ul[@class='pagination']//a[@rel='next']/@href").get()

        if next_page:
            yield scrapy.Request(url= next_page, callback= self.parse)

        

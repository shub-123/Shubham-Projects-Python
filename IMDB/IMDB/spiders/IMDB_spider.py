# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImdbSpiderSpider(CrawlSpider):
    name = 'IMDB_spider'
    allowed_domains = ['www.imdb.com'] 

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url="https://m.imdb.com/list/ls091520106", headers ={
            "User-Agent": self.user_agent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='lister-item mode-detail']/div/a[1]"), callback='parse_item', follow=True, process_request="set_user_agent"),
        
    )


    def set_user_agent(self, request, spider):
        request.headers["User-Agent"] = self.user_agent
        return request

    def parse_item(self, response):
        yield {

            "Movie Title": response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            "Movie Year":  response.xpath("//span[@id='titleYear']/a/text()").get(),
            "Movie Rating": response.xpath("(//div[@class='ratingValue']//span)[1]/text()").get(),
            "Movie Genre": response.xpath("//div[@class='subtext']/a/text()").get(),
            "Movie Director": response.xpath("(//div[@class='credit_summary_item'])[1]/a/text()").get(),
            "User-Agent": response.request.headers["User-Agent"]

        }
        

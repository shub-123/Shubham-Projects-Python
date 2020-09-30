# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpiderSpider(CrawlSpider):
    name = 'Books_Spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"


    def start_requests(self):
        yield scrapy.Request(url = 'http://books.toscrape.com', headers= {"User-Agent":self.user_agent})


    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article[@class="product_pod"]'), callback='parse_item', follow=True, process_request="set_user_agent"),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'),process_request="set_user_agent")
    )


    def set_user_agent(self, request):
        request.headers["User-Agent"] = self.user_agent
        return request


    def parse_item(self, response):
        yield {
            "Book_name":response.xpath(".//h3/a/@title").get(),
            "Book_Price":response.xpath(".//div[@class='product_price']/p/text()").get(),
            "User-Agent": response.request.headers["User-Agent"]
        }
        

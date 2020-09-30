# -*- coding: utf-8 -*-
import scrapy


class DebtSpiderSpider(scrapy.Spider):
    name = 'debt_spider'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table[@class='jsx-533923983 table table-striped tp-table-body']/tbody/tr")
        for row in rows:
            countryname = row.xpath(".//td[1]/a/text()").get()
            debt_ratio = row.xpath(".//td[2]/text()").get()
        
            yield {

                "Country_Name":countryname,   
                "Debit_Ratio":debt_ratio
            }




        

import scrapy
import re

class CollegesSpider(scrapy.Spider):
    name = "Colleges"

    def start_requests(self):
        urls = [
            'https://www.niche.com/colleges/search/best-colleges/',
            'https://www.niche.com/colleges/search/best-colleges/?page=2',
            'https://www.niche.com/colleges/search/best-colleges/?page=3',
            'https://www.niche.com/colleges/search/best-colleges/?page=4'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css():
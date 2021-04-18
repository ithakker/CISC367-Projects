import scrapy
import re


class CryptoSpider(scrapy.Spider):
    name = "crypto"

    def start_requests(self):
        url = "https://coinmarketcap.com/all/views/all/"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css("tbody tr"):
            yield {
                "Name": row.css("a.cmc-link:nth-child(2)::text").extract_first(),
                "Symbol": row.css("td.cmc-table__cell:nth-child(3) div::text").extract_first(),
                "Market Cap": row.css("td.cmc-table__cell:nth-child(4) p::text").extract_first(),
                "Price": row.css("td.cmc-table__cell:nth-child(5) a::text").extract_first(),
                "Circulating Supply": row.css("td.cmc-table__cell:nth-child(6) div::text").extract_first(),
                "Volume": row.css("td.cmc-table__cell:nth-child(7) a::text").extract_first()
            }



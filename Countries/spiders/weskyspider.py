import scrapy
from weskyscraper.items import WeskyscraperItem

class WeskyspiderSpider(scrapy.Spider):
    name = "weskyspider"
    allowed_domains = ["www.scrapethissite.com/"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        items_count = WeskyscraperItem()
        for i in range(0, 249):
            items_count['country_name'] = response.css('div.container h3::text').getall()[2*i+1].strip()
            items_count['capital'] = response.css('div.col-md-4.country div span.country-capital::text').getall()[i]
            items_count['population'] = response.css('div.col-md-4.country div span.country-population::text').getall()[i]
            items_count['Area'] = response.css('div.col-md-4.country div span.country-area::text').getall()[i]

            yield items_count

import scrapy


class GethjSpider(scrapy.Spider):
    name = 'gethj'
    allowed_domains = ['http://39.98.126.217/']
    start_urls = ['http://39.98.126.217/']

    def parse(self, response):
        pass


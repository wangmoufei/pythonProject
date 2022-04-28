import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org']
    # start_urls = ['https://httpbin.org/get']
    start_urls = ['https://httpbin.org/get?id=1', 'https://httpbin.org/get?id=2', 'https://httpbin.org/get?id=3']

    def parse(self, response):
        print('地址：', response.url)
        print('状态：', response.status)
        print(response.body.decode('utf-8'))


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl test".split()
    cmdline.execute(args)

import scrapy


class Wenku2Spider(scrapy.Spider):
    name = 'wenku2'
    allowed_domains = ['wenku.baidu.com']

    # start_urls = ['https://wenku.baidu.com/']
    # 重新父类方法，自行初始化get处理，并设置回调
    def start_requests(self):
        yield scrapy.Request('https://wenku.baidu.com/search?word=python&pn=1', self.parse2)
        yield scrapy.Request('https://wenku.baidu.com/search?word=python&pn=2', self.parse2)
        yield scrapy.Request('https://wenku.baidu.com/search?word=python&pn=3', self.parse2)

    def parse2(self, response):
        print("Hello Scrapy")
        print(response.url)
        print(response.status)
        alist = response.selector.css("dl dt a.tiaoquan")
        print(len(alist))
        for a in alist:
            print(a.css("::attr(title)").get())


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl wenku2".split()
    cmdline.execute(args)

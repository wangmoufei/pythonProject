import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=1']

    p = 0

    def parse(self, response):
        print("===============正在爬取第%d页=================" % (self.p+1))
        print("Hello Scrapy")
        # print(response.url)
        # print(response.status)
        alist = response.selector.css("dl dt a.tiaoquan")
        print(len(alist))
        for a in alist:
            print(a.css("::attr(title)").get())
        # 负责爬取下一页
        self.p += 1
        if self.p < 10:  # 如果p小于10就继续爬取否则停止
            next_url = '/search?word=python&pn=' + str(self.p + 1)
            url = response.urljoin(next_url)  # 构建绝对的url地址
            yield scrapy.Request(url=url, callback=self.parse)


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl wenku".split()
    cmdline.execute(args)

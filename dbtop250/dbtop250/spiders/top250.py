import scrapy
from dbtop250.items import Dbtop250Item


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250?start=0']
    start_urls = ['https://httpbin.org/get?show_env=1']  # 测试请求返回信息
    page = 1

    def parse(self, response):
        # print(response.url)
        # print(response.status)
        print(response.text)
        blist = response.selector.css("tr.item")
        i = 1
        for item in blist:
            book = Dbtop250Item()
            book['index'] = i + (self.page - 3) * 25
            book['title'] = item.css("div.pl2 a::attr(title)").get()
            book['image'] = item.css("a.nbg img::attr(src)").get()
            info = item.css("p.pl::text").get().split("/")  # 提取text使用/进行识别拆分列表
            book['author'] = ",".join(info[0:-3])  # 使用逗号进行分割
            book['publisher'] = info[-3]
            book['time'] = info[-2]
            book['price'] = info[-1]
            book['score'] = item.css("span.rating_nums::text").get()
            book['comments'] = item.css("span.pl::text").re_first("[0-9]+")  # 使用re进行数字提取
            i += 1
            print(book)
            if self.page <= 11:
                url = "https://book.douban.com/top250?start=" + str(self.page * 25)
                self.page += 1
                yield scrapy.Request(url=url, callback=self.parse)


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl top250".split()
    cmdline.execute(args)

# scrapy crawl wyy --nolog不输出日志
# scrapy crawl wyy默认输出日志到窗口
# scrapy crawl wyy -s LOG_FILE=all.log #日志输出到当前目录下

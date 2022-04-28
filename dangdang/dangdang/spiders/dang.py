import scrapy
from dangdang.items import DangdangItem  # 导入items中的DangdangItem类


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['https://search.dangdang.com/?medium=01&key1=python&category_path=01.00.00.00.00.00']

    def parse(self, response):
        # 获取所有图书信息
        print(response)
        dlist = response.selector.css("ul.bigimg li")
        for dd in dlist:
            item = DangdangItem()  # 实例化DangdangItem
            item['author'] = dd.xpath(".//p[@class='search_book_author']//span[1]/a[1]/text()").get()
            item['publish'] = dd.xpath(".//p[@class='search_book_author']//span[2]/text( )").get()
            item['comment'] = dd.css('p.search_star_line a.search_comment_num::text').get()
            item['pic'] = response.urljoin(dd.css("a.pic img::attr(data-original)").get())  # response.urljoin 拼接完整图片地址
            item['title'] = dd.css('a.pic img::attr(alt)').get()
            item['price'] = dd.css("span.search_now_price::text").get()
            item['image_urls'] = [item['pic']]
            # print(item)
            yield item


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl dang".split()
    cmdline.execute(args)

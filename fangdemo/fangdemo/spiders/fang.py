import scrapy
from fangdemo.items import FangdemoItem


class FangSpider(scrapy.Spider):
    name = 'fang'
    allowed_domains = ['fang.5i5j.com']
    start_urls = ['https://fang.5i5j.com/bj/loupan/']

    def parse(self, response):
        '''解析响应结果'''
        # print(response.url)
        # print(response.status)
        # print(response.css("title::text").extract_first())
        # 获取每个房源信息
        hlist = response.css("li.houst_ctn")
        # 遍历
        for vo in hlist:
            item = FangdemoItem()  # 实例化item
            item['title'] = vo.css("span.house_name::text").get()
            # item['address'] = vo.selector.re_first(r"<span>(.*?)</span>")
            item['price'] = vo.css("p.price::text").get()
            yield item
if __name__ == '__main__':
    from scrapy import cmdline
    args = "scrapy crawl fang".split()
    cmdline.execute(args)
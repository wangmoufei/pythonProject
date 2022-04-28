import csv
import json
import time

import scrapy

from wangyiy.items import WangyiyItem


class WyySpider(scrapy.Spider):
    name = 'wyy'
    allowed_domains = ['http://music.163.com']

    # start_time = time.time()
    # start_urls = ['http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(i)]
    def start_requests(self):
        # 重写start_requests方法
        for i in range(589536, 775392):
            # time.sleep(20)
            start_urls = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}'.format(i)
            print(start_urls)
            yield scrapy.Request(url=start_urls, callback=self.parse)
        # print(start_urls)
        # end_time = time.time()
        # print("程序耗时%f秒." % (end_time - start_time))

    def parse(self, response):
        item = WangyiyItem()
        comments_dict = json.loads(response.text)  # 读取获取的json格式文件
        comments_list = comments_dict.get('comments')
        for urlID in comments_list:
            userid = urlID.get('user').get('userId')
            # print(userid)
            next_url = 'http://music.163.com/api/user/playlist/?offset=0&limit=100&uid=' + str(userid)
            # print(next_url)
            yield scrapy.Request(next_url, callback=self.user_information, dont_filter=True)

    def user_information(self, response):
        json_text = response.text
        json_user = json.loads(json_text)["playlist"]
        item = WangyiyItem()  # 实例化WangyiyItem
        for json_playlist in json_user:
            item['playlistID'] = str(json_playlist["id"])  # 播放列表ID
            print(item['playlistID'])
            item['name'] = json_playlist["name"]  # 歌单名字
            item['tags'] = "、".join(json_playlist["tags"])  # 标签
            item['createTime'] = time.strftime("%Y-%m-%d",
                                               time.localtime(int(str(json_playlist["createTime"])[:-3])))  # 创建时间
            item['playCount'] = json_playlist["playCount"]  # 播放次数
            item['subscribedCount'] = json_playlist["subscribedCount"]  # 订阅计数
            item['nickname'] = json_playlist['creator']['nickname']  # 昵称
            item['gender'] = str(json_playlist['creator']['gender'])  # 性别
            item['userType'] = str(json_playlist['creator']['userType'])  # 用户类型
            item['vipType'] = str(json_playlist['creator']['vipType'])  # vip类型
            item['province'] = str(json_playlist['creator']['province'])  # 省
            item['city'] = str(json_playlist['creator']['city'])  # 城市
            # 匹配性别、省份、城市代码
            if item['gender'] == '1':
                item['gender'] = '男'
            else:
                item['gender'] = '女'

            # 打开行政区代码文件
            with open("country.csv", encoding="utf-8") as f:
                rows = csv.reader(f)

                for row in rows:
                    if row[0] == item['province']:
                        item['province'] = row[1]
                    if row[0] == item['city']:
                        item['city'] = row[1]

                if item['province'] == '香港特别行政区':
                    item['city'] = '香港特别行政区'
                if item['province'] == '澳门特别行政区':
                    item['city'] = '澳门特别行政区'
                if item['province'] == '台湾省':
                    item['city'] = '台湾省'
                if item['province'] == str(json_playlist['creator']['province']):
                    item['province'] = '海外'
                    item['city'] = '海外'
                if item['city'] == str(json_playlist['creator']['city']):
                    item['city'] = item['province']
            yield item
            # print(item)


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl wyy -s LOG_FILE=all.log".split()
    cmdline.execute(args)

# scrapy crawl wyy --nolog不输出日志
# scrapy crawl wyy默认输出日志到窗口
# scrapy crawl wyy -s LOG_FILE=all.log #日志输出到当前目录下

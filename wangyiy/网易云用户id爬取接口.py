# -*- coding:utf-8 -*-
import pymysql
import requests
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}
db = pymysql.connect(host='8.142.77.136', port=3306, user='root', password='root', db='wangfei', charset='utf8mb4')
print('成功！')
conn = db.cursor()


# 获得接口，解析评论接口
def parse_comments_json(comments_list):
    for hotComments in comments_list:

        user_icon = hotComments.get('user').get('avatarUrl')
        print("user_icon: ", user_icon)
        userId = hotComments.get('user').get('userId')
        print("userId: ", userId)
        user_nickname = hotComments.get('user').get('nickname')
        print("user_nickname: ", user_nickname)
        comment_time = hotComments.get('time')
        print("comment_time: ", comment_time)
        comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(float(comment_time) / 1000))
        print(comment_time)
        zan_count = hotComments.get('likedCount')
        print("zan_count: ", zan_count)
        comment_content = hotComments.get('content')
        print("comment_content: ", comment_content)



# 获取全部评论
def get_wangyiyu_comments(url, path):
    header = {
        'Accept': "*/*",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'Host': "music.163.com",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }

    response = requests.post(url, headers=header)
    comments_dict = json.loads(response.text)
    comments_list = comments_dict.get('comments')
    parse_comments_json(comments_list)


if __name__ == '__main__':
    path = 'HelloMyLove.txt'
    start_time = time.time()
    for i in range(575392, 775392):
        # time.sleep(8)
        comments_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_{}".format(i)  # 小宇
        print("==================================================================================================================================================")
        print('爬取的api地址', comments_url)  # 爬取的api地址
        get_wangyiyu_comments(comments_url, path)
        end_time = time.time()
        print("程序耗时%f秒." % (end_time - start_time))

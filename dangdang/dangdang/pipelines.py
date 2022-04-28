# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class DangdangPipeline:
    def process_item(self, item, spider):
        # return item
        # pass
        if item.get('price') == '¥44.40':
            return item
        else:
            raise DropItem("价格不满足已删除")


import pymysql
# mysql数据库存储
class MysqlPipeline:

    # 构造数据库链接创建,实例化当前对象帮我们初始化信息
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    @classmethod  # 类的静态方法
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASS'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        # 打开数据库链接
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port, charset="utf8")
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        # 关闭数据库链
        self.db.close()
        # pass

    def process_item(self, item, spider):
        # 负责数据储存
        sql = u"insert into dangdang(title,author,pic,publish,comment,price)values('%s','%s','%s','%s','%s','%s')" % (
            item['title'], item['author'], item['pic'], item['publish'], item['comment'], item['price'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item

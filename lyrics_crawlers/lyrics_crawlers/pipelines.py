# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class LyricsCrawlersPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='user',
            database='soundtrack_db',
        )
        self.con_db = self.conn.cursor()

    def create_table(self):
        self.con_db.execute("""DROP TABLE IF EXISTS soundtrack_table""")
        self.con_db.execute("""CREATE TABLE soundtrack_table(
                            title text,
                            artist text,
                            album text,
                            year text,
                            writer text,
                            lyrics text
            
        )""")

    def process_item(self, item, spider):
        print("Pipeline:", item)
        self.store_db(item)
        return item

    def store_db(self, item):
        self.con_db.execute("""INSERT INTO soundtrack_table VALUES (%s,%s,%s,%s,%s,%s)""", (
            item['title'], item['artist'], item['album'], item['year'], item['writer'], item['lyrics']
        ))
        self.conn.commit()

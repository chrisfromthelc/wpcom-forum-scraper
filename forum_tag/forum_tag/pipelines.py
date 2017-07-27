# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request


class MySQLStorePipeline(object):
    def __init__(self):
        global db
        db = MySQLdb.connect(host="LOCALHOST", port=3306, user="USER", passwd="PASS", db="forum_topics")
        global cursor
        cursor = db.cursor()

class ForumTagPipeline(object):
    def process_item(self, item, spider):
        try:
            cursor.execute("""INSERT INTO topics (topic_title, topic_url, topic_messages_text)
                            VALUES (%s,%s,%s)""",
                           (item['topic_title'].encode('utf-8'),
                            item['topic_url'].encode('utf-8'),
                            item['topic_messages_text'].encode('utf-8')))

            db.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join

class ForumTagItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topic_title = scrapy.Field()
    topic_url = scrapy.Field()
    topic_messages_text = scrapy.Field()

    pass

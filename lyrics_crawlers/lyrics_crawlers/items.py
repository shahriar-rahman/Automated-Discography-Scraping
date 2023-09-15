# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricsCrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    artist = scrapy.Field()
    album = scrapy.Field()
    year = scrapy.Field()
    writer = scrapy.Field()
    lyrics = scrapy.Field()
    pass

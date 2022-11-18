# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Subject(scrapy.Item):
    name = scrapy.Field()
    week = scrapy.Field()
    lepr = scrapy.Field()
    time = scrapy.Field()
    room = scrapy.Field()

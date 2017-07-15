# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    shipping = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()


class Quote(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class Recipe(scrapy.Item):
    url = scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
    reviews = scrapy.Field()
    cooked_times = scrapy.Field()
    ingredients = scrapy.Field()
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PetShopcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PetzcrawlerItemPage(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field();

class PetzcrawlerItemNumberPage(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field();
    pageNumber = scrapy.Field();

class PetzcrawlerItemProduct(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field();
    sku = scrapy.Field();
    name = scrapy.Field();
    category = scrapy.Field();
    brand = scrapy.Field();
    price = scrapy.Field();
    url = scrapy.Field();

class CobasicrawlerItemCategory(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field();

class CobasicrawlerItemProduct(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field();
    name = scrapy.Field();
    brand = scrapy.Field();
    price = scrapy.Field();
    url = scrapy.Field();

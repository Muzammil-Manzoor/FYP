# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandssaleItem(scrapy.Item):
    # define the fields for your item here like:

    brand_name=scrapy.Field()
    gender_category=scrapy.Field()
    category_name=scrapy.Field()
    
    title=scrapy.Field()
    price=scrapy.Field()
    sale_price=scrapy.Field()
    product_link=scrapy.Field()
    image_link=scrapy.Field()
    image_link2=scrapy.Field()
    
    date=scrapy.Field()
    rating=scrapy.Field()
    status=scrapy.Field()
    brand_id=scrapy.Field()
    category_id=scrapy.Field()
    gender_id=scrapy.Field()
    
    

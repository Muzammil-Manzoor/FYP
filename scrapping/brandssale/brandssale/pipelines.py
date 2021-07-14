# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class BrandssalePipeline:
    
    
    def __init__(self):
        self.create_connnection()
    

    def create_connnection(self):
        self.conn=mysql.connector.connect(
            #**************remote host***************

            # host='remotemysql.com',
            # user='xqfN1TVo49',
            # password='hHCrWlOgxk',
            # database='xqfN1TVo49',
            # port='3306'

           #***************local host**************
            host='localhost',
            user='root',
            password='',
            database='final_testing2',
            port='3306'



        )
        self.curr=self.conn.cursor()


    def process_item(self, item, spider):
        self.store_db(item)
       # print("pipline: "+ item['title'][0])
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into product(brand_name, gender_category,category_name,title,price,sale_price,product_link,image_link,image_link2,datee,rating,status,brand_id,category_id,gender_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
        (
            item['brand_name'],
            item['gender_category'],
            item['category_name'],

            item['title'],
            item['price'],
            item['sale_price'],
            item['product_link'],
            item['image_link'],
            item['image_link2'],
            item['date'],
            item['rating'],
            item['status'],
            item['brand_id'],
            item['category_id'],
            item['gender_id'],
            
        ))
        self.conn.commit()
        

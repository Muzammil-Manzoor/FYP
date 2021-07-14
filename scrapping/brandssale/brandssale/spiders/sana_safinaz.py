import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from ..items import BrandssaleItem
from datetime import date
import io

class SanaSafinazSpider(scrapy.Spider):
    name = 'sana_safinaz'
    page_number1= 2
    page_number2= 2
    category_name=''

    # allowed_domains = ['https://www.sanasafinaz.com/pk/sale/ready-to-wear.html']
    start_urls = ['https://www.sanasafinaz.com/pk/sale/ready-to-wear.html?p=1',
    'https://www.sanasafinaz.com/pk/sale/unstitched-fabric.html?p=1'
    ]

    def parse(self, response):



        items=BrandssaleItem()

        today= date.today()
        datee = today.strftime("%Y-%m-%d")

        all_div_quotes=response.css('.product-item')
        
        for quotes in all_div_quotes:
            title=quotes.css('.product-item-link::text').get().replace('\r\n','').strip()
            
            category_name=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get()
            if title is list:
                title=title[0]
            
            if category_name=='Ready To Wear':
                category_name='kameezshalwar_stitched'
                category_id=4
            elif category_name=='Unstitched Fabric':
                category_name='kameezshalwar_unstitched' 
                category_id=5
            elif category_name=='Accessories':
                category_name='accessories'
                category_id=10


            sale_price=quotes.css('.special-price .price::text').get()
            price=quotes.css('.sly-old-price .price::text').get() 

            product_link=quotes.css('a.sl-product-item-photo::attr(href)').get() 
            
            image_link=quotes.css('.product-image-photo::attr(srcset)').get()
            image_link2=quotes.css('.hover_image::attr(srcset)').get()
            if image_link2==None:
                image_link2=image_link
            




        

            items['brand_name'] ='Sana Safinaz'
            items['title']=title
            items['category_name'] =category_name

            items['gender_category'] ='female'
            items['price']=price
            items['sale_price']=sale_price
            items['product_link']=product_link
            items['image_link']=image_link
            items['image_link2']=image_link2
            items['date']=datee
            items['rating']='Good'
            items['status']='avb'

            items['brand_id']=3
            items['category_id']=category_id
            items['gender_id']=1

            yield items

        

      
        if category_name=='kameezshalwar_stitched':           
            next_page='https://www.sanasafinaz.com/pk/sale/ready-to-wear.html?p='+str(SanaSafinazSpider.page_number1)

            if SanaSafinazSpider.page_number1 <3:
                SanaSafinazSpider.page_number1 +=1
                yield response.follow(next_page,callback=self.parse)
        
        # if category_name=='kameezshalwar_unstitched':           
        #     next_page='https://www.sanasafinaz.com/pk/sale/unstitched-fabric.html?p='+ str(SanaSafinazSpider.page_number2)

        #     if SanaSafinazSpider.page_number2 <3:
        #         SanaSafinazSpider.page_number2 +=1
        #         yield response.follow(next_page,callback=self.parse)



       

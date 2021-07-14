import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from ..items import BrandssaleItem
from datetime import date
import io



class MariabSpider(scrapy.Spider):
    name = 'mariab'
   # allowed_domains = ['https://www.mariab.pk/sale/unstitched.html']

    page_number= 2
    category_name=''

    start_urls = [
        'https://www.mariab.pk/sale/unstitched.html/',
        'https://www.mariab.pk/sale/pret.html'
     
    ]

    def parse(self, response):
        # html=response.text
        # with io.open("khaadi.txt", "w", encoding="utf-8") as f:

        #     f.write(html)


        items=BrandssaleItem()

        today= date.today()
        datee = today.strftime("%Y-%m-%d")

        all_div_quotes=response.css('div.fhover')
        
        for quotes in all_div_quotes:
            title=quotes.css('.product-name a::text').get().replace('\r\n','').strip()
            title=title.lower()

            if 'unstitched' in title:
                category_name='kameezshalwar_unstitched' 
                category_id=5

            else:
                category_name='kameezshalwar_stitched'
                category_id=4

            sale_price=quotes.css('.special-price .price::text').get()
            price=quotes.css('.old-price .price::text').get()
            if sale_price is not None:
                sale_price=sale_price.replace('\r\n','').strip()
            if price is not None:
                price=price.replace('\r\n','').strip()

            product_link=quotes.css('a.product-image::attr(href)').get() 
            
            image_link=quotes.css('.product-image img::attr(src)').get()
            image_link2=quotes.css('.backImage::attr(src)').get()
            if image_link2==None:
                image_link2=image_link
            
            items['brand_name'] ='Maria.B'
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

            items['brand_id']=5
            items['category_id']=category_id
            items['gender_id']=1

            yield items

        
        # next_page='https://www.mariab.pk/ready-pret/m-basics.html#/page/='+str(MariabSpider.page_number)

        # if MariabSpider.page_number <5:
        #     MariabSpider.page_number +=1
        #     yield response.follow(next_page,callback=self.parse)
import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from ..items import BrandssaleItem
from datetime import date
import io


class BataSpider(scrapy.Spider):

    name = 'bata'
    page_number1= 2
    page_number2=2
    page_number3=2

   # allowed_domains = ['https://www.bata.com.pk/collections/deals']
    start_urls = [
       'https://www.bata.com.pk/collections/women-deals?page=1',
       'https://www.bata.com.pk/collections/kids-deals?page=1',
         'https://www.bata.com.pk/collections/men-deals?page=1',
        ]

    def isWordPresent(sentence, word):
    
        s = sentence.split(" ")
 
        for i in s:
            if (i == word):
                return True
        return False

    def parse(self, response):
        
        items=BrandssaleItem()

        today= date.today()
        datee = today.strftime("%Y-%m-%d")

        all_div_quotes=response.css('.mobile-half')
        
        for quotes in all_div_quotes:
            title=quotes.css('h3::text').get().replace('\r\n','').strip()
            title=title.lower()

            
            gender_category=quotes.xpath('//h1/text()').get()
           # gender_category=quotes.css('h1::text').get().replace('\r\n','').strip()
            gender_category=gender_category.lower()

            #if 'men' in gender_category:
            if (BataSpider.isWordPresent(gender_category, 'men')):
                gender_category='male'
                category_name='shoes' 
                category_id=11
                gender_id=2

            elif (BataSpider.isWordPresent(gender_category, 'women')):
                gender_category='female'
                category_name='shoes' 
                category_id=11
                gender_id=1

            elif (BataSpider.isWordPresent(gender_category, 'kids')):
                gender_category='kid'
                category_name='shoes' 
                category_id=11
                gender_id=3

            sale_price=quotes.css('.money::text').get()
            price=quotes.css('.was .money::text').get()
            if sale_price is not None:
                sale_price=sale_price.replace('\r\n','').strip()
            if price is not None:
                price=price.replace('\r\n','').strip()

            product_link=quotes.css('div .product-info a::attr(href)').get() 
            product_link='https://www.bata.com.pk'+product_link           
            
            
            image_link=quotes.css('div img ::attr(src)').get()

            image_link2=quotes.css('div .hidden img::attr(src)').get()
            if image_link2==None:
                image_link2=image_link
            
            items['brand_name'] ='Bata'
            items['title']=title
            items['category_name'] =category_name

            items['gender_category'] =gender_category
            items['price']=price
            items['sale_price']=sale_price
            items['product_link']=product_link
            items['image_link']=image_link
            items['image_link2']=image_link2
            items['date']=datee
            items['rating']='Good'
            items['status']='avb'

            items['brand_id']=6
            items['category_id']=category_id
            items['gender_id']=gender_id

            yield items

        
        if gender_category=='male':
            
            next_page='https://www.bata.com.pk/collections/men-deals?page='+ str(BataSpider.page_number1)

            if BataSpider.page_number1 <4:
                BataSpider.page_number1 +=1
                yield response.follow(next_page,callback=self.parse)

        if gender_category=='female':
            
            next_page='https://www.bata.com.pk/collections/women-deals?page='+ str(BataSpider.page_number2)

            if BataSpider.page_number2 <4:
                BataSpider.page_number2 +=1
                yield response.follow(next_page,callback=self.parse)

        if gender_category=='kid':
            
            next_page='https://www.bata.com.pk/collections/kids-deals?page='+ str(BataSpider.page_number3)

            if BataSpider.page_number3 <2:
                BataSpider.page_number3 +=1
                yield response.follow(next_page,callback=self.parse)
        



import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
from ..items import BrandssaleItem
from datetime import date
import io


class GulahmedSpider(scrapy.Spider):
    name = 'gulahmed'
    page_number1
    page_number2
    page_number3
    page_number4
    page_number5
    page_number6
    page_number7
    page_number8
    page_number9
    page_number10
    #allowed_domains = ['https://www.gulahmedshop.com/sale']
    start_urls = [
    #women
        
    #    'https://www.gulahmedshop.com/sale?cat=269_ready-to-wear&p=1',
      #  'https://www.gulahmedshop.com/sale?cat=289_unstitched&p=1',
         #'https://www.gulahmedshop.com/sale?cat=350_trousers&p=1',

       #  'https://www.gulahmedshop.com/sale?cat=347_salt&p=1',
        # 'https://www.gulahmedshop.com/sale/accessories?cat=323_bags&p=1',
        'https://www.gulahmedshop.com/sale/accessories?cat=371_shoes&p=1',
    
    # # # man
         #'https://www.gulahmedshop.com/sale/men?cat=263_unstitched&p=1',
         #'https://www.gulahmedshop.com/sale/men?cat=275_western&p=1',
        #'https://www.gulahmedshop.com/sale/men?cat=242_eastern&p=1',
    # #  # kids
          # 'https://www.gulahmedshop.com/kids?cat=249_girls&p=1',



        ]

    def parse(self, response):
        
        # html=response.text
        # with io.open("khaadi.txt", "w", encoding="utf-8") as f:
        #     f.write(html)



        items=BrandssaleItem()

        today= date.today()
        datee = today.strftime("%Y-%m-%d")

        all_div_quotes=response.css('.product-item .product-item-info')
        
        for quotes in all_div_quotes:
            
            title=quotes.css('.product-item-link::text').get().replace('\r\n','').strip()
            
            
            category_name=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "filter-value", " " ))]/text()').get()
            category_name=category_name.lower()

            if title is list:
                title=title[0]
            
            if category_name=='eastern':
                category_name='kameezshalwar_stitched'
                category_id=4
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

            elif category_name=='ready to wear':
                category_name='kameezshalwar_stitched'
                category_id=4
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

            elif category_name=='unstitched':
                category_name='kameezshalwar_unstitched' 
                category_id=5
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='women'
                    gender_id=1

            elif category_name=='trousers':
                category_name='pant' 
                category_id=2
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

            elif category_name=='salt':
                category_name='shirt' 
                category_id=1
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

                

            elif category_name=='western':
                category_name='shirt_pant' 
                category_id=3
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2

                
                # if a=='Men' and b==None:
                #     gender_id=2
                #     gender_category=Male
                # if a==None' and b=='Men':
                #     gender_id=2
                #     gender_category=Male



            elif category_name=='Accessories':
                category_name='accessories'
                category_id=10

            elif category_name=='girls':
                category_name='shirt_pant'
                gender_id=3
                gender_category='kid'
                category_id=3

            elif category_name=='bags':
                category_name='bags' 
                category_id=12
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

            elif category_name=='shoes':
                category_name='shoes' 
                category_id=11
                gender_category=quotes.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "base", " " ))]/text()').get().replace('\r\n','').strip().lower()
                if gender_category=='men':
                    gender_category='Male'
                    gender_id=2
                else:
                    gender_category='female'
                    gender_id=1

            





            sale_price=quotes.css('.special-price .price::text').get()
            price=quotes.css('.old-price .price::text').get() 

            product_link=quotes.css('a.product-item-photo::attr(href)').get() 
            
            image_link=quotes.css('.main-image .product-image-photo::attr(src)').get()
            image_link2=quotes.css('.hover-image .product-image-photo::attr(src)').get()
            if image_link2==None:
                image_link2=image_link
            




        

            items['brand_name'] ='Gul Ahmed'
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

            items['brand_id']=2
            items['category_id']=category_id
            items['gender_id']=gender_id

            yield items


       # **************kids*****************
        if category_name=='shirt_pant' and gender_category=='kid':         
            next_page='https://www.gulahmedshop.com/kids?cat=249_girls&p='+str(GulahmedSpider.page_number1)
            if GulahmedSpider.page_number1 <7:
                GulahmedSpider.page_number1 +=1
                yield response.follow(next_page,callback=self.parse)

        #**************men stitched*********************
        if category_name=='kameezshalwar_stitched' and gender_category=='Male':         
            next_page='https://www.gulahmedshop.com/sale/men?cat=242_eastern&p='+str(GulahmedSpider.page_number2)
            if GulahmedSpider.page_number2 <3:
                GulahmedSpider.page_number2 +=1
                yield response.follow(next_page,callback=self.parse)

                
        #**************men westren*********************
        if category_name=='shirt_pant' and gender_category=='Male':         
            next_page='https://www.gulahmedshop.com/sale/men?cat=275_western&p='+str(GulahmedSpider.page_number3)
            if GulahmedSpider.page_number3 <2:
                GulahmedSpider.page_number3 +=1
                yield response.follow(next_page,callback=self.parse)

            
        
        #**************men unstitched*********************
        if category_name=='kameezshalwar_unstitched' and gender_category=='Male':         
            next_page='https://www.gulahmedshop.com/sale/men?cat=263_unstitched&p='+str(GulahmedSpider.page_number4)
            if GulahmedSpider.page_number4 <7:
                GulahmedSpider.page_number4 +=1
                yield response.follow(next_page,callback=self.parse)

        #**************women unstitched*********************
        if category_name=='kameezshalwar_unstitched' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale?cat=289_unstitched&p='+str(GulahmedSpider.page_number5)
            if GulahmedSpider.page_number5 <5:
                GulahmedSpider.page_number5 +=1
                yield response.follow(next_page,callback=self.parse)

    
        
        #**************women stitched*********************
        if category_name=='kameezshalwar_stitched' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale?cat=269_ready-to-wear&p='+str(GulahmedSpider.page_number6)
            if GulahmedSpider.page_number6 <8:
                GulahmedSpider.page_number6 +=1
                yield response.follow(next_page,callback=self.parse)
            


        #**************women pant*********************
        if category_name=='pant' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale?cat=350_trousers&p='+str(GulahmedSpider.page_number7)
            if GulahmedSpider.page_number7 <3:
                GulahmedSpider.page_number7 +=1
                yield response.follow(next_page,callback=self.parse)

        #**************women shoes*********************
        if category_name=='shoes' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale/accessories?cat=371_shoes_shoes&p='+str(GulahmedSpider.page_number8)
            if GulahmedSpider.page_number8 <3:
                GulahmedSpider.page_number8 +=1
                yield response.follow(next_page,callback=self.parse)
        
        #**************women bags*********************
        if category_name=='bags' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale/accessories?cat=323_bags&p='+str(GulahmedSpider.page_number9)
            if GulahmedSpider.page_number9 <5:
                GulahmedSpider.page_number9 +=1
                yield response.follow(next_page,callback=self.parse)
                
        #**************women shirt*********************
        if category_name=='bags' and gender_category=='women':         
            next_page='https://www.gulahmedshop.com/sale?cat=347_salt&p='+str(GulahmedSpider.page_number10)
            if GulahmedSpider.page_number10 <3:
                GulahmedSpider.page_number10 +=1
                yield response.follow(next_page,callback=self.parse)
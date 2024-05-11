import scrapy

class NewsDaySpider(scrapy.Spider):
    name = 'sundaymail'
    start_urls = [
        'https://www.newsday.co.zw/category/4/business',
        'https://www.newsday.co.zw/category/9/opinion-and-analysis',
        'https://www.newsday.co.zw/category/5/sport',
        'https://www.newsday.co.zw/category/8/lifestyle-and-arts'
        
    ]

    def parse(self, response):
        # Extract data from each article
            category = response.css('div.row h1 a.links::text').get()
            title = response.css('a.text-dark div.sub-title.mt-3::text').extract()
            link = response.css('div.card-body.pad-o.mt-3 a::attr(href)').extract()
            content = response.css('div.card-body.pad-o.mt-3 div.mb-3.pt-2.top-article::text').extract()

            row_data = zip(title,link,content)
            
        #Making extracted data row wise
            for item in row_data:
                #create a dictionary to store the scraped info
                scraped_info = {
                    #key:value
                    'category':category,
                    'title' : item[0],
                    'link' : item[1],
                    'content' : item[2]
                }

                #yield or give the scraped info to scrapy
                yield scraped_info
                
                
class NewsDaySpider(scrapy.Spider):
    name = 'hmetro'
    start_urls = [
        'https://fingaz.co.zw/category/c77-companies-a-markets',
        'https://fingaz.co.zw/category/lifestyle',
        'https://fingaz.co.zw/category/sport',
        'https://fingaz.co.zw/category/tech/'
        
    ]

    def parse(self, response):
        # Extract data from each article
            category = response.css('div.category-title h2 a.links::text').get()
            title = response.css('div.entry-title div.sub-title.mt-3::text').extract()
            link = response.css('div.entry-title.pad-o.mt-3 a::attr(href)').extract()
            content = response.css('div.post-excerpt.pad-o.mt-3 div.mb-3.pt-2.top-article::text').extract()

            row_data = zip(title,link,content)
            
        #Making extracted data row wise
            for item in row_data:
                #create a dictionary to store the scraped info
                scraped_info = {
                    #key:value
                    'category':category,
                    'title' : item[0],
                    'link' : item[1],
                    'content' : item[2]
                }

                #yield or give the scraped info to scrapy
                yield scraped_info
                

                #yield or give the scraped info to scrapy
                yield scraped_info

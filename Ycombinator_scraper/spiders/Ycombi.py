import scrapy
import time

class ycombi(scrapy.Spider):
    name = 'ycombi'
    start_urls = ['https://news.ycombinator.com/newest']

    def parse(self, response):
        for posts in response.css('span.titleline'):
            yield {
                'title': posts.css('a::text').get(),
                'link': posts.css('a::attr(href)').get()
            }
        time.sleep(1)
        next_page = response.css('a.morelink').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse) # runs parse function again
# spiders/quotes.py

import scrapy
from template.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes_page'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield scrapy.Request(url, meta=dict(
            playwright = True,
            playwright_include_page = True, 
        ))

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = QuoteItem()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item

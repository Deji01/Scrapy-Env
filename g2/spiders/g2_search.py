import scrapy
from g2.items import G2Item

class G2SearchSpider(scrapy.Spider):
    name = 'g2-search'
    allowed_domains = ['g2.com']
    start_urls = ['https://www.g2.com/search?utf8=%E2%9C%93&query=sales+and+marketing&filters%5Bcategory_ids%5D%5B%5D=771&filters%5Bcategory_ids%5D%5B%5D=2']

    def parse(self, response):
        for div in response.css('div.cell.large-8.xlarge-9'):
            g2_item = G2Item()
            g2_item["name"] = div.css("div.product-listing.mb-1.border-bottom > div.product-listing__head > div > div > div > a > div::text").get()
            g2_item["description"] = div.css("div.product-listing.mb-1.border-bottom > div.product-listing__body > div > p > span::text").get()
            g2_item["link"] = div.css("div.product-listing.mb-1.border-bottom > div.product-listing__head > div > div > div > a:attr[href]").get()
            g2_item["category"] = div.css("div.grid-x.grid-margin-x.product-listing__search-footer > div.cell.xlarge-8::text").getall()
            yield g2_item
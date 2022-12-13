import scrapy
from g2.items import G2Item

class G2SearchSpider(scrapy.Spider):
    name = 'g2-search'
    allowed_domains = ['g2.com']
    start_urls = ['https://www.g2.com/search?utf8=%E2%9C%93&query=sales+and+marketing&filters%5Bcategory_ids%5D%5B%5D=771&filters%5Bcategory_ids%5D%5B%5D=2']

    def parse(self, response):
        for div in response.css('div.paper.mb-1'):
            g2_item = G2Item()
            g2_item["name"] = response.css("body > div.off-canvas-wrapper > div > div > div.d-f.fd-c.min-h-full-screen > div > div.page.paper-padding > div > div.cell.large-8.xlarge-9 > div:nth-child(4) > div.product-listing.mb-1.border-bottom > div.product-listing__head > div > div > div > a > div::text").get()
            g2_item["description"] = response.css("body > div.off-canvas-wrapper > div > div > div.d-f.fd-c.min-h-full-screen > div > div.page.paper-padding > div > div.cell.large-8.xlarge-9 > div:nth-child(4) > div.product-listing.mb-1.border-bottom > div.product-listing__body > div > p > span::text").get()
            g2_item["link"] = response.css("body > div.off-canvas-wrapper > div > div > div.d-f.fd-c.min-h-full-screen > div > div.page.paper-padding > div > div.cell.large-8.xlarge-9 > div:nth-child(4) > div.product-listing.mb-1.border-bottom > div.product-listing__head > div > div > div > a:attr[href]").get()
            g2_item["category"] = response.css("body > div.off-canvas-wrapper > div > div > div.d-f.fd-c.min-h-full-screen > div > div.page.paper-padding > div > div.cell.large-8.xlarge-9 > div:nth-child(4) > div.grid-x.grid-margin-x.product-listing__search-footer > div.cell.xlarge-8::text").getall()
            yield g2_item
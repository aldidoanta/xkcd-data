import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://xkcd.com/info.0.json',
    ]

    def parse(self, response):
       jsonresponse = json.loads(response.body_as_unicode())
       return jsonresponse
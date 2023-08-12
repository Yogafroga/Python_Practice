import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv


class SteamSpider(CrawlSpider):

    name = "steam"
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?filter=topsellers']
    custom_settings = {
        'DEPTH_LIMIT': 1000
    }
    rules = (
        Rule(LinkExtractor(allow=r'app/'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        yield {
            'Tag': response.xpath("//a[@class='app_tag']/text()").getall()
        }
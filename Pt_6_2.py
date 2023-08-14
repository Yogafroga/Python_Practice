import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv


class SteamSpider(CrawlSpider):
    name = "steam"
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 1500
    }
    rules = (
        Rule(LinkExtractor(allow=r'app/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tags = response.xpath("//a[@class='app_tag']")

        tag_text = []
        for tag in tags:
            tag_text.append(tag.xpath("text()").get().strip())

        with open('steam_tags.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(tag_text)

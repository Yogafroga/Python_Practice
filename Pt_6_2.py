import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv


class SteamSpider(CrawlSpider):
    name = "steam"
    allowed_domains = ['store.steampowered.com']
    start_urls = ['https://store.steampowered.com/search/?category1=998&filter=globaltopsellers&ndl=1']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 1500
    }
    rules = (
        Rule(LinkExtractor(allow=r'app/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tags = response.xpath("//a[@class='app_tag']")
        tag_text = [tag.xpath("text()").get().strip() for tag in tags]

        if tag_text:  # Check if there are tags before writing
            game_title = response.xpath("//div[@class='apphub_AppName']/text()").get()
            if game_title:
                with open('steam_tags.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([game_title] + tag_text)  # Write game title and tags on the same row

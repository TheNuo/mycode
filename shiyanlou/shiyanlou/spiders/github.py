# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem

class GithubSpider(scrapy.Spider):
    name = 'github'

    @property
    def start_urls(self):
        url_1 = 'https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yMVQxODowOTowMiswODowMM4BnQBZ&tab=repositories'
        url_2 = 'https://github.com/shiyanlou?before=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories'
        url_3 = 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxNjoxNzo1MyswODowMM4Bx3_0&tab=repositories'
        url_4 = 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMS0yNFQxNTowMDoxNyswODowMM4BnPdj&tab=repositories'
        return [url_1, url_2, url_3, url_4]

    def parse(self, response):
        for i in response.css('div.col-9.d-inline-block'):
            item = GithubItem({
                'name': i.css('div.d-inline-block.mb-1 h3 a::text').re_first(' *(.+)'),
                'update_time': i.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()
            })
            yield item


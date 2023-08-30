import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import ALLOWED_DOMAINS, START_URLS


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        tr_tags = response.css('section#numerical-index tbody tr')
        for tr_tag in tr_tags:
            yield response.follow(
                tr_tag.css('a').attrib['href'] + '/', callback=self.parse_pep)

    def parse_pep(self, response):
        string_number = response.css(
            'ul.breadcrumbs li:last-child::text').get()
        return PepParseItem(
            number=''.join(num for num in string_number if num.isdigit()),
            name=response.css('section#pep-content h1::text').get(),
            status=response.css('dd.field-even abbr::text').get(),
        )

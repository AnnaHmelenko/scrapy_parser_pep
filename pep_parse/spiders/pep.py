import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    # Связываем start_urls с allowed_domains через list comprehension
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        pep_links = response.css(
            'table.pep-zero-table a.pep::attr(href)'
        ).getall()

        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        status = response.css(
            'dt:contains("Status") + dd abbr::text'
        ).get()

        if title:
            parts = title.split(' – ', 1)

            if len(parts) == 2:
                number = parts[0].replace('PEP ', '')
                name = parts[1]

                yield PepParseItem(
                    number=number,
                    name=name,
                    status=status,
                )

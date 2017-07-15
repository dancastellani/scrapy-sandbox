import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes_splash"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        # yield scrapy.Request(url, self.parse)
        yield SplashRequest(url, self.parse,
                            endpoint='render.html',
                            args={'wait': 0.5},
                            )

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)
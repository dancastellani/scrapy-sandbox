
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class QuotesSpider(CrawlSpider):
    name = "quotes_crawl"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('page', )),  callback='parse_quote'),
    )

    def parse_page(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        items = []
        for quote in response.css('div.quote'):
            item = scrapy.item.Item()
            item['text'] = quote.css('span.text::text').extract_first()
            item['author'] = quote.css('span small::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            items.append(item)
        return items

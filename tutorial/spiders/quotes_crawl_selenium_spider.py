
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import Quote
from selenium import webdriver


class QuotesCrawlSeleniumSpider(CrawlSpider):
    name = "quotes_selenium"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('page', )),  callback='parse_page'),
    )

    def __init__(self, *args, **kwargs):
        super(QuotesCrawlSeleniumSpider, self).__init__(*args, **kwargs)
        self.download_delay = 0.25
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(60)

    def parse_page(self, response):
        self.logger.info('Hi, this is a page! %s', response.url)
        quotes = []
        for page_quote in response.css('div.quote'):
            quote = Quote()
            quote['text'] = page_quote.css('span.text::text').extract_first()
            quote['author'] = page_quote.css('span small::text').extract_first()
            quote['tags'] = page_quote.css('div.tags a.tag::text').extract()
            quotes.append(quote)
        return quotes

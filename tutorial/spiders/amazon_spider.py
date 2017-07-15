import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import Product

from tutorial import helpers


class AmazonSpider(CrawlSpider):
    name = 'amazon'

    allowed_domains = ['amazon.com']
    # start_urls = ['https://amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=laptop']

    custom_settings = {
        'DEPTH_LIMIT': 2,
        'DOWNLOAD_DELAY': 2,
    }

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('dp', )),  callback='parse_product'),
        # Rule(LinkExtractor(allow=('gp', )),  callback='parse_product'),
    )

    def parse_product(self, response):
        self.logger.info('Amazon product page: %s', response.url)
        product = Product()
        product['name'] = helpers.clean(response.css('span#productTitle::text').extract_first())
        product['description'] = helpers.clean(response.css('#productDescription p::text').extract_first())
        product['price'] = helpers.clean(response.css('#priceblock_ourprice::text').extract_first())
        product['shipping'] = helpers.clean(response.css('#price-shipping-message::text').extract_first())
        product['rating'] = helpers.clean(response.css('.arp-rating-out-of-text::text').extract_first())
        product['reviews'] = helpers.clean(response.css('#acrCustomerReviewText::text').extract_first())
        if product['reviews']:
            product['reviews'] = product['reviews'].replace(' customer reviews', '')
        product['url'] = response.url
        return product



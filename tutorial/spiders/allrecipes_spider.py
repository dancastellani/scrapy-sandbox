import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import Recipe

from tutorial import helpers


class AllRecipesSpider(CrawlSpider):
    name = 'allrecipes'

    allowed_domains = ['allrecipes.com.br']
    start_urls = ['http://allrecipes.com.br/receitas/pratos.aspx?o_is=TopNode_1_Pratos']

    custom_settings = {
        'DEPTH_LIMIT': 1,
    }

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('receita*.aspx',)), callback='parse_item'),
        # Rule(LinkExtractor(allow=('gp', )),  callback='parse_product'),
    )

    def parse_item(self, response):
        self.logger.info('Recipe page: %s', response.url)
        recipe = Recipe()
        recipe['url'] = response.url
        recipe['name'] = helpers.clean(response.css('.boardContainer h1 span::text').extract_first())
        recipe['description'] = helpers.clean(response.css('.description::text').extract_first())
        recipe['cooked_times'] = helpers.clean(response.css('#imi10842 span::text').extract_first())
        if recipe['cooked_times']:
            recipe['cooked_times'] = recipe['cooked_times'].replace(' pessoas fizeram essa receita', '')
        ingredients = []
        for ingredient in response.css('.recipeIngredients ul li span::text').extract():
            ingredients.append(ingredient)
        recipe['ingredients'] = ingredients

        return recipe

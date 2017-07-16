# scrapy-tutorial + other things
https://docs.scrapy.org/en/latest/intro/tutorial.html

This is my scrapy sandbox. I followed the Scrapy tutorial and then tried other things.
Played to crawl with **Amazon.com** and **AllRecipes**, but got banned after a few runs.

TODO:
* Discover how to avoid bot-blockers and crawl `tudogostoso.com.br`

# How do I get set up? 

## Dependencies

* Python3
* [Scrapy](https://docs.scrapy.org/en/latest/index.html)
* [Splash](https://splash.readthedocs.io/en/stable/index.html)
* Docker (to run the Splash container)
* Selenium and geckodriver (firefox webdriver) - for `quotes_selenium` spider

## Set up (ubuntu)
1. Install ubuntu dependencies: `sudo ./configure`
2. Create a virtual env (`virtualenv -p python3 env`) and source it (`source env/bin/activate`).
3. Install pip dependencies (`pip install -r requirements.txt`)
4. Run Splash on Docker. 
Pull Splash image (`docker pull scrapinghub/splash`) 
and run the container (`docker run -d -p 8050:8050 -p 5023:5023 scrapinghub/splash`).

# Usage

Implementations from **quotes crawler** using Spider and CrawlSpider 
with/out Splash.

Run `scrapy crawl <spider_name>`. 

Possible spiders:
* `quotes_crawl`
* `quotes_splash`
* `quotes_crawl_splash`

To save on a file the extracted items, use `-o <filename`. 
Supported extensions include `.jl` and `.json` among others.

## Extra Spiders
* `amazon`: crawl products from [Amazon.com](https://amazon.com) (searched for _ldaptops_)
* `allrecipes`: crawl recipes from [allrecipes.com.br](http://allrecipes.com.br) 
* `quotes_selenium` (Run on Selenium)

**Note**: Running `amazon` and `allrecipes` crawlers can get banned after a few runs.

# References:
* [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
* [Scrapy with Splash on Docker and Splash](https://github.com/scrapy-plugins/scrapy-splash)
* [Python Selenium](http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)
* [Headless Firefox](http://scraping.pro/use-headless-firefox-scraping-linux/)
* [Fake-user-agents](https://github.com/alecxe/scrapy-fake-useragent) can help avoid being banned.
 
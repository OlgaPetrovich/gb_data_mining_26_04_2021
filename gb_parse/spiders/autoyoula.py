import scrapy
from ..loaders import AutoyoulaLoader

class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']
    _xpath_selectors = {
        "brand": "//div[contains(@class, 'TransportMainFilters_brandsList')]"
                 "//a[@data-target='brand']/@href",
        "pagination": "//div[contains(@class, 'Paginator_block')]"
                      "/a[@data-target-id='button-link-serp-paginator']/@href",
        "car": "//article[@data-target='serp-snippet']//a[@data-target='serp-snippet-title']/@href",
    }
    _xpath_data_selectors = (
        {
            "field_name": "title",
            "xpath": "//div[@data-target='advert-title']/text()"
        },
        {
            "field_name": "price",
            "xpath": "//div[@data-target='advert-price']/text()"
        }
    )

    def _get_follow(self, response, selector_str, callback):
        for url in response.xpath(selector_str):
            yield response.follow(url, callback=callback)

    def parse(self, response, *args, **kwargs):
        yield from self._get_follow(
            response,
            self._xpath_selectors["brand"]
            , self.brand_parse
        )

    def brand_parse(self, response):
        yield from self._get_follow(
            response,
            self._xpath_selectors["pagination"]
            , self.brand_parse
        )
        yield from self._get_follow(
            response,
            self._xpath_selectors["car"]
            , self.car_parse
        )

    def car_parse(self, response):
        loader = AutoyoulaLoader(response=response)
        loader.add_value("url", "")
        loader.add_value("url", response.url)
        loader.add_value("url", "hello")
        for xpath_strict in self._xpath_data_selectors:
            loader.add_xpath(** xpath_strict)
        yield loader.load_item()
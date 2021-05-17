from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose


def clear_price():
    try:
        result = float(price.replace("\u2009", ''))
    except ValueError:
        result = None
    return result


class AutoyoulaLoader(ItemLoader):
    default_item_class = dict
    url_out = TakeFirst()
    title_out = TakeFirst()
    price_in = MapCompose(clear_price)
    price_out = TakeFirst()

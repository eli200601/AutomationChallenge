from ui_lib.selenium import Locator, LT, SeleniumElement


class ResultsScreenLocators(object):
    def __init__(self, driver_):
        self._driver = driver_
        self.results_items = SeleniumElement(self._driver, Locator(LT.class_name, 's-result-item', multi_item_=True))
        # Child items of results_items
        self.book_name = SeleniumElement(self._driver, Locator(LT.xpath, './/h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]'))
        self.book_author_date = SeleniumElement(self._driver, Locator(LT.xpath, './/div[@class="a-row a-size-base a-color-secondary"][1]'))
        self.book_rating = SeleniumElement(self._driver, Locator(LT.xpath, './/span[@class="a-icon-alt"]/../../../..'))
        self.book_reviews = SeleniumElement(self._driver, Locator(LT.xpath, './/div[@class="a-section a-spacing-none a-spacing-top-micro"][1]//span[2]'))
        self.book_price = SeleniumElement(self._driver, Locator(LT.xpath, './/span[@class="a-price"]'))
        self.price_secondary = SeleniumElement(self._driver, Locator(LT.xpath, './/span[@class="a-color-base" or "a-size-small a-color-secondary"]'))
        self.item_href = SeleniumElement(self._driver, Locator(LT.class_name, 'a-link-normal'))
        # Result page navigation bar
        self.navigation_bar = SeleniumElement(self._driver, Locator(LT.xpath, '//ul[@class="a-pagination"]//li', multi_item_=True))

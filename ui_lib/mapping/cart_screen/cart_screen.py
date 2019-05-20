from ui_lib.selenium import Locator, LT, SeleniumElement


class CartScreenLocators(object):
    def __init__(self, driver_):
        self._driver = driver_
        self.cart_items = SeleniumElement(self._driver, Locator(LT.xpath, '//div[@id[starts-with(., "sc-item-")]]', multi_item_=True))

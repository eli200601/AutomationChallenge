from ui_lib.selenium import Locator, LT, SeleniumElement


class BookItemScreenLocators(object):
    def __init__(self, driver_):
        self._driver = driver_
        self.paperback = SeleniumElement(self._driver, Locator(LT.id, 'a-autoid-1-announce'))
        self.add_to_cart_button = SeleniumElement(self._driver, Locator(LT.id, 'add-to-cart-button'))

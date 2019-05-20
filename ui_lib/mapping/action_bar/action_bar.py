from ui_lib.selenium import Locator, LT, SeleniumElement


class ActionBarLocators(object):

    def __init__(self, driver_):
        self._driver = driver_
        self.search_field = SeleniumElement(self._driver, Locator(LT.id, 'twotabsearchtextbox'))
        self.cart_button = SeleniumElement(self._driver, Locator(LT.id, 'nav-cart-count'))

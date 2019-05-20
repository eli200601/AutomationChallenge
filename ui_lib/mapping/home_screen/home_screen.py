from ui_lib.selenium import Locator, LT, SeleniumElement


class HomeScreenLocators(object):
    def __init__(self, driver_):
        self._driver = driver_
        self.path = "http://www.amazon.com"

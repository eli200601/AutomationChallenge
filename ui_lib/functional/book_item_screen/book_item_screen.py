from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from ui_lib.functional import BasePageElement
from ui_lib.mapping import BookItemScreenLocators


class BookItemFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = BookItemScreenLocators(driver)

    def click_paperback(self):
        try:
            self._map.paperback.click()
        except (ElementNotVisibleException, NoSuchElementException):
            try:
                self._map.paperback_sec.click()
            except (ElementNotVisibleException, NoSuchElementException):
                print('paperback No clicked')

    def click_add_to_cart(self):
        self.click_paperback()
        self._map.add_to_cart_button.click()

from ui_lib.functional import BasePageElement
from ui_lib.mapping import ActionBarLocators


class ActionBarFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = ActionBarLocators(driver)

    def click_cart(self):
        self._map.cart_button.click()

    def search_for_text(self, text_):
        print('Set text: ' + text_)
        while not self._map.search_field.find_element().get_attribute('value') == text_:
            self._map.search_field.set_text(text_)
        self._map.search_field.send_enter_key()

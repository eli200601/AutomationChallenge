from ui_lib.mapping import CartScreenLocators
from ui_lib.functional import BasePageElement
from ui_lib.functional.action_bar import ActionBarFunctionality


class CartScreenFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = CartScreenLocators(driver)
        self.action_bar = ActionBarFunctionality(driver)

    def check_if_item_exist_in_cart(self, book_item_):
        cart_items = self._map.cart_items.find_element()
        for item in cart_items:
            if item.text.__contains__(book_item_.book_name):
                print('Item exist in the cart list')
                return True
        print('Item does not exist in the cart list')
        return False

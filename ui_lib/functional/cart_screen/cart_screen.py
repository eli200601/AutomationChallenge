from ui_lib.mapping import CartScreenLocators
from ui_lib.functional import BasePageElement


class CartScreenFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = CartScreenLocators(driver)

    def check_if_item_exist_in_cart(self, book_item_):
        print('Verify book in the cart list:')
        print(book_item_)
        cart_items = self._map.cart_items.find_element()
        for item in cart_items:
            if self._is_same_item(item, book_item_):
                print('Item exist in the cart list')
                return True
        print('Item does not exist in the cart list')
        return False

    def _is_same_item(self, item_elm, book_item):
        return str.__contains__(item_elm.text, book_item.book_name[:20])

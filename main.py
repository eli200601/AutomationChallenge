#!/usr/bin/python
# -*- coding: utf-8 -*-
from ui_lib.functional import HomeScreenFunctionality
from ui_lib.functional import ResultsScreenFunctionality
from ui_lib.functional import BookItemFunctionality
from ui_lib.functional import CartScreenFunctionality
from utils import selenium, db


if __name__ == "__main__":
    print('Begin Challenge')

    driver = selenium.get_driver()

    home_screen = HomeScreenFunctionality(driver)
    results_screen = ResultsScreenFunctionality(driver)
    book_screen = BookItemFunctionality(driver)
    cart_screen = CartScreenFunctionality(driver)

    home_screen.navigate_to_screen()
    home_screen.action_bar.search_for_text('software testing')

    results_items = results_screen.get_n_pages_results_objects(4)

    item_to_click = -3

    results_screen.focus_by_element(results_items[item_to_click].element)
    book_screen.click_add_to_cart()
    results_screen.action_bar.click_cart()

    assert cart_screen.check_if_item_exist_in_cart(results_items[item_to_click]), 'Item does not appear in cart screen'

    db.insert_books_list_to_db(results_items)

    selenium.quit_driver(driver)

    print("Finish")

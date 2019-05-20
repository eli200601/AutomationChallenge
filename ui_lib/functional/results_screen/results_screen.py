from selenium.webdriver import ActionChains

from ui_lib.functional import BasePageElement
from ui_lib.functional.action_bar import ActionBarFunctionality
from ui_lib.functional.data_types import BookItem
from ui_lib.mapping import ResultsScreenLocators
from selenium.common.exceptions import NoSuchElementException


class ResultsScreenFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = ResultsScreenLocators(driver)
        self.action_bar = ActionBarFunctionality(driver)

    def focus_by_element(self, element):
        action = ActionChains(self._driver)
        action.move_to_element(element).click().perform()

    def get_n_pages_results_objects(self, number_of_pages=1):
        print("Getting {} pages results items".format(str(number_of_pages)))
        book_items_array = []
        i = 1
        while i <= number_of_pages:
            results_items = self.get_results_list_to_objects()
            print('Found {} books in this page'.format(str(len(results_items))))
            book_items_array.extend(results_items)
            if not i == number_of_pages:
                self.go_to_next_result_page()
            else:
                print('Last iteration')
            i += 1
        print("Manage to collect {} books".format(str(len(book_items_array))))
        return book_items_array

    def go_to_next_result_page(self):
        nav_bar = self._map.navigation_bar.find_element()
        for button in nav_bar:
            if button.text == 'Next→':
                print('next page')
                button.click()

    def get_results_list_to_objects(self):
        book_items_array = []
        results_items = self._map.results_items.find_element()
        for book in results_items:
            book_item = self.get_book_item_from_element(book)
            print(book_item)
            if book_item is not None:
                book_items_array.append(book_item)
        return book_items_array

    def get_book_item_from_element(self, book):
        if book.text.__contains__('Prime Video'):
            return None
        book_name = book.find_element(*self._map.book_name.get_locator()).text
        try:
            book_author_date = book.find_element(*self._map.book_author_date.get_locator()).text
            book_author, book_date = self._parse_author_and_date(book_author_date)
        except NoSuchElementException:
            book_author, book_date = '', ''
        try:
            book_rating = book.find_element(*self._map.book_rating.get_locator()).get_attribute('aria-label')
            book_reviews = book.find_element(*self._map.book_reviews.get_locator()).text
        except NoSuchElementException:
            book_rating = ''
            book_reviews = ''
        try:
            book_price = book.find_element(*self._map.book_price.get_locator()).text
        except NoSuchElementException:
            book_price = book.find_element(*self._map.price_secondary.get_locator()).text

        book_price = self._parse_book_price(book_price)

        book_item = BookItem(book_name=book_name,
                             book_author=book_author,
                             book_date=book_date,
                             book_rating=book_rating,
                             book_reviews=book_reviews,
                             book_price=book_price,
                             element=book.find_element(*self._map.book_name.get_locator()))
        return book_item

    @staticmethod
    def _parse_author_and_date(author_date):
        try:
            author = author_date.split(' | ')[0].split('by ')[1]
            date = author_date.split(' | ')[1]
        except IndexError:
            author = ''
            date = author_date
        return author, date

    @staticmethod
    def _parse_book_price(book_price):
        return book_price.replace('\n', '.')

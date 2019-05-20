from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from enum import Enum


class LT(Enum):
    id = By.ID
    class_name = By.CLASS_NAME
    xpath = By.XPATH
    name = By.NAME
    css_selector = By.CSS_SELECTOR
    link_text = By.LINK_TEXT
    partial_link_test = By.PARTIAL_LINK_TEXT
    tag = By.TAG_NAME

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Locator(object):

    def __init__(self, type_, query_string_, parent_element_=None, multi_item_=False):
        self.type = type_
        self.query_string = query_string_
        self.parent_element = parent_element_
        self.multi_item = multi_item_

    def locator_details(self):
        return '(Locator: {}, {})'.format(self.type.value, self.query_string)

    def locator(self):
        return self.type.value, self.query_string


class SeleniumElement(object):

    def __init__(self, driver_, locator_):
        self.driver = driver_
        self.locator = locator_

    def get_locator(self):
        return self.locator.locator()

    def find_element(self):
        try:
            if self.locator.multi_item is True:
                element = self._find_elements_by_locator()
            else:
                element = self._find_element_by_locator()
            return element
        except NoSuchElementException:
            print("SeleniumElement - {} was not found!")
            raise

    def _find_element_by_locator(self):
        if self.locator.parent_element is not None:
            element = self.locator.parent_element.find_element().find_element(*self.locator.locator())
        else:
            element = self.driver.find_element(*self.locator.locator())
        return element

    def _find_elements_by_locator(self):
        if self.locator.parent_element is not None:
            elements = self.locator.parent_element.find_element().find_elements(*self.locator.locator())
        else:
            elements = self.driver.find_elements(*self.locator.locator())
        return elements

    def exists(self):
        try:
            self.find_element()
            return True
        except NoSuchElementException:
            return False
        except IndexError:
            return False

    def clear(self):
        self.find_element().clear()

    def click(self):
        self.find_element().click()

    def get_text(self):
        return self.find_element().text

    def set_text(self, text):
        self.find_element().clear()
        self.find_element().send_keys(text)

    def send_enter_key(self):
        self.find_element().send_keys(Keys.ENTER)

    def get_location(self):
        return self.find_element().location

    def get_size(self):
        return self.find_element().size

    def get_class_name(self):
        return self.find_element().get_attribute('class')

    def is_enabled(self):
        return self.find_element().is_enabled()

    def is_selected(self):
        return self.find_element().is_selected()

    def is_displayed(self):
        return self.find_element().is_displayed()

    def focus_to_element(self):
        elm = self.find_element()
        action = ActionChains(self.driver)
        action.move_to_element(elm).perform()

    def click_on_the_element_end(self):
        print('click_on_element_at_the_end by locator')
        elm = self.find_element()
        size = self.get_size()
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(elm, size['width'] - 1, size['height'] - 1)
        action.click()
        action.perform()

    def add_boarder_to_element(self):
        self.driver.execute_script('arguments[0].style.border = "5px solid red"', self.find_element())

    def remove_boarder_from_element(self):
        self.driver.execute_script('arguments[0].style.border = ""', self.find_element())

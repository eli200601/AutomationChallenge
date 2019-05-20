from ui_lib.functional import BasePageElement
from ui_lib.mapping import HomeScreenLocators
from ui_lib.functional.action_bar import ActionBarFunctionality


class HomeScreenFunctionality(BasePageElement):

    def __init__(self, driver):
        BasePageElement.__init__(self, driver)
        self._map = HomeScreenLocators(driver)
        self.action_bar = ActionBarFunctionality(driver)

    def navigate_to_screen(self):
        self._start(self._map.path)

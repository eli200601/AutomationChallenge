class BasePageElement(object):
    def __init__(self, driver):
        self._driver = driver

    def _start(self, url):
        print("Navigating chrome to URL: " + url)
        self._driver.get(url)

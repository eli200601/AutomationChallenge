class BasePageElement(object):

    def __init__(self, driver):
        self._driver = driver

    def _start(self, url):
        print("starting chrome driver URL=" + url)
        self._driver.get(url)

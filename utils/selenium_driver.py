from selenium import webdriver


def get_chrome_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--ignore-ssl-errors=true")
    chrome_options.add_argument("--ssl-protocol=any")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options.to_capabilities()


def get_driver():
    print('Get driver: setup chrome driver')
    print("starting chrome web driver")
    driver = webdriver.Chrome(desired_capabilities=get_chrome_options())
    print("Local chrome driver has started")
    driver.implicitly_wait(1)
    return driver


def quit_driver(driver):
    driver.quit()

from venv import logger
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator_type, locator):
        try:
            self.browser.find_element(locator_type, locator)
        except NoSuchElementException as ex:
            return False
        return True

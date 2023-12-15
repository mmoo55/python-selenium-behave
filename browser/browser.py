from selenium import webdriver

from browser.chrome import Chrome
from browser.edge import Edge
from browser.firefox import Firefox
from browser.headless import Headless


class Browser:

    def __init__(self):
        self.driver = None

    def choose_browser(self, browser: str = "chrome"):
        try:
            if browser.lower() == "chrome":
                self.driver = Chrome().open_chrome()
            elif browser.lower() == "firefox":
                self.driver = Firefox().start_firefox()
            elif browser.lower() == "edge":
                self.driver = Edge().start_edge()
            elif browser.lower() == "safari":
                self.driver = webdriver.Safari()
            elif browser.lower() == "headless":
                self.driver = Headless().start_headless()
            self.vars = {}
            return self.driver
        except Exception as e:
            print(e)
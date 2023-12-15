import chromedriver_autoinstaller
from selenium import webdriver


class Chrome:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def open_chrome(self):
        """
        Open Chrome
        :return: webdriver
        """
        driver = webdriver.Chrome()
        driver.implicitly_wait(25)
        driver.set_page_load_timeout(25)
        driver.maximize_window()
        return driver

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Headless:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def start_headless(self):
        """
        Open Chrome in Headless mode
        :return: webdriver
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver
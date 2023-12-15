import edgedriver_autoinstaller
from selenium import webdriver


class Edge:

    def __init__(self):
        edgedriver_autoinstaller.install()

    def start_edge(self):
        """
        Open Edge
        :return: webdriver
        """
        driver = webdriver.Edge()
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver
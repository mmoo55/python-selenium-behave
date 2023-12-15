from browser.browser import Browser

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util.get_env import load_env

class Session:
    _instance = None
    _browser = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Session()
        return cls._instance

    def __init__(self):
        self._browser = Browser().choose_browser(load_env.get_browser())

    def get_browser(self):
        return self._browser

    def load_website(self):
        self._browser.get()

    def close_session(self):
        self._browser.quit()
        self._instance = None

    def accept_alert(self):
        self._browser.switch_to.alert.accept()

    def get_text_alert(self):
        return self._browser.switch_to.alert.text

    def wait_alert_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(self._browser, 10)
        explicit_wait.until(EC.alert_is_present())

session = Session.get_instance()
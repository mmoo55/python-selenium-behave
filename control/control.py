from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from session.session import session


class Control:
    _session_handler = None

    @classmethod
    def set_session_handler(cls, session_handler):
        cls._session_handler = session_handler

    def __init__(self, type, locator):
        """
        Startup constructor of the Control class.
        :param type: Type of selector to enter, it can be of type:
                    id, name, link text, css selector, partial link text, class name, xpath.
        :param locator: element to reference the web page.
        :return:
        """
        self.type = type
        self.locator = locator
        self.control: WebElement = None
        # self.driver = session_instance.get_browser()
        self.driver = None

    def set_driver(self):
        self.driver = self._session_handler.get_browser()

    def find(self):
        self.set_driver()
        self.control = self.driver.find_element(self.type, self.locator)

    def scroll(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.control)

    def mouse_actions(self):
        return ActionChains(self.driver)

    def click(self):
        self.find()
        print("Click on -> {} ".format(self.locator))
        self.control.click()

    def rigth_click(self):
        self.find()
        self.scroll()
        self.mouse_actions().context_click(self.control).perform()

    def double_click(self):
        self.find()
        self.scroll()
        self.mouse_actions().double_click(self.control).perform()

    def control_is_displayed(self):
        try:
            self.find()
            return self.control.is_displayed()
        except:
            return False

    def get_text(self):
        self.find()
        return self.control.text

    def get_attribute(self, type_atribute):
        self.find()
        return self.control.get_attribute(type_atribute)

    def wait_control_is_not_in_the_page(self):
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.visibility_of_element_located(self.control))

    def move__mouse_to_element(self):
        self.find()
        # self.scroll()
        print("Moving to -> {} ".format(self.locator))
        self.mouse_actions().move_to_element(self.control).perform()

    def move_mouse_to_element_and_click(self):
        self.find()
        # self.scroll()
        print("Moving and clicking to -> {} ".format(self.locator))
        self.mouse_actions().move_to_element(self.control).click().perform()

    def send_file(self, path: str):
        self.find()
        print("Typing in {} the path of the file -> {} ".format(self.control, path))
        self.control.send_keys(path)
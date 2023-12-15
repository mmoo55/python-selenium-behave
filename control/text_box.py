from control.control import Control
from selenium.webdriver.common.keys import Keys

class TextBox(Control):

    def __init__(self, type, locator):
        super(TextBox, self).__init__(type, locator)

    def set_text(self, text: str):
        self.find()
        print("Typing in {} this text -> {} ".format(self.control, text))
        self.control.send_keys(text)

    def set_text_clear(self, text: str):
        self.find()
        print("Typing in {} this text -> {} ".format(self.control, text))
        self.control.clear()
        self.control.send_keys(text)

    def clear_textbox(self):
        self.find()
        print("Cleaning {}".format(self.control))
        self.control.clear()

    def set_text_tab(self, text: str):
        self.find()
        print("Typing in {} this text -> {} ".format(self.control, text))
        self.control.send_keys(text)
        self.control.send_keys(Keys.TAB)

    def set_text_enter(self, text: str):
        self.find()
        print("Typing in {} this text -> {} ".format(self.control, text))
        self.control.send_keys(text)
        self.control.send_keys(Keys.ENTER)
from selenium.webdriver.common.by import By

from control.button import Button
from control.text_box import TextBox
from control.label import Label



class LoginPage:

    def __init__(self):

        # HOME
        self.login_label = Label(By.XPATH, "//*[contains(@src, 'pagelogin.png')]")

        self.email_textbox = TextBox(By.ID, "ctl00_MainContent_LoginControl1_TextBoxEmail")
        self.password_textbox = TextBox(By.ID, "ctl00_MainContent_LoginControl1_TextBoxPassword")
        self.login_button = Button(By.ID, "ctl00_MainContent_LoginControl1_ButtonLogin")

    def login(self, username, password):
        self.email_textbox.set_text(username)
        self.password_textbox.set_text(password)
        self.login_button.click()
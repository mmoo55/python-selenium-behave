from selenium.webdriver.common.by import By

from control.button import Button


class MainPage:

    def __init__(self):
        self.logout_button = Button(By.ID, "ctl00_HeaderTopControl1_LinkButtonLogout")
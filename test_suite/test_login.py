from test_suite.test_base import TestBase


class LoginTest(TestBase):

    def test_login(self):

        self.login_section.login_label.click()
        self.login_section.email_textbox.set_text(self.USERNAME)
        self.login_section.password_textbox.set_text(self.PASSWORD)
        self.login_section.login_button.click()

        self.assertTrue(self.main_section.logout_button.control_is_displayed(), "No esta visible")
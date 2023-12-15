import allure
from allure_commons.types import AttachmentType

from session.session import session
from test_suite.test_base import TestBase

@allure.severity(allure.severity_level.NORMAL)
class LoginTest(TestBase):

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):

        self.login_section.login_label.click()
        self.login_section.email_textbox.set_text(self.USERNAME)
        self.login_section.password_textbox.set_text(self.PASSWORD)
        self.login_section.login_button.click()

        allure.attach(session.get_browser().get_screenshot_as_png(), name="testLoginScreen",
                      attachment_type=AttachmentType.PNG)
        self.assertTrue(self.main_section.logout_button.control_es_visible(), "No esta visible")
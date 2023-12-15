import unittest

from util.get_env import load_env
# from session.session import Session
from session.session import session
from util.extra_functions import ExtraFunctions

# Ingresar al Home
from page.login_page import LoginPage

# Main page
from page.main_page import MainPage

###### ALLURE ######
# import allure
# import pytest

# session_instance = Session.get_instance()

class TestBase(unittest.TestCase):
    # Login
    login_section = LoginPage()

    main_section = MainPage()

    # FUNCIONES EXTRA
    # funcion_extra = FuncionesExtra()

    # Obteniendo los datos base
    USERNAME = load_env.get_username()
    PASSWORD = load_env.get_password()

    def setUp(self):
        # Configurando Navegador
        # self.session.get_browser().get(load_env.get_url())
        session.get_browser().get(load_env.get_url())

        # Login
        # self.login_section.ingresar_login(self.USERNAME, self.PASSWORD)

        # self.session.get_instance().get_browser().implicitly_wait(5)
        session.get_instance().get_browser().implicitly_wait(5)

    def tearDown(self):
        # self.session.get_instance().close_session()
        session.get_instance().close_session()
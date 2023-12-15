from os import getenv

from dotenv import load_dotenv
from pathlib import Path

from config import basedir

class GetEnv:
    _get_env = None

    # DATOS BASE
    _url = None
    _browser = None

    # DATOS LOGIN
    _username = None
    _password = None

    def __init__(self):
        # global url, browser
        dotenv_path = Path(f"{basedir}/resources/base_data/.env")
        load_dotenv(dotenv_path=dotenv_path)

        # DATOS BASE
        self._url = getenv("URL")
        self._browser = getenv("BROWSER")

        # DATOS PARA LA PRUEBA
        self._username = getenv("USERNAME_LOGIN")
        self._password = getenv("PASSWORD_LOGIN")

        print("DATOS:   ", self._url, self._browser, self._username, self._password)

    @classmethod
    def get_instance(cls):
        if cls._get_env is None:
            cls._get_env = GetEnv()
        return cls._get_env

    def get_url(self):
        return self._url

    def get_browser(self):
        return self._browser

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

load_env = GetEnv.get_instance()
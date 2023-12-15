from test_suite.test_base import TestBase

from ddt import ddt, data, unpack

from util.funciones_excel import FuncionesExcel
from util.funciones_extra import FuncionesExtra


@ddt
class LoginTestDDT(TestBase):
    # archivo_excel = r"C:\Users\gandrade\PycharmProjects\Curso_selenium\resources\excel\login.xlsx"
    archivo_excel = FuncionesExtra().obtener_ruta_archivo("login.xlsx")

    @data(*FuncionesExcel().obtener_datos(archivo_excel, "LOGIN"))
    @unpack
    def test_login_ddt(self, numero_fila, username, password):

        self.login_section.login_label.click()
        self.login_section.email_textbox.set_text(username)
        self.login_section.password_textbox.set_text(password)
        self.login_section.login_button.click()
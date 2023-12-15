from control.control import Control


class Menu(Control):

    def __init__(self, type, *args):
        super(Menu, self).__init__(type, args[0])
        self.args = args

    def seleccionar_menu(self):
        self.find()
        self.click()
        for a in self.args[1: len(self.args) - 1]:
            self.locator = a
            self.desplazar_mouse_a_elemento()
        self.locator = self.args[len(self.args) -1]
        self.desplazar_mouse_a_elemento_click()
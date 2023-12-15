from control.control import Control

class Button(Control):
    def __init__(self, type, locator):
        super(Button, self).__init__(type, locator)
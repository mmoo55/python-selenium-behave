from control.control import Control


class Label(Control):

    def __init__(self, type, locator):
        super(Label, self).__init__(type, locator)
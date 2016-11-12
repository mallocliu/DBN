from PyQt5.QtWidgets import QMainWindow

from Output import Ui_Output


class OutPutWindow(QMainWindow, Ui_Output):
    def __init__(self, parent=None):
        super(OutPutWindow, self).__init__(parent)
        self.setupUi(self)

from PyQt5.QtWidgets import QMainWindow

from Output import Ui_Output


class OutPutWindow(Ui_Output):
    def __init__(self):
        super(OutPutWindow, self).setupUi(QMainWindow)

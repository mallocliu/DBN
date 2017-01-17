from PyQt5 import QtCore


class TrainThread(QtCore.QThread):
    def __init__(self, wd, parent=None):
        super().__init__(parent)
        self.window = wd

    def run(self):
        self.window.dbn.pretrain_DBN(self.window)


class TestThread(QtCore.QThread):
    def __init__(self, wd, parent=None):
        super().__init__(parent)
        self.window = wd

    def run(self):
        self.window.dbn.test_DBN(self.window)

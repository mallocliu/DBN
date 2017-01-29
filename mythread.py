from PyQt5 import QtCore
from DBN import runDBN


class TrainThread(QtCore.QThread):
    def __init__(self, dbn: runDBN, parent=None):
        super().__init__(parent)
        self.dbn = dbn

    def run(self):
        self.dbn.pretrain_DBN()


class TestThread(QtCore.QThread):
    evaluate_dbn_finished = QtCore.pyqtSignal(list, int, list)

    def __init__(self, dbn: runDBN, pos, ws, column, header, parent=None):
        super().__init__(parent)
        self.dbn = dbn
        self.ws = ws
        self.column = column
        self.pos = pos
        self.header = header

    def run(self):
        self.dbn.datasets.append(self.dbn.load_testdata(self.ws, self.column))
        label = self.dbn.test_DBN()
        self.evaluate_dbn_finished.emit(label, self.pos, self.header)

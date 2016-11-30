import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    # ui.push_retest.clicked.connect(ui.lineEdit_result.clear)
    # ui.push_retest.clicked.connect(outui.textEdit.clear)
    # ui.push_retest.clicked.connect(dbn.resetTest)
    sys.exit(app.exec_())

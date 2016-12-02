import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())

import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class SelectDialog(QDialog):
    def __init__(self, parent=None):
        super(SelectDialog, self).__init__(parent)
        self.path = os.getcwd()
        self.initUI()
        self.setWindowTitle("选择")
        self.resize(240, 100)

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("路径："), 0, 0)
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setFixedWidth(200)
        self.pathLineEdit.setText(self.path)
        grid.addWidget(self.pathLineEdit, 0, 1)
        button = QPushButton("更改")
        button.clicked.connect(self.changePath)
        grid.addWidget(button, 0, 2)
        
        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        grid.addWidget(buttonBox, 2, 1)
        self.setLayout(grid)

    def changePath(self):
        open = QFileDialog()
        self.path=open.getOpenFileName()
        self.pathLineEdit.setText(self.path[0])

    def getPath(self):
        return self.path


class SaveDialog(QDialog):
    def __init__(self, parent=None):
        super(SaveDialog, self).__init__(parent)
        self.path = os.getcwd()
        self.initUI()
        self.setWindowTitle("选择")
        self.resize(240, 100)

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(QLabel("路径："), 0, 0)
        self.pathLineEdit = QLineEdit()
        self.pathLineEdit.setFixedWidth(200)
        self.pathLineEdit.setText(self.path)
        grid.addWidget(self.pathLineEdit, 0, 1)
        button = QPushButton("更改")
        button.clicked.connect(self.changePath)
        grid.addWidget(button, 0, 2)

        buttonBox = QDialogButtonBox()
        buttonBox.setOrientation(Qt.Horizontal)  # 设置为水平方向
        buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)  # 确定
        buttonBox.rejected.connect(self.reject)  # 取消
        grid.addWidget(buttonBox, 2, 1)
        self.setLayout(grid)

    def changePath(self):
        open = QFileDialog(self, 'Save File...', os.getcwd(), 'All Files (*);;Text Files (*.txt)')
        self.path = open.getSaveFileName()
        self.pathLineEdit.setText(self.path[0])

    def getPath(self):
        return self.path[0]

    def printout(self, text):
        with open(self.getPath(), 'w') as saveFile:
            saveFile.write(str(text))

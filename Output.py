# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Output.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Output(object):
    def setupUi(self, Output):
        Output.setObjectName("Output")
        Output.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Output)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Output)
        QtCore.QMetaObject.connectSlotsByName(Output)

    def retranslateUi(self, Output):
        _translate = QtCore.QCoreApplication.translate
        Output.setWindowTitle(_translate("Output", "评估报告"))

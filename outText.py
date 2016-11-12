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

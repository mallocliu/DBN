from PyQt5.QtWidgets import QApplication, QMainWindow

from DBN import *
from Window import MainWindow
from dialog import SelectDialog, SaveDialog
from outText import OutPutWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dbn = runDBN()

    window = QMainWindow()
    outwindow = QMainWindow()
    ui = MainWindow(window)
    outui = OutPutWindow(outwindow)

    # ui.setupUi(window)
    # outui.setupUi(outwindow)
    ui.comboBox_indexLevel.addItem('2', 2)
    dialog_selectTrain = SelectDialog()
    dialog_selectTest = SelectDialog()
    dialog_save = SaveDialog()
    window.show()

    ui.pushButton_selectTrain.clicked.connect(dialog_selectTrain.exec)
    ui.pushButton_selectEvaluate.clicked.connect(dialog_selectTest.exec)
    ui.push_printresult.clicked.connect(dialog_save.exec)

    # ui.push_editIndex.clicked.connect(ui.preset)
    ui.push_editIndex.clicked.connect(lambda: dbn.setIndexname(ui.getIndexName()))

    # ui.push_resumeIndex.clicked.connect(ui.treeReset)
    ui.push_resumeIndex.clicked.connect(dbn.reset)
    # ui.push_resumeIndex.clicked.connect(ui.comboBox_indexName.clear)
    # ui.push_resumeIndex.clicked.connect(ui.lineEdit_result.clear)
    ui.push_resumeIndex.clicked.connect(outui.textEdit.clear)

    ui.push_retest.clicked.connect(ui.lineEdit_result.clear)
    ui.push_retest.clicked.connect(outui.textEdit.clear)
    ui.push_retest.clicked.connect(dbn.reset)

    ui.lineEdit_indexName.setText(ui.comboBox_indexName.currentText())
    ui.lineEdit_indexName_2.setText(ui.lineEdit_indexName.text())

    ui.lineEdit_indexWeight.setText('1')
    ui.comboBox_indexName.currentTextChanged.connect(
        lambda: ui.lineEdit_indexName.setText(ui.comboBox_indexName.currentText()))
    ui.lineEdit_indexName.textChanged.connect(lambda: ui.lineEdit_indexName_2.setText(ui.lineEdit_indexName.text()))
    ui.command_startTrain.clicked.connect(
        lambda: dbn.pretrain_DBN(ui, dialog_selectTrain.getPath(), ui.comboBox_indexName.currentIndex()))
    ui.command_startEvaluate.clicked.connect(lambda: dbn.test_DBN(ui, outui, dialog_selectTest))
    dialog_save.accepted.connect(lambda: dialog_save.printout(outui.textEdit.toPlainText()))
    ui.push_showresult.clicked.connect(outwindow.show)
    sys.exit(app.exec_())

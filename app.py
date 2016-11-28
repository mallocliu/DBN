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

    dialog_selectTrain = SelectDialog()
    dialog_selectTest = SelectDialog()
    dialog_save = SaveDialog()
    window.show()
    ui.pushButton_selectTrain.clicked.connect(dialog_selectTrain.exec)
    ui.pushButton_selectEvaluate.clicked.connect(dialog_selectTest.exec)
    ui.push_printresult.clicked.connect(dialog_save.exec)

    dialog_save.accepted.connect(lambda: dialog_save.printout(outui.textEdit.toPlainText()))
    ui.push_showresult.clicked.connect(outwindow.show)

    ui.push_editIndex.clicked.connect(lambda: dbn.setIndexname(ui.getIndexName()))
    ui.push_editIndex.clicked.connect(lambda: dbn.setRootIndex(ui.getRootIndexName()))

    ui.push_retrain.clicked.connect(ui.lineEdit_result.clear)
    ui.push_retrain.clicked.connect(outui.textEdit.clear)
    ui.push_retrain.clicked.connect(lambda: dbn.retrain(ui.getIndexName()))

    ui.push_retest.clicked.connect(ui.lineEdit_result.clear)
    ui.push_retest.clicked.connect(outui.textEdit.clear)
    ui.push_retest.clicked.connect(dbn.resetTest)

    ui.command_startTrain.clicked.connect(
        lambda: dbn.pretrain_DBN(ui, dialog_selectTrain.getPath(), ui.comboBox_indexName.currentIndex()))
    ui.command_startEvaluate.clicked.connect(
        lambda: dbn.test_DBN(ui, outui, dialog_selectTest.getPath(), ui.comboBox_testIndex.currentIndex()))

    sys.exit(app.exec_())

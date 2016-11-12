from PyQt5.QtWidgets import QApplication, QMainWindow
from dialog import SelectDialog, SaveDialog
from mainwindow import *
from outText import *
from DBN import *


def editBox(tree, index, ui, dbn):
    root = tree.topLevelItem(0)
    dbn.rootindex = root.text(0)
    treeitem = [root]
    ui.comboBox_indexName.clear()
    dbn.indexname = []
    for times in range(index - 1):
        # treeitem holds all the valid level 2 index
        treeitem = [node.child(i) for node in treeitem for i in range(node.childCount()) if
                    node.child(i).text(0) != '//']

    for val, node in enumerate(treeitem):
        ui.comboBox_indexName.insertItem(val, node.text(0))
        dbn.indexname.append((str(node.text(0)), 0))


def pre_set(ui, dbn):
    index = ui.comboBox_indexLevel.currentData()
    editBox(ui.tree_index, index, ui, dbn)


def treeReset(tree, dbn):
    dbn = runDBN()
    resetStr = '/'
    root = tree.topLevelItem(0)
    root.setText(0, resetStr)
    treeitem = [root]
    for level in range(2):
        treeitem = [node.child(i) for node in treeitem for i in range(node.childCount())]
        resetStr += '/'
        for node in treeitem:
            node.setText(0, resetStr)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    outwindow = QMainWindow()
    ui = Ui_MainWindow()
    outui = Ui_Output()
    ui.setupUi(window)
    outui.setupUi(outwindow)
    ui.comboBox_indexLevel.addItem('2', 2)
    dialog_selectTrain = SelectDialog()
    dialog_selectTest = SelectDialog()
    dialog_save = SaveDialog()
    window.show()
    ui.pushButton_selectTrain.clicked.connect(dialog_selectTrain.exec)
    ui.pushButton_selectEvaluate.clicked.connect(dialog_selectTest.exec)
    ui.push_printresult.clicked.connect(dialog_save.exec)
    dbn = runDBN()
    ui.push_editIndex.clicked.connect(lambda: pre_set(ui, dbn))
    ui.push_resumeIndex.clicked.connect(lambda: treeReset(ui.tree_index, dbn))
    ui.push_resumeIndex.clicked.connect(ui.comboBox_indexName.clear)
    ui.push_resumeIndex.clicked.connect(ui.lineEdit_result.clear)
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
    ui.command_startTrain.clicked.connect(lambda: dbn.pretrain_DBN(ui, dialog_selectTrain))
    ui.command_startEvaluate.clicked.connect(lambda: dbn.test_DBN(ui, outui, dialog_selectTest))
    dialog_save.accepted.connect(lambda: dialog_save.printout(outui.textEdit.toPlainText()))
    ui.push_showresult.clicked.connect(outwindow.show)
    sys.exit(app.exec_())

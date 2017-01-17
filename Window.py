import json
from collections import deque, OrderedDict

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from DBN import runDBN
from dialog import SelectDialog, SaveDialog
from mainwindow import Ui_MainWindow
from mythread import TrainThread, TestThread
from outText import OutPutWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, window):
        super().setupUi(window)
        self.indexWidget = []
        self.indexname = set()
        self.indexweight = []
        self.level = 0
        self.dbn = runDBN()

        self.trThread = TrainThread(self)
        self.teThread = TestThread(self)

        self.lineEdit_batch.setText('4')
        self.lineEdit_lr.setText('0.01')
        self.lineEdit_epoch.setText('100')

        self.dialog_loadindex = SelectDialog()  # select index file
        self.push_selectIndex.clicked.connect(self.loadindex)
        self.push_editIndex.clicked.connect(self.setindex)

        self.push_editIndex.clicked.connect(lambda: self.dbn.setIndexname(self.indexname))

        # self.command_startEvaluate.clicked.connect(
        #     lambda: self.lineEdit_indexName_2.setText(self.comboBox_testIndex.currentText()))

        self.dialog_selectTrain = SelectDialog()
        self.dialog_selectTest = SelectDialog()
        self.dialog_save = SaveDialog()

        self.pushButton_selectTrain.clicked.connect(self.dialog_selectTrain.exec)
        self.pushButton_selectEvaluate.clicked.connect(self.dialog_selectTest.exec)
        self.push_printresult.clicked.connect(self.dialog_save.exec)

        self.outwindow = QMainWindow()
        self.outui = OutPutWindow(self.outwindow)
        self.dialog_save.accepted.connect(lambda: self.dialog_save.printout(self.outui.textEdit.toPlainText()))
        self.push_showresult.clicked.connect(self.outwindow.show)

        self.command_startTrain.clicked.connect(self.trThread.start)
        self.command_startEvaluate.clicked.connect(self.teThread.start)

        self.push_retest.clicked.connect(self.retest)

    def getRootIndexName(self):
        root = self.tree_index.topLevelItem(0)
        return root.text(0)

    def buildTree(self, rootindex, root):
        q = deque()
        q.append((rootindex, root))
        while q:
            node, nodewidget = q.popleft()  # node is a dict, nodewidget is a QtreeWidgetItem
            if len(node) > 1:
                for eachitem in node.keys():
                    if not eachitem == 'w':
                        newwidget = QtWidgets.QTreeWidgetItem()
                        newwidget.setText(0, eachitem)
                        newwidget.setText(1, str(node[eachitem]['w']))
                        nodewidget.addChild(newwidget)
                        q.append((node[eachitem], newwidget))
        self.tree_index.addTopLevelItem(root)

    def loadindex(self):
        self.dialog_loadindex.exec()
        with open(self.dialog_loadindex.getPath(), 'r') as f:
            index = json.load(f, object_pairs_hook=OrderedDict)
            rootindex = list(index.keys())[0]
            root = QtWidgets.QTreeWidgetItem()
            root.setText(0, rootindex)
            root.setText(1, str(index[rootindex]['w']))
            self.buildTree(index[rootindex], root)

    def setindex(self):
        root = self.tree_index.topLevelItem(0)
        treeitem = [root]
        level = 1
        while treeitem:
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount())]
            level += 1
            if not treeitem[0].childCount():
                for node in treeitem:
                    parent = node.parent()
                    if not parent.text(0) in self.indexname:
                        self.indexname.add(parent.text(0))
                        self.indexweight.append(parent.text(1))
                        self.indexWidget.append(parent)
                break

        for val, node in enumerate(self.indexWidget):
            self.comboBox_indexName.insertItem(val, node.text(0))
            self.comboBox_testIndex.insertItem(val, node.text(0))

        self.level = level
        self.comboBox_indexLevel.insertItem(0, str(level - 1))

    def get_all_level_k_widget(self, k: int):
        '''
        :param k: level to search
        :return:
        '''
        root = self.tree_index.topLevelItem(0)
        treeitem = [root]
        level = 1
        while level < k:
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount())]
        return treeitem

    # def using_trainthread(self):
    #     thread = TrainThread(self)
    #     thread.start()
    #
    # def using_testthread(self):
    #     thread = TestThread(self)
    #     thread.start()

    def retest(self):
        self.outui.textEdit.clear()
        count = self.comboBox_testIndex.count()
        for index in range(count):
            text = self.comboBox_testIndex.itemText(index).split()
            self.comboBox_testIndex.setItemText(index, text[0])
        self.dbn.resetTest()

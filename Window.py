import json
from collections import deque, OrderedDict

from PyQt5 import QtWidgets

from dialog import SelectDialog
from mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, QMainWindow):
        super().setupUi(QMainWindow)
        self.dialog_loadindex = SelectDialog()  # select index file
        self.push_editIndex.clicked.connect(self.setindex)
        self.command_startEvaluate.clicked.connect(
            lambda: self.lineEdit_indexName_2.setText(self.comboBox_testIndex.currentText()))
        self.push_selectIndex.clicked.connect(self.loadindex)
        self.indexWidget = []
        self.indexname = set()
        self.level = 0

    def preset(self):
        treeitem = self.getIndexTree()
        self.comboBox_indexName.clear()
        self.comboBox_testIndex.clear()
        for val, node in enumerate(treeitem):
            self.comboBox_indexName.insertItem(val, node.text(0))
            self.comboBox_testIndex.insertItem(val, node.text(0))

    def getIndexTree(self):
        index = self.comboBox_indexLevel.currentData()
        root = self.tree_index.topLevelItem(0)
        treeitem = [root]
        for times in range(index - 1):
            # treeitem holds all the valid level 2 index
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount()) if
                        node.child(i).text(0) != '//']
        return treeitem

    def getIndexName(self):
        treeitem = self.getIndexTree()
        name = [str(node.text(0)) for node in treeitem]
        return name

    def getRootIndexName(self):
        root = self.tree_index.topLevelItem(0)
        return root.text(0)

    def treeReset(self):
        resetStr = '/'
        root = self.tree_index.topLevelItem(0)
        root.setText(0, resetStr)
        treeitem = [root]
        for level in range(2):
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount())]
            resetStr += '/'
            for node in treeitem:
                node.setText(0, resetStr)

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
            print(index)
            rootindex = list(index.keys())[0]
            root = QtWidgets.QTreeWidgetItem()
            root.setText(0, rootindex)
            root.setText(1, str(index[rootindex]['w']))
            self.buildTree(index[rootindex], root)

    def setindex(self):
        root = self.tree_index.topLevelItem(0)
        treeitem = [root]
        level = 0
        while treeitem:
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount())]
            level += 1
            if not treeitem[0].childCount():
                for node in treeitem:
                    parent = node.parent()
                    if not parent.text(0) in self.indexname:
                        self.indexname.add(parent.text(0))
                        self.indexWidget.append(parent)
                break

        for val, node in enumerate(self.indexWidget):
            self.comboBox_indexName.insertItem(val, node.text(0))

        self.comboBox_indexLevel.insertItem(0, str(level))

from mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, QMainWindow):
        super().setupUi(QMainWindow)
        self.push_editIndex.clicked.connect(self.preset)
        self.push_resumeIndex.clicked.connect(self.treeReset)

        self.push_resumeIndex.clicked.connect(self.comboBox_indexName.clear)
        self.push_resumeIndex.clicked.connect(self.comboBox_testIndex.clear)
        self.push_resumeIndex.clicked.connect(self.lineEdit_result.clear)

        self.command_startEvaluate.clicked.connect(
            lambda: self.lineEdit_indexName_2.setText(self.comboBox_testIndex.currentText()))

        self.comboBox_indexLevel.addItem('2', 2)
        self.lineEdit_indexWeight.setText('1')

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

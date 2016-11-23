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
        self.push_reloadIndex.clicked.connect(self.reloading)
        self.push_save.clicked.connect(self.save)

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

    def reloadlv1(self, s):
        root = self.tree_index.topLevelItem(0)
        root.setText(0, s)

    def reloadlv2(self, s, index):
        root = self.tree_index.topLevelItem(0)
        root.child(eval(index)).setText(0, s)

    def reloadlv3(self, s, index1, index2):
        root = self.tree_index.topLevelItem(0)
        lv2child = root.child(eval(index1))
        lv3child = lv2child.child(eval(index2))
        lv3child.setText(0, s)

    def reloading(self):
        import os
        filename = os.path.join(os.getcwd(), 'log.txt')
        if os.path.exists(filename):
            if os.path.isfile(filename):
                with open(filename, mode='rt') as f:
                    lines = f.readlines()
                    for line in lines:
                        word = line.split()
                        if word[0] == 'Level1:':
                            self.reloadlv1(word[1])
                        elif word[0] == 'Level2:':
                            self.reloadlv2(word[1], word[2])
                        elif word[0] == 'Level3:':
                            self.reloadlv3(word[1], word[2], word[3])
                        elif word[0] == 'NodeNum:':
                            word.pop(0)
                            if word:
                                self.checkBox_lv1.click()
                                self.lineEdit_lv1.setText(word[0])
                            word.pop(0)
                            if word:
                                self.checkBox_lv2.click()
                                self.lineEdit_lv2.setText(word[0])
                            word.pop(0)
                            if word:
                                self.checkBox_lv3.click()
                                self.lineEdit_lv3.setText(word[0])
                self.preset()

    def save(self):
        with open('log.txt', mode='w+') as f:
            root = self.tree_index.topLevelItem(0)

            text = ['Level1: ' + root.text(0) + '\n']
            treeitem = [root]

            nullchar = '//'
            treeitem = [node.child(i) for node in treeitem for i in range(node.childCount()) if
                        node.child(i).text(0) != nullchar]
            tmptext = ['Level2: ' + node.text(0) + ' {}\n'.format(index) for index, node in
                       enumerate(treeitem)]
            text.extend(tmptext)

            nullchar += '/'
            treeitem = [(node.child(i), index, i) for index, node in enumerate(treeitem) for i in
                        range(node.childCount())
                        if node.child(i).text(0) != nullchar]
            tmptext = ['Level3: ' + node[0].text(0) + ' {} {}\n'.format(node[1], node[2]) for node in
                       treeitem]
            text.extend(tmptext)

            text.extend('NodeNum:')
            if self.checkBox_lv1.isChecked():
                text.extend(' ' + str(self.lineEdit_lv1.text()))
            if self.checkBox_lv2.isChecked():
                text.extend(' ' + str(self.lineEdit_lv2.text()))
            if self.checkBox_lv3.isChecked():
                text.extend(' ' + str(self.lineEdit_lv3.text()))
            f.writelines(text)

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 539)
        MainWindow.setDocumentMode(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.MainTitle = QtWidgets.QLabel(self.centralWidget)
        self.MainTitle.setGeometry(QtCore.QRect(270, 20, 461, 41))
        self.MainTitle.setTextFormat(QtCore.Qt.RichText)
        self.MainTitle.setScaledContents(False)
        self.MainTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.MainTitle.setWordWrap(False)
        self.MainTitle.setObjectName("MainTitle")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(390, 100, 551, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_train = QtWidgets.QWidget()
        self.tab_train.setObjectName("tab_train")
        self.label_indexName = QtWidgets.QLabel(self.tab_train)
        self.label_indexName.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_indexName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_indexName.setObjectName("label_indexName")
        self.groupBox_dbn = QtWidgets.QGroupBox(self.tab_train)
        self.groupBox_dbn.setGeometry(QtCore.QRect(220, 120, 311, 241))
        self.groupBox_dbn.setCheckable(True)
        self.groupBox_dbn.setChecked(False)
        self.groupBox_dbn.setObjectName("groupBox_dbn")
        self.label = QtWidgets.QLabel(self.groupBox_dbn)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit_lr = QtWidgets.QLineEdit(self.groupBox_dbn)
        self.lineEdit_lr.setGeometry(QtCore.QRect(110, 20, 51, 16))
        self.lineEdit_lr.setObjectName("lineEdit_lr")
        self.lineEdit_epoch = QtWidgets.QLineEdit(self.groupBox_dbn)
        self.lineEdit_epoch.setGeometry(QtCore.QRect(110, 50, 51, 16))
        self.lineEdit_epoch.setObjectName("lineEdit_epoch")
        self.label_2 = QtWidgets.QLabel(self.groupBox_dbn)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_dbn)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 71, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_batch = QtWidgets.QLineEdit(self.groupBox_dbn)
        self.lineEdit_batch.setGeometry(QtCore.QRect(110, 80, 51, 16))
        self.lineEdit_batch.setObjectName("lineEdit_batch")
        self.groupBox_nodeNum = QtWidgets.QGroupBox(self.groupBox_dbn)
        self.groupBox_nodeNum.setGeometry(QtCore.QRect(10, 110, 161, 121))
        self.groupBox_nodeNum.setObjectName("groupBox_nodeNum")
        self.checkBox_lv1 = QtWidgets.QCheckBox(self.groupBox_nodeNum)
        self.checkBox_lv1.setGeometry(QtCore.QRect(30, 30, 71, 16))
        self.checkBox_lv1.setObjectName("checkBox_lv1")
        self.lineEdit_lv1 = QtWidgets.QLineEdit(self.groupBox_nodeNum)
        self.lineEdit_lv1.setGeometry(QtCore.QRect(100, 30, 51, 16))
        self.lineEdit_lv1.setText("")
        self.lineEdit_lv1.setObjectName("lineEdit_lv1")
        self.checkBox_lv2 = QtWidgets.QCheckBox(self.groupBox_nodeNum)
        self.checkBox_lv2.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.checkBox_lv2.setObjectName("checkBox_lv2")
        self.lineEdit_lv2 = QtWidgets.QLineEdit(self.groupBox_nodeNum)
        self.lineEdit_lv2.setGeometry(QtCore.QRect(100, 60, 51, 16))
        self.lineEdit_lv2.setObjectName("lineEdit_lv2")
        self.checkBox_lv3 = QtWidgets.QCheckBox(self.groupBox_nodeNum)
        self.checkBox_lv3.setGeometry(QtCore.QRect(30, 90, 71, 16))
        self.checkBox_lv3.setObjectName("checkBox_lv3")
        self.lineEdit_lv3 = QtWidgets.QLineEdit(self.groupBox_nodeNum)
        self.lineEdit_lv3.setGeometry(QtCore.QRect(100, 90, 51, 16))
        self.lineEdit_lv3.setObjectName("lineEdit_lv3")
        self.pushButton_selectTrain = QtWidgets.QPushButton(self.groupBox_dbn)
        self.pushButton_selectTrain.setGeometry(QtCore.QRect(190, 20, 101, 31))
        self.pushButton_selectTrain.setObjectName("pushButton_selectTrain")
        self.command_startTrain = QtWidgets.QPushButton(self.groupBox_dbn)
        self.command_startTrain.setGeometry(QtCore.QRect(190, 60, 101, 31))
        self.command_startTrain.setObjectName("command_startTrain")
        self.pushButton_saveModel = QtWidgets.QPushButton(self.groupBox_dbn)
        self.pushButton_saveModel.setGeometry(QtCore.QRect(190, 140, 101, 31))
        self.pushButton_saveModel.setObjectName("pushButton_saveModel")
        self.pushButton_loadModel = QtWidgets.QPushButton(self.groupBox_dbn)
        self.pushButton_loadModel.setGeometry(QtCore.QRect(190, 180, 101, 31))
        self.pushButton_loadModel.setObjectName("pushButton_loadModel")
        self.label_4 = QtWidgets.QLabel(self.tab_train)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 61, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_indexType = QtWidgets.QLabel(self.tab_train)
        self.label_indexType.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_indexType.setAlignment(QtCore.Qt.AlignCenter)
        self.label_indexType.setObjectName("label_indexType")
        self.lineEdit_indexName = QtWidgets.QLineEdit(self.tab_train)
        self.lineEdit_indexName.setGeometry(QtCore.QRect(80, 20, 101, 20))
        self.lineEdit_indexName.setObjectName("lineEdit_indexName")
        self.combo_indexType = QtWidgets.QComboBox(self.tab_train)
        self.combo_indexType.setGeometry(QtCore.QRect(80, 60, 101, 22))
        self.combo_indexType.setObjectName("combo_indexType")
        self.groupBox_weight = QtWidgets.QGroupBox(self.tab_train)
        self.groupBox_weight.setGeometry(QtCore.QRect(10, 120, 201, 231))
        self.groupBox_weight.setCheckable(True)
        self.groupBox_weight.setChecked(False)
        self.groupBox_weight.setObjectName("groupBox_weight")
        self.label_6 = QtWidgets.QLabel(self.groupBox_weight)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 61, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.combo_subIndex = QtWidgets.QComboBox(self.groupBox_weight)
        self.combo_subIndex.setGeometry(QtCore.QRect(80, 20, 101, 22))
        self.combo_subIndex.setObjectName("combo_subIndex")
        self.label_5 = QtWidgets.QLabel(self.groupBox_weight)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 61, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_weight = QtWidgets.QLineEdit(self.groupBox_weight)
        self.lineEdit_weight.setGeometry(QtCore.QRect(80, 60, 101, 20))
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.push_saveWeight = QtWidgets.QPushButton(self.groupBox_weight)
        self.push_saveWeight.setGeometry(QtCore.QRect(80, 100, 101, 31))
        self.push_saveWeight.setObjectName("push_saveWeight")
        self.push_saveCurrentindex = QtWidgets.QPushButton(self.tab_train)
        self.push_saveCurrentindex.setGeometry(QtCore.QRect(410, 10, 101, 31))
        self.push_saveCurrentindex.setObjectName("push_saveCurrentindex")
        self.push_clearCurrentindex = QtWidgets.QPushButton(self.tab_train)
        self.push_clearCurrentindex.setGeometry(QtCore.QRect(410, 50, 101, 31))
        self.push_clearCurrentindex.setObjectName("push_clearCurrentindex")
        self.push_checkIndex = QtWidgets.QPushButton(self.tab_train)
        self.push_checkIndex.setGeometry(QtCore.QRect(410, 90, 101, 31))
        self.push_checkIndex.setObjectName("push_checkIndex")
        self.tabWidget.addTab(self.tab_train, "")
        self.tab_test = QtWidgets.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.push_selectEvaluate = QtWidgets.QPushButton(self.tab_test)
        self.push_selectEvaluate.setGeometry(QtCore.QRect(70, 320, 101, 31))
        self.push_selectEvaluate.setObjectName("push_selectEvaluate")
        self.command_startEvaluate = QtWidgets.QPushButton(self.tab_test)
        self.command_startEvaluate.setGeometry(QtCore.QRect(220, 320, 101, 31))
        self.command_startEvaluate.setObjectName("command_startEvaluate")
        self.push_saveResult = QtWidgets.QPushButton(self.tab_test)
        self.push_saveResult.setGeometry(QtCore.QRect(370, 320, 101, 31))
        self.push_saveResult.setObjectName("push_saveResult")
        self.table_result = QtWidgets.QTableWidget(self.tab_test)
        self.table_result.setGeometry(QtCore.QRect(10, 10, 521, 291))
        self.table_result.setColumnCount(0)
        self.table_result.setObjectName("table_result")
        self.table_result.setRowCount(0)
        self.tabWidget.addTab(self.tab_test, "")
        self.group_index = QtWidgets.QGroupBox(self.centralWidget)
        self.group_index.setGeometry(QtCore.QRect(30, 100, 311, 381))
        self.group_index.setObjectName("group_index")
        self.tree_index = QtWidgets.QTreeWidget(self.group_index)
        self.tree_index.setGeometry(QtCore.QRect(10, 30, 291, 291))
        self.tree_index.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_index.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tree_index.setRootIsDecorated(True)
        self.tree_index.setUniformRowHeights(True)
        self.tree_index.setHeaderHidden(False)
        self.tree_index.setObjectName("tree_index")
        self.tree_index.header().setVisible(True)
        self.tree_index.header().setCascadingSectionResizes(True)
        self.tree_index.header().setDefaultSectionSize(200)
        self.tree_index.header().setMinimumSectionSize(50)
        self.tree_index.header().setStretchLastSection(True)
        self.push_saveIndex = QtWidgets.QPushButton(self.group_index)
        self.push_saveIndex.setGeometry(QtCore.QRect(110, 340, 91, 31))
        self.push_saveIndex.setObjectName("push_saveIndex")
        self.push_selectIndex = QtWidgets.QPushButton(self.group_index)
        self.push_selectIndex.setGeometry(QtCore.QRect(10, 340, 91, 31))
        self.push_selectIndex.setObjectName("push_selectIndex")
        self.push_confirmindex = QtWidgets.QPushButton(self.group_index)
        self.push_confirmindex.setGeometry(QtCore.QRect(210, 340, 91, 31))
        self.push_confirmindex.setObjectName("push_confirmindex")
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 967, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于深度学习的雷达/侦察系统效能评估软件"))
        self.MainTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">基于深度学习的雷达/侦察系统效能评估软件</span></p></body></html>"))
        self.label_indexName.setText(_translate("MainWindow", "指标名称"))
        self.groupBox_dbn.setTitle(_translate("MainWindow", "深度学习"))
        self.label.setText(_translate("MainWindow", "训练学习速率"))
        self.label_2.setText(_translate("MainWindow", "迭代次数"))
        self.label_3.setText(_translate("MainWindow", "Batch大小"))
        self.groupBox_nodeNum.setTitle(_translate("MainWindow", "节点数量"))
        self.checkBox_lv1.setText(_translate("MainWindow", "第一层"))
        self.checkBox_lv2.setText(_translate("MainWindow", "第二层"))
        self.checkBox_lv3.setText(_translate("MainWindow", "第三层"))
        self.pushButton_selectTrain.setText(_translate("MainWindow", "选择样本数据"))
        self.command_startTrain.setText(_translate("MainWindow", "开始训练"))
        self.pushButton_saveModel.setText(_translate("MainWindow", "保存模型"))
        self.pushButton_loadModel.setText(_translate("MainWindow", "加载模型"))
        self.label_4.setText(_translate("MainWindow", "计算方法"))
        self.label_indexType.setText(_translate("MainWindow", "指标类型"))
        self.groupBox_weight.setTitle(_translate("MainWindow", "加权计算"))
        self.label_6.setText(_translate("MainWindow", "选择指标"))
        self.label_5.setText(_translate("MainWindow", "权重"))
        self.push_saveWeight.setText(_translate("MainWindow", "确定"))
        self.push_saveCurrentindex.setText(_translate("MainWindow", "保存"))
        self.push_clearCurrentindex.setText(_translate("MainWindow", "重置"))
        self.push_checkIndex.setText(_translate("MainWindow", "一致性校验"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_train), _translate("MainWindow", "指标属性"))
        self.push_selectEvaluate.setText(_translate("MainWindow", "选择评估数据"))
        self.command_startEvaluate.setText(_translate("MainWindow", "开始评估"))
        self.push_saveResult.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("MainWindow", "评估计算"))
        self.group_index.setTitle(_translate("MainWindow", "指标体系"))
        self.tree_index.headerItem().setText(0, _translate("MainWindow", "名称"))
        self.tree_index.headerItem().setText(1, _translate("MainWindow", "权重"))
        self.tree_index.headerItem().setText(2, _translate("MainWindow", "类型"))
        self.tree_index.headerItem().setText(3, _translate("MainWindow", "是否加权"))
        self.push_saveIndex.setText(_translate("MainWindow", "保存指标体系"))
        self.push_selectIndex.setText(_translate("MainWindow", "导入指标体系"))
        self.push_confirmindex.setText(_translate("MainWindow", "确认"))


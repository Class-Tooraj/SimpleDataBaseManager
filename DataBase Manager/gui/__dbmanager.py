# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 550)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAddRow = QAction(MainWindow)
        self.actionAddRow.setObjectName(u"actionAddRow")
        self.actionAddColumn = QAction(MainWindow)
        self.actionAddColumn.setObjectName(u"actionAddColumn")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDelRow = QAction(MainWindow)
        self.actionDelRow.setObjectName(u"actionDelRow")
        self.actionDelColumn = QAction(MainWindow)
        self.actionDelColumn.setObjectName(u"actionDelColumn")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_tableName = QLabel(self.centralwidget)
        self.lbl_tableName.setObjectName(u"lbl_tableName")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(False)
        self.lbl_tableName.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_tableName)

        self.cmb_tableName = QComboBox(self.centralwidget)
        self.cmb_tableName.addItem("")
        self.cmb_tableName.addItem("")
        self.cmb_tableName.setObjectName(u"cmb_tableName")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_tableName.sizePolicy().hasHeightForWidth())
        self.cmb_tableName.setSizePolicy(sizePolicy)
        self.cmb_tableName.setMinimumSize(QSize(150, 0))
        self.cmb_tableName.setEditable(True)
        self.cmb_tableName.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.cmb_tableName.setMinimumContentsLength(0)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmb_tableName)


        self.horizontalLayout.addLayout(self.formLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 100):
            self.tableWidget.setColumnCount(100)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.tableWidget.setDefaultDropAction(Qt.MoveAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setIconSize(QSize(16, 16))
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(100)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTable = QMenu(self.menubar)
        self.menuTable.setObjectName(u"menuTable")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTable.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTable.addAction(self.actionAddRow)
        self.menuTable.addAction(self.actionAddColumn)
        self.menuTable.addSeparator()
        self.menuTable.addAction(self.actionDelRow)
        self.menuTable.addAction(self.actionDelColumn)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(shortcut)
        self.actionSaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAddRow.setText(QCoreApplication.translate("MainWindow", u"Add Row", None))
#if QT_CONFIG(tooltip)
        self.actionAddRow.setToolTip(QCoreApplication.translate("MainWindow", u"Add Row", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAddRow.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddColumn.setText(QCoreApplication.translate("MainWindow", u"Add Column", None))
#if QT_CONFIG(shortcut)
        self.actionAddColumn.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDelRow.setText(QCoreApplication.translate("MainWindow", u"Del Row", None))
        self.actionDelColumn.setText(QCoreApplication.translate("MainWindow", u"Del Column", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.lbl_tableName.setText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.cmb_tableName.setItemText(0, QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.cmb_tableName.setItemText(1, QCoreApplication.translate("MainWindow", u"-------------", None))

        self.cmb_tableName.setCurrentText(QCoreApplication.translate("MainWindow", u"Table Name", None))
        self.cmb_tableName.setPlaceholderText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuTable.setTitle(QCoreApplication.translate("MainWindow", u"&Table", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi


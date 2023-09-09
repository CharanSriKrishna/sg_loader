# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loaderr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Projects = QComboBox(self.centralwidget)
        self.Projects.addItem("")
        self.Projects.setObjectName(u"Projects")

        self.horizontalLayout_2.addWidget(self.Projects)

        self.mytask = QCheckBox(self.centralwidget)
        self.mytask.setObjectName(u"mytask")

        self.horizontalLayout_2.addWidget(self.mytask)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.TreeView = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Example Project");
        self.TreeView.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.TreeView)
        QTreeWidgetItem(self.TreeView)
        self.TreeView.setObjectName(u"TreeView")

        self.verticalLayout_3.addWidget(self.TreeView)

        self.details = QLabel(self.centralwidget)
        self.details.setObjectName(u"details")

        self.verticalLayout_3.addWidget(self.details)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display = QLabel(self.centralwidget)
        self.display.setObjectName(u"display")

        self.verticalLayout.addWidget(self.display)

        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Projects.setItemText(0, QCoreApplication.translate("MainWindow", u"Example Project", None))

        self.mytask.setText(QCoreApplication.translate("MainWindow", u"My Tasks", None))

        __sortingEnabled = self.TreeView.isSortingEnabled()
        self.TreeView.setSortingEnabled(False)
        ___qtreewidgetitem = self.TreeView.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Shot_1", None));
        ___qtreewidgetitem1 = self.TreeView.topLevelItem(1)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Shot_2", None));
        self.TreeView.setSortingEnabled(__sortingEnabled)

        self.details.setText(QCoreApplication.translate("MainWindow", u"Total : 2 Shots", None))
        self.display.setText(QCoreApplication.translate("MainWindow", u"Shot_1", None))

        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"example", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

    # retranslateUi


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
            MainWindow.setObjectName(u"SG Loader")
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
        __qtreewidgetitem.setText(0, u"Project")
        self.TreeView.setHeaderItem(__qtreewidgetitem)
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

        self.tasklist = QListWidget(self.centralwidget)
        QListWidgetItem(self.tasklist)
        self.tasklist.setObjectName(u"tasklist")

        self.verticalLayout.addWidget(self.tasklist)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SG Loader", None))
        self.Projects.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Project", None))

        self.mytask.setText(QCoreApplication.translate("MainWindow", u"My Tasks", None))
    # retranslateUi


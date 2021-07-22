# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'g.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_viewTasksDialog(object):
    def setupUi(self, viewTasksDialog):
        if not viewTasksDialog.objectName():
            viewTasksDialog.setObjectName(u"viewTasksDialog")
        viewTasksDialog.resize(591, 434)
        self.gridLayoutWidget = QWidget(viewTasksDialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 571, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tasksListView = QListView(self.gridLayoutWidget)
        self.tasksListView.setObjectName(u"tasksListView")

        self.gridLayout.addWidget(self.tasksListView, 0, 0, 1, 1)


        self.retranslateUi(viewTasksDialog)

        QMetaObject.connectSlotsByName(viewTasksDialog)
    # setupUi

    def retranslateUi(self, viewTasksDialog):
        viewTasksDialog.setWindowTitle(QCoreApplication.translate("viewTasksDialog", u"ViewTasks", None))
    # retranslateUi


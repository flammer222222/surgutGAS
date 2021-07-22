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


class Ui_documentsViewDialog(object):
    def setupUi(self, documentsViewDialog):
        if not documentsViewDialog.objectName():
            documentsViewDialog.setObjectName(u"documentsViewDialog")
        documentsViewDialog.resize(578, 450)
        self.verticalLayout_2 = QVBoxLayout(documentsViewDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.documentsListView = QListView(documentsViewDialog)
        self.documentsListView.setObjectName(u"documentsListView")

        self.verticalLayout.addWidget(self.documentsListView)

        self.addButton = QPushButton(documentsViewDialog)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.delButton = QPushButton(documentsViewDialog)
        self.delButton.setObjectName(u"delButton")

        self.verticalLayout.addWidget(self.delButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(documentsViewDialog)

        QMetaObject.connectSlotsByName(documentsViewDialog)
    # setupUi

    def retranslateUi(self, documentsViewDialog):
        documentsViewDialog.setWindowTitle(QCoreApplication.translate("documentsViewDialog", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.addButton.setText(QCoreApplication.translate("documentsViewDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delButton.setText(QCoreApplication.translate("documentsViewDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi


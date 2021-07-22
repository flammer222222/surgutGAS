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


class Ui_objectDelDialog(object):
    def setupUi(self, objectDelDialog):
        if not objectDelDialog.objectName():
            objectDelDialog.setObjectName(u"objectDelDialog")
        objectDelDialog.resize(400, 122)
        self.verticalLayout_2 = QVBoxLayout(objectDelDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.delLabel = QLabel(objectDelDialog)
        self.delLabel.setObjectName(u"delLabel")
        self.delLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.delLabel)

        self.okButton = QPushButton(objectDelDialog)
        self.okButton.setObjectName(u"okButton")

        self.verticalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(objectDelDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(objectDelDialog)

        QMetaObject.connectSlotsByName(objectDelDialog)
    # setupUi

    def retranslateUi(self, objectDelDialog):
        objectDelDialog.setWindowTitle(QCoreApplication.translate("objectDelDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
        self.delLabel.setText(QCoreApplication.translate("objectDelDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442?", None))
        self.okButton.setText(QCoreApplication.translate("objectDelDialog", u"\u041e\u043a", None))
        self.cancelButton.setText(QCoreApplication.translate("objectDelDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


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


class Ui_documentAddPathDialog(object):
    def setupUi(self, documentAddPathDialog):
        if not documentAddPathDialog.objectName():
            documentAddPathDialog.setObjectName(u"documentAddPathDialog")
        documentAddPathDialog.resize(583, 114)
        self.verticalLayout_3 = QVBoxLayout(documentAddPathDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.documenttNameLabel = QLabel(documentAddPathDialog)
        self.documenttNameLabel.setObjectName(u"documenttNameLabel")
        self.documenttNameLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.documenttNameLabel, 0, 0, 1, 1)

        self.pathToDocumentLabel = QLabel(documentAddPathDialog)
        self.pathToDocumentLabel.setObjectName(u"pathToDocumentLabel")
        self.pathToDocumentLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.pathToDocumentLabel, 1, 0, 1, 1)

        self.fileBrowesButton = QPushButton(documentAddPathDialog)
        self.fileBrowesButton.setObjectName(u"fileBrowesButton")

        self.gridLayout.addWidget(self.fileBrowesButton, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.documentNameLineEdit = QLineEdit(documentAddPathDialog)
        self.documentNameLineEdit.setObjectName(u"documentNameLineEdit")
        self.documentNameLineEdit.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.documentNameLineEdit, 0, 1, 1, 1)

        self.pathToDocumentLineEdit = QLineEdit(documentAddPathDialog)
        self.pathToDocumentLineEdit.setObjectName(u"pathToDocumentLineEdit")
        self.pathToDocumentLineEdit.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.pathToDocumentLineEdit, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(documentAddPathDialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(documentAddPathDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(documentAddPathDialog)

        QMetaObject.connectSlotsByName(documentAddPathDialog)
    # setupUi

    def retranslateUi(self, documentAddPathDialog):
        documentAddPathDialog.setWindowTitle(QCoreApplication.translate("documentAddPathDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.documenttNameLabel.setText(QCoreApplication.translate("documentAddPathDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430:", None))
        self.pathToDocumentLabel.setText(QCoreApplication.translate("documentAddPathDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0443:", None))
        self.fileBrowesButton.setText(QCoreApplication.translate("documentAddPathDialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.addButton.setText(QCoreApplication.translate("documentAddPathDialog", u"\u0414\u043e\u0431\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("documentAddPathDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


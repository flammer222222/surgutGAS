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


class Ui_objectAddDialog(object):
    def setupUi(self, objectAddDialog):
        if not objectAddDialog.objectName():
            objectAddDialog.setObjectName(u"objectAddDialog")
        objectAddDialog.resize(583, 114)
        self.verticalLayout_3 = QVBoxLayout(objectAddDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.objectNameLabel = QLabel(objectAddDialog)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.objectNameLabel, 0, 0, 1, 1)

        self.pathToSchemaLabel = QLabel(objectAddDialog)
        self.pathToSchemaLabel.setObjectName(u"pathToSchemaLabel")
        self.pathToSchemaLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.pathToSchemaLabel, 1, 0, 1, 1)

        self.fileBrowesButton = QPushButton(objectAddDialog)
        self.fileBrowesButton.setObjectName(u"fileBrowesButton")

        self.gridLayout.addWidget(self.fileBrowesButton, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.objectNameLineEdit = QLineEdit(objectAddDialog)
        self.objectNameLineEdit.setObjectName(u"objectNameLineEdit")
        self.objectNameLineEdit.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.objectNameLineEdit, 0, 1, 1, 1)

        self.pathToSchemaLineEdit = QLineEdit(objectAddDialog)
        self.pathToSchemaLineEdit.setObjectName(u"pathToSchemaLineEdit")
        self.pathToSchemaLineEdit.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.pathToSchemaLineEdit, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(objectAddDialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(objectAddDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(objectAddDialog)

        QMetaObject.connectSlotsByName(objectAddDialog)
    # setupUi

    def retranslateUi(self, objectAddDialog):
        objectAddDialog.setWindowTitle(QCoreApplication.translate("objectAddDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
        self.objectNameLabel.setText(QCoreApplication.translate("objectAddDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430:", None))
        self.pathToSchemaLabel.setText(QCoreApplication.translate("objectAddDialog", u"\u041e\u0434\u043d\u043e\u043b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0441\u0445\u0435\u043c\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430:", None))
        self.fileBrowesButton.setText(QCoreApplication.translate("objectAddDialog", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.addButton.setText(QCoreApplication.translate("objectAddDialog", u"\u0414\u043e\u0431\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("objectAddDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


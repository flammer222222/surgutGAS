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


class Ui_calendarAddDialog(object):
    def setupUi(self, calendarAddDialog):
        if not calendarAddDialog.objectName():
            calendarAddDialog.setObjectName(u"calendarAddDialog")
        calendarAddDialog.resize(787, 452)
        self.gridLayout_2 = QGridLayout(calendarAddDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolsNameLabel = QLabel(calendarAddDialog)
        self.toolsNameLabel.setObjectName(u"toolsNameLabel")
        self.toolsNameLabel.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.toolsNameLabel, 2, 0, 1, 1)

        self.objectLabel = QLabel(calendarAddDialog)
        self.objectLabel.setObjectName(u"objectLabel")
        self.objectLabel.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\" ")

        self.gridLayout.addWidget(self.objectLabel, 0, 0, 1, 1)

        self.workNameLabel = QLabel(calendarAddDialog)
        self.workNameLabel.setObjectName(u"workNameLabel")
        self.workNameLabel.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.workNameLabel, 3, 0, 1, 1)

        self.objectTextEdit = QTextEdit(calendarAddDialog)
        self.objectTextEdit.setObjectName(u"objectTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.objectTextEdit.sizePolicy().hasHeightForWidth())
        self.objectTextEdit.setSizePolicy(sizePolicy)
        self.objectTextEdit.setMinimumSize(QSize(450, 0))
        self.objectTextEdit.setMaximumSize(QSize(700, 16777215))
        self.objectTextEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.objectTextEdit, 0, 1, 1, 1)

        self.tehNumberTextEdit = QTextEdit(calendarAddDialog)
        self.tehNumberTextEdit.setObjectName(u"tehNumberTextEdit")
        sizePolicy.setHeightForWidth(self.tehNumberTextEdit.sizePolicy().hasHeightForWidth())
        self.tehNumberTextEdit.setSizePolicy(sizePolicy)
        self.tehNumberTextEdit.setMinimumSize(QSize(450, 0))
        self.tehNumberTextEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.tehNumberTextEdit, 1, 1, 1, 1)

        self.tehNumberLabel = QLabel(calendarAddDialog)
        self.tehNumberLabel.setObjectName(u"tehNumberLabel")
        self.tehNumberLabel.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.tehNumberLabel, 1, 0, 1, 1)

        self.toolsNameTextEdit = QTextEdit(calendarAddDialog)
        self.toolsNameTextEdit.setObjectName(u"toolsNameTextEdit")
        sizePolicy.setHeightForWidth(self.toolsNameTextEdit.sizePolicy().hasHeightForWidth())
        self.toolsNameTextEdit.setSizePolicy(sizePolicy)
        self.toolsNameTextEdit.setMinimumSize(QSize(450, 0))
        self.toolsNameTextEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.toolsNameTextEdit, 2, 1, 1, 1)

        self.workNameTextEdit = QTextEdit(calendarAddDialog)
        self.workNameTextEdit.setObjectName(u"workNameTextEdit")
        sizePolicy.setHeightForWidth(self.workNameTextEdit.sizePolicy().hasHeightForWidth())
        self.workNameTextEdit.setSizePolicy(sizePolicy)
        self.workNameTextEdit.setMinimumSize(QSize(450, 0))
        self.workNameTextEdit.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.workNameTextEdit, 3, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.saveButton = QPushButton(calendarAddDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(calendarAddDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(calendarAddDialog)

        QMetaObject.connectSlotsByName(calendarAddDialog)
    # setupUi

    def retranslateUi(self, calendarAddDialog):
        calendarAddDialog.setWindowTitle(QCoreApplication.translate("calendarAddDialog", u"AddCalendar", None))
        self.toolsNameLabel.setText(QCoreApplication.translate("calendarAddDialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f (\u0442\u0438\u043f):", None))
        self.objectLabel.setText(QCoreApplication.translate("calendarAddDialog", u"\u041e\u0431\u044a\u0435\u043a\u0442:", None))
        self.workNameLabel.setText(QCoreApplication.translate("calendarAddDialog", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0430 \u0440\u0430\u0431\u043e\u0442:", None))
        self.tehNumberLabel.setText(QCoreApplication.translate("calendarAddDialog", u"\u0422\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043d\u043e\u043c\u0435\u0440:", None))
        self.saveButton.setText(QCoreApplication.translate("calendarAddDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("calendarAddDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi


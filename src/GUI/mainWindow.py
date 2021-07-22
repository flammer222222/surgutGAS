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


class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        if not mainDialog.objectName():
            mainDialog.setObjectName(u"mainDialog")
        mainDialog.resize(709, 560)
        self.gridLayout_3 = QGridLayout(mainDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLabel = QLabel(mainDialog)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setStyleSheet(u"font: 75 10pt \"Times New Roman\";")
        self.mainLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.mainLabel, 0, 0, 1, 1)

        self.listView = QListView(mainDialog)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.iconLabel = QLabel(mainDialog)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMinimumSize(QSize(0, 250))
        self.iconLabel.setMaximumSize(QSize(16777215, 250))
        self.iconLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.iconLabel, 3, 0, 1, 1)

        self.calendarButton = QPushButton(mainDialog)
        self.calendarButton.setObjectName(u"calendarButton")
        self.calendarButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarButton.sizePolicy().hasHeightForWidth())
        self.calendarButton.setSizePolicy(sizePolicy)
        self.calendarButton.setMinimumSize(QSize(250, 0))
        self.calendarButton.setMaximumSize(QSize(250, 250))
        self.calendarButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.calendarButton.setLayoutDirection(Qt.LeftToRight)
        self.calendarButton.setAutoFillBackground(False)
        self.calendarButton.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.calendarButton, 1, 0, 1, 1, Qt.AlignHCenter)

        self.calendarWidget = QCalendarWidget(mainDialog)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)

        self.viewTasksButton = QPushButton(mainDialog)
        self.viewTasksButton.setObjectName(u"viewTasksButton")
        self.viewTasksButton.setMinimumSize(QSize(250, 0))

        self.gridLayout_2.addWidget(self.viewTasksButton, 2, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 2, 2, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addButton = QPushButton(mainDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_4.addWidget(self.addButton)

        self.deleteButton = QPushButton(mainDialog)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout_4.addWidget(self.deleteButton)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.retranslateUi(mainDialog)

        self.calendarButton.setDefault(False)


        QMetaObject.connectSlotsByName(mainDialog)
    # setupUi

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(QCoreApplication.translate("mainDialog", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0439 \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u0434\u043b\u044f \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 \u0420\u0417\u0410 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.mainLabel.setText(QCoreApplication.translate("mainDialog", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 ", None))
        self.iconLabel.setText(QCoreApplication.translate("mainDialog", u"TextLabel", None))
        self.calendarButton.setText(QCoreApplication.translate("mainDialog", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.viewTasksButton.setText(QCoreApplication.translate("mainDialog", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0438", None))
        self.addButton.setText(QCoreApplication.translate("mainDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
        self.deleteButton.setText(QCoreApplication.translate("mainDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043e\u0431\u044a\u0435\u043a\u0442", None))
    # retranslateUi


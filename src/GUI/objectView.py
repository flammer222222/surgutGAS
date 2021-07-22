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


class Ui_objectViewDialog(object):
    def setupUi(self, objectViewDialog):
        if not objectViewDialog.objectName():
            objectViewDialog.setObjectName(u"objectViewDialog")
        objectViewDialog.resize(928, 498)
        self.gridLayout_3 = QGridLayout(objectViewDialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.objectNameLabel = QLabel(objectViewDialog)
        self.objectNameLabel.setObjectName(u"objectNameLabel")
        self.objectNameLabel.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.objectNameLabel, 0, 0, 1, 1)

        self.objectTreeWidget = QTreeWidget(objectViewDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.objectTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.objectTreeWidget.setObjectName(u"objectTreeWidget")

        self.gridLayout.addWidget(self.objectTreeWidget, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.schemaLabel = QLabel(objectViewDialog)
        self.schemaLabel.setObjectName(u"schemaLabel")
        self.schemaLabel.setMinimumSize(QSize(600, 0))
        self.schemaLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.schemaLabel, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(objectViewDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.delButton = QPushButton(objectViewDialog)
        self.delButton.setObjectName(u"delButton")

        self.horizontalLayout.addWidget(self.delButton)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(objectViewDialog)

        QMetaObject.connectSlotsByName(objectViewDialog)
    # setupUi

    def retranslateUi(self, objectViewDialog):
        objectViewDialog.setWindowTitle(QCoreApplication.translate("objectViewDialog", u"\u041e\u0431\u044a\u0435\u043a\u0442", None))
        self.objectNameLabel.setText(QCoreApplication.translate("objectViewDialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.schemaLabel.setText(QCoreApplication.translate("objectViewDialog", u"TextLabel", None))
        self.addButton.setText(QCoreApplication.translate("objectViewDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delButton.setText(QCoreApplication.translate("objectViewDialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi


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


class Ui_addEquipDialog(object):
    def setupUi(self, addEquipDialog):
        if not addEquipDialog.objectName():
            addEquipDialog.setObjectName(u"addEquipDialog")
        addEquipDialog.resize(714, 459)
        self.gridLayout_2 = QGridLayout(addEquipDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(addEquipDialog)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(addEquipDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.oscillogramCheck = QCheckBox(addEquipDialog)
        self.oscillogramCheck.setObjectName(u"oscillogramCheck")

        self.gridLayout.addWidget(self.oscillogramCheck, 14, 1, 1, 1)

        self.filesCheck = QCheckBox(addEquipDialog)
        self.filesCheck.setObjectName(u"filesCheck")

        self.gridLayout.addWidget(self.filesCheck, 15, 1, 1, 1)

        self.techCtrlCheck = QCheckBox(addEquipDialog)
        self.techCtrlCheck.setObjectName(u"techCtrlCheck")

        self.gridLayout.addWidget(self.techCtrlCheck, 7, 1, 1, 1)

        self.preCtrlCheck = QCheckBox(addEquipDialog)
        self.preCtrlCheck.setObjectName(u"preCtrlCheck")

        self.gridLayout.addWidget(self.preCtrlCheck, 4, 1, 1, 1)

        self.testCtrlCheck = QCheckBox(addEquipDialog)
        self.testCtrlCheck.setObjectName(u"testCtrlCheck")

        self.gridLayout.addWidget(self.testCtrlCheck, 8, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 11, 1, 1, 1)

        self.nameEquipLabel = QLabel(addEquipDialog)
        self.nameEquipLabel.setObjectName(u"nameEquipLabel")
        self.nameEquipLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.nameEquipLabel, 0, 0, 1, 1)

        self.adjustmentCheck = QCheckBox(addEquipDialog)
        self.adjustmentCheck.setObjectName(u"adjustmentCheck")

        self.gridLayout.addWidget(self.adjustmentCheck, 2, 1, 1, 1)

        self.errorSignalCheck = QCheckBox(addEquipDialog)
        self.errorSignalCheck.setObjectName(u"errorSignalCheck")

        self.gridLayout.addWidget(self.errorSignalCheck, 12, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 16, 1, 1, 1)

        self.frstPreCtrlCheck = QCheckBox(addEquipDialog)
        self.frstPreCtrlCheck.setObjectName(u"frstPreCtrlCheck")

        self.gridLayout.addWidget(self.frstPreCtrlCheck, 3, 1, 1, 1)

        self.signalStartCheck = QCheckBox(addEquipDialog)
        self.signalStartCheck.setObjectName(u"signalStartCheck")

        self.gridLayout.addWidget(self.signalStartCheck, 13, 1, 1, 1)

        self.worksTypesLabel = QLabel(addEquipDialog)
        self.worksTypesLabel.setObjectName(u"worksTypesLabel")
        self.worksTypesLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.worksTypesLabel, 2, 0, 1, 1)

        self.serviceCheck = QCheckBox(addEquipDialog)
        self.serviceCheck.setObjectName(u"serviceCheck")

        self.gridLayout.addWidget(self.serviceCheck, 6, 1, 1, 1)

        self.nameEquipLineEdit = QLineEdit(addEquipDialog)
        self.nameEquipLineEdit.setObjectName(u"nameEquipLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEquipLineEdit.sizePolicy().hasHeightForWidth())
        self.nameEquipLineEdit.setSizePolicy(sizePolicy)
        self.nameEquipLineEdit.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.nameEquipLineEdit, 0, 1, 1, 1)

        self.monitoringDataLabel = QLabel(addEquipDialog)
        self.monitoringDataLabel.setObjectName(u"monitoringDataLabel")
        self.monitoringDataLabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.monitoringDataLabel, 12, 0, 1, 1)

        self.testingCheck = QCheckBox(addEquipDialog)
        self.testingCheck.setObjectName(u"testingCheck")

        self.gridLayout.addWidget(self.testingCheck, 9, 1, 1, 1)

        self.repairsCheck = QCheckBox(addEquipDialog)
        self.repairsCheck.setObjectName(u"repairsCheck")

        self.gridLayout.addWidget(self.repairsCheck, 5, 1, 1, 1)

        self.techViewCheck = QCheckBox(addEquipDialog)
        self.techViewCheck.setObjectName(u"techViewCheck")

        self.gridLayout.addWidget(self.techViewCheck, 10, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(addEquipDialog)

        QMetaObject.connectSlotsByName(addEquipDialog)
    # setupUi

    def retranslateUi(self, addEquipDialog):
        addEquipDialog.setWindowTitle(QCoreApplication.translate("addEquipDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.addButton.setText(QCoreApplication.translate("addEquipDialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("addEquipDialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.oscillogramCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041e\u0441\u0446\u0438\u043b\u043b\u043e\u0433\u0440\u0430\u043c\u044b \u0438 \u0436\u0443\u0440\u043d\u0430\u043b\u044b \u0441\u043e\u0431\u044b\u0442\u0438\u0439, \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0435\u043c\u044b\u0435 \u043c\u043d\u043e\u0433\u043e\u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u043d\u044b\u043c \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e\u043c \u0420\u0417\u0410", None))
        self.filesCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0424\u0430\u0439\u043b\u044b \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u0420\u0417\u0410", None))
        self.techCtrlCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.preCtrlCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.testCtrlCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.nameEquipLabel.setText(QCoreApplication.translate("addEquipDialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f: ", None))
        self.adjustmentCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043f\u0440\u0438 \u043d\u043e\u0432\u043e\u043c \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0438 (\u043d\u0430\u043b\u0430\u0434\u043a\u0430)", None))
        self.errorSignalCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0421\u0438\u0433\u043d\u0430\u043b\u044b \u0441\u0431\u043e\u0435\u0432 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a, \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u043d\u044b\u0445 \u0432 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0435 \u0441\u0430\u043c\u043e\u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0438 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 \u0420\u0417\u0410", None))
        self.frstPreCtrlCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041f\u0435\u0440\u0432\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.signalStartCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0421\u0438\u0433\u043d\u0430\u043b\u044b \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f (\u043f\u0443\u0441\u043a\u0430) \u0438 \u043d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u0438 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432 \u0420\u0417\u0410", None))
        self.worksTypesLabel.setText(QCoreApplication.translate("addEquipDialog", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0432\u0438\u0434\u044b \u0440\u0430\u0431\u043e\u0442:", None))
        self.serviceCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u043f\u0440\u043e\u0434\u043b\u0435\u043d\u0438\u044f \u0441\u0440\u043e\u043a\u0430 \u0441\u043b\u0443\u0436\u0431\u044b", None))
        self.monitoringDataLabel.setText(QCoreApplication.translate("addEquipDialog", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043c\u043e\u043d\u0438\u0442\u043e\u0440\u0438\u043d\u0433\u0430:", None))
        self.testingCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041e\u043f\u0440\u043e\u0431\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.repairsCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u041f\u0440\u043e\u0444\u0438\u043b\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 (\u0440\u0435\u043c\u043e\u043d\u0442)", None))
        self.techViewCheck.setText(QCoreApplication.translate("addEquipDialog", u"\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043e\u0441\u043c\u043e\u0442\u0440", None))
    # retranslateUi


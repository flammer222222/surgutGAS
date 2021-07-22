from GUI.mainWindow import Ui_mainDialog
from GUI.calendar_add import Ui_calendarAddDialog
from GUI.viewTasks import Ui_viewTasksDialog
from GUI.objectView import Ui_objectViewDialog
from GUI.objectAdd import Ui_objectAddDialog
from GUI.addEquipment import Ui_addEquipDialog
from GUI.addDocuments import Ui_documentsViewDialog
from GUI.documentAddPath import Ui_documentAddPathDialog


from pdf2image import convert_from_path

import sys
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas as pd
import sqlite3

class Application():

    def __init__(self):
        self.listEquipParams = ['Проверка при новом включении (наладка)', 'Первый профилактический контроль',
                                'Профилактический контроль', 'Профилактическое восстановление (ремонт)',
                                'Техническое обслуживание для продления срока службы', 'Технический контроль',
                                'Тестовый контроль', 'Опробование', 'Технический осмотр',
                                'Сигналы сбоев и ошибок, выявленных в результате самодиагностики устройств РЗА',
                                'Сигналы срабатывания (пуска) и неисправности устройств РЗА',
                                'Осциллограмы и журналы событий, регистрируемые многопроцессорным устройством РЗА',
                                'Файлы параметрирования устройства РЗА']
        self.PDFinPNG()
        self.app = QApplication(sys.argv)
        self.MainWindow = QDialog()
        self.ui_mainWindow = Ui_mainDialog()
        self.ui_mainWindow.setupUi(self.MainWindow)
        self.pixmap = QPixmap('../resources/logo.png')
        self.ui_mainWindow.iconLabel.setPixmap(self.pixmap)
        self.viewObjects()
        self.MainWindow.show()

        self.addObjectWindow = QDialog()
        self.ui_addObject = Ui_objectAddDialog()
        self.ui_addObject.setupUi(self.addObjectWindow)

        self.objectViewWindow = QDialog()
        self.ui_objectView = Ui_objectViewDialog()
        self.ui_objectView.setupUi(self.objectViewWindow)

        self.addEquipWindow = QDialog()
        self.ui_addEquip = Ui_addEquipDialog()
        self.ui_addEquip.setupUi(self.addEquipWindow)

        self.addDocumentsWindow = QDialog()
        self.ui_addDocuments = Ui_documentsViewDialog()
        self.ui_addDocuments.setupUi(self.addDocumentsWindow)

        self.addDocumentPathWindow = QDialog()
        self.ui_addDocumentPath = Ui_documentAddPathDialog()
        self.ui_addDocumentPath.setupUi(self.addDocumentPathWindow)

        self.calendarWindow = QDialog()
        self.ui_calendarAdd = Ui_calendarAddDialog()
        self.ui_calendarAdd.setupUi(self.calendarWindow)

        self.viewTasksCalendarWindow = QDialog()
        self.ui_viewTasksCalendar = Ui_viewTasksDialog()
        self.ui_viewTasksCalendar.setupUi(self.viewTasksCalendarWindow)

        self.connections()

        sys.exit(self.app.exec_())

    def connections(self):
        self.ui_mainWindow.calendarButton.clicked.connect(self.openCalendar)
        self.ui_mainWindow.viewTasksButton.clicked.connect(self.viewTasks)
        self.ui_mainWindow.addButton.clicked.connect(self.openAddObject)
        self.ui_mainWindow.deleteButton.clicked.connect(self.deleteObjectFromDB)
        self.ui_mainWindow.listView.doubleClicked.connect(self.openObjectView)

        self.ui_addObject.cancelButton.clicked.connect(self.closeAddObject)
        self.ui_addObject.fileBrowesButton.clicked.connect(self.selectObjectSchema)
        self.ui_addObject.addButton.clicked.connect(self.addObjectInDB)

        self.ui_objectView.addButton.clicked.connect(self.openAddEquip)
        self.ui_objectView.delButton.clicked.connect(self.deleteEquipFromDB)
        self.ui_objectView.objectTreeWidget.doubleClicked.connect(self.openAddDocuments)

        self.ui_addEquip.addButton.clicked.connect(self.addEquip)
        self.ui_addEquip.cancelButton.clicked.connect(self.closeAddEquip)

        self.ui_addDocuments.addButton.clicked.connect(self.openAddDocumentPath)
        self.ui_addDocuments.delButton.clicked.connect(self.deleteDocumentFromDB)
        self.ui_addDocuments.documentsListView.doubleClicked.connect(self.openFile)

        self.ui_addDocumentPath.cancelButton.clicked.connect(self.closeAddDocumentPath)
        self.ui_addDocumentPath.fileBrowesButton.clicked.connect(self.selectEquipDocument)
        self.ui_addDocumentPath.addButton.clicked.connect(self.addDocumentInDB)

        self.ui_calendarAdd.saveButton.clicked.connect(self.saveTask)
        self.ui_calendarAdd.cancelButton.clicked.connect(self.closeCalendar)

    def openAddObject(self):
        self.addObjectWindow.show()

    def selectObjectSchema(self):
        self.objectFilePath, _ = QFileDialog.getOpenFileName()
        self.ui_addObject.pathToSchemaLineEdit.setText(str(self.objectFilePath))

    def addObjectInDB(self):
        self.objectName = self.ui_addObject.objectNameLineEdit.displayText()
        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        cursorObj.execute('INSERT INTO objects VALUES ({0},{1}) '.format(self.addQuotes(self.objectName),
                                                              self.addQuotes(self.objectFilePath)))
        con.commit()
        con.close()
        self.addObjectWindow.close()

        self.viewObjects()

    def deleteObjectFromDB(self):
        self.selectedObjectName = self.ui_mainWindow.listView.selectedIndexes()[0].data()
        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        cursorObj.execute('DELETE FROM objects WHERE name = {0}'.format(
            self.addQuotes(self.selectedObjectName)))
        cursorObj.execute('DELETE FROM equipments WHERE objectName = {0}'.format(
            self.addQuotes(self.selectedObjectName)))
        cursorObj.execute('DELETE FROM documents WHERE objectName = {0}'.format(
            self.addQuotes(self.selectedObjectName)))
        con.commit()
        con.close()

        self.ui_objectView.objectTreeWidget.clear()
        self.viewObjects()

    def viewObjects(self):
        con = sqlite3.connect("../resources/data.db")
        cursorObj = con.cursor()
        self.objectList = cursorObj.execute('SELECT * FROM objects').fetchall()
        con.close()

        self.objectsModel = QStandardItemModel()
        for i in range(len(self.objectList)):
            item = QStandardItem(self.objectList[i][0])
            self.objectsModel.appendRow(item)

        self.ui_mainWindow.listView.setModel(self.objectsModel)

    def closeAddObject(self):
        self.addObjectWindow.close()

    def openObjectView(self):
        self.addEquipInTree(0)
        self.selectedObjectName = self.ui_mainWindow.listView.selectedIndexes()[0].data()
        con = sqlite3.connect("../resources/data.db")
        cursorObj = con.cursor()
        self.selectedObjectPath = cursorObj.execute('SELECT path FROM objects WHERE name = {0}'.format(
            self.addQuotes(self.selectedObjectName))).fetchall()[0][0]
        con.close()

        self.ui_objectView.objectNameLabel.setText(self.selectedObjectName)
        self.objectViewWindow.show()

    def openAddEquip(self):
        self.addEquipWindow.show()

    def addEquip(self):
        self.nameEquip = self.ui_addEquip.nameEquipLineEdit.displayText()
        self.oscillogram = self.ui_addEquip.oscillogramCheck.isChecked()
        self.files = self.ui_addEquip.filesCheck.isChecked()
        self.techCtrl = self.ui_addEquip.techCtrlCheck.isChecked()
        self.preCtrl = self.ui_addEquip.preCtrlCheck.isChecked()
        self.testCtrl = self.ui_addEquip.testCtrlCheck.isChecked()
        self.adjustment = self.ui_addEquip.adjustmentCheck.isChecked()
        self.errorSignal = self.ui_addEquip.errorSignalCheck.isChecked()
        self.frstPreCtrl = self.ui_addEquip.frstPreCtrlCheck.isChecked()
        self.signalStart = self.ui_addEquip.signalStartCheck.isChecked()
        self.service = self.ui_addEquip.serviceCheck.isChecked()
        self.testing = self.ui_addEquip.testingCheck.isChecked()
        self.repairs = self.ui_addEquip.repairsCheck.isChecked()
        self.techView = self.ui_addEquip.techViewCheck.isChecked()
        self.addEquipInDB()
        self.addEquipInTree(1)
        pass

    def getEquipFromBD(self):
        self.selectedObjectName = self.ui_mainWindow.listView.selectedIndexes()[0].data()
        self.equipments = []
        try:
            con = sqlite3.connect("../resources/data.db")
            cursorObj = con.cursor()
            self.equipments = cursorObj.execute('SELECT * FROM equipments WHERE objectName = {0}'.format(
                self.addQuotes(self.selectedObjectName))).fetchall()
            con.close()
        except:
            pass

    def getOneEquipFromBD(self):
        self.selectedObjectName = self.ui_mainWindow.listView.selectedIndexes()[0].data()
        self.equipments = []
        try:
            con = sqlite3.connect("../resources/data.db")
            cursorObj = con.cursor()
            self.equipments = cursorObj.execute('SELECT * FROM equipments WHERE objectName = {0} and nameEquip = {1}'
                .format(self.addQuotes(self.selectedObjectName), self.addQuotes(self.nameEquip))).fetchall()
            con.close()
        except:
            pass

    def addEquipInTree(self, flag):
        if (flag == 0):
            self.getEquipFromBD()
        else:
            self.getOneEquipFromBD()

        if self.equipments != []:
            for j in range(len(self.equipments)):
                self.itemWorksTypes = QTreeWidgetItem(self.ui_objectView.objectTreeWidget)
                self.itemWorksTypes.setText(0, self.equipments[j][1])

                self.itemNameEquip = QTreeWidgetItem(self.itemWorksTypes)
                self.itemNameEquip.setText(0, 'Виды работ')
                for i in range(0, 9):
                    if (self.equipments[j][i + 2] != 0):
                        self.itemParamEquip = QTreeWidgetItem(self.itemNameEquip)
                        self.itemParamEquip.setText(0, self.listEquipParams[i])

                self.itemMonitoringData = QTreeWidgetItem(self.itemWorksTypes)
                self.itemMonitoringData.setText(0, 'Данные мониторинга функционирования')

                for i in range(9, len(self.listEquipParams)):
                    if (self.equipments[j][i + 2] != 0):
                        self.itemNameEquip = QTreeWidgetItem(self.itemMonitoringData)
                        self.itemNameEquip.setText(0, self.listEquipParams[i])
        pass

    def addEquipInDB(self):
        con = sqlite3.connect("../resources/data.db")
        cursorObj = con.cursor()
        cursorObj.execute(
            'INSERT INTO equipments VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}) '.format(
             self.addQuotes(self.selectedObjectName), self.addQuotes(self.nameEquip), int(self.adjustment),
             int(self.frstPreCtrl), int(self.preCtrl), int(self.repairs), int(self.service), int(self.techCtrl),
             int(self.testCtrl), int(self.testing), int(self.techView), int(self.errorSignal), int(self.signalStart),
             int(self.oscillogram), int(self.files)
             ))
        con.commit()
        con.close()
        self.closeAddEquip()

    def deleteEquipFromDB(self):
        self.toolSelectedInTree = self.ui_objectView.objectTreeWidget.selectedItems()[0]
        self.ui_objectView.objectTreeWidget.takeTopLevelItem(
            self.ui_objectView.objectTreeWidget.indexOfTopLevelItem(self.toolSelectedInTree))

        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        cursorObj.execute('DELETE FROM equipments WHERE objectName = {0} AND nameEquip = {1}'.format(
            self.addQuotes(self.selectedObjectName), self.addQuotes(self.toolSelectedInTree.text(0))))
        cursorObj.execute('DELETE FROM documents WHERE objectName = {0} AND selectedTool = {1}'.format(
            self.addQuotes(self.selectedObjectName), self.addQuotes(self.toolSelectedInTree.text(0))))
        con.commit()
        con.close()

    def closeAddEquip(self):
        self.addEquipWindow.close()

    def viewDocumentsInEquip(self):
        print(self.selectedObjectName)
        print(self.equipSelectedInTree.text(0))
        print(self.selectedTool)
        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        self.documentsList = cursorObj.execute(
            'SELECT * FROM documents WHERE objectName = {0} AND equipName = {1} AND selectedTool = {2}'.format(
                self.addQuotes(self.selectedObjectName),
                self.addQuotes(self.equipSelectedInTree.text(0)),
                self.addQuotes(self.selectedTool))).fetchall()
        con.close()

        print(self.documentsList)
        self.documentsModel = QStandardItemModel()
        if self.documentsList != []:
            for i in range(len(self.documentsList)):
                item = QStandardItem(self.documentsList[i][3])
                self.documentsModel.appendRow(item)

        self.ui_addDocuments.documentsListView.setModel(self.documentsModel)

    def openAddDocuments(self):
        self.equipSelectedInTree = self.ui_objectView.objectTreeWidget.selectedItems()[0]
        if self.equipSelectedInTree.text(0) in self.listEquipParams:
            self.selectedTool = self.equipSelectedInTree.parent().parent().text(0)
            self.addDocumentsWindow.setWindowTitle(self.equipSelectedInTree.text(0) + ' ' + self.selectedTool)
            self.addDocumentsWindow.open()
            self.viewDocumentsInEquip()

    def addDocumentInDB(self):
        self.documentName = self.ui_addDocumentPath.documentNameLineEdit.displayText()
        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        cursorObj.execute(
            'INSERT INTO documents VALUES ({0},{1},{2},{3},{4})'.format(
                self.addQuotes(self.selectedObjectName), self.addQuotes(self.selectedTool),
                self.addQuotes(self.equipSelectedInTree.text(0)),
                self.addQuotes(self.documentName), self.addQuotes(self.equipDocumentPath)))
        con.commit()
        con.close()
        self.viewDocumentsInEquip()
        self.closeAddDocumentPath()

    def deleteDocumentFromDB(self):
        print(self.selectedObjectName)
        print(self.selectedTool)
        print(self.equipSelectedInTree.text(0))

        self.selectedDocumentName = self.ui_addDocuments.documentsListView.selectedIndexes()[0].data()
        con = sqlite3.connect("data.db")
        cursorObj = con.cursor()
        cursorObj.execute(
        'DELETE FROM documents WHERE objectName = {0} AND selectedTool = {1} AND equipName = {2} AND documentName = {3}'
                .format(self.addQuotes(self.selectedObjectName), self.addQuotes(self.selectedTool),
                        self.addQuotes(self.equipSelectedInTree.text(0)),
                        self.addQuotes(self.selectedDocumentName)))
        con.commit()
        con.close()
        self.viewDocumentsInEquip()

    def selectEquipDocument(self):
        self.equipDocumentPath, _ = QFileDialog.getOpenFileName()
        self.ui_addDocumentPath.pathToDocumentLineEdit.setText(str(self.equipDocumentPath))

    def openAddDocumentPath(self):
        self.addDocumentPathWindow.open()

    def closeAddDocumentPath(self):
        self.addDocumentPathWindow.close()

    def getSelectedDate(self):
        self.selectedDate = self.ui_mainWindow.calendarWidget.selectedDate().toString("dd.MM.yyyy")

    def openCalendar(self):
        self.calendarWindow.show()

    def viewTasks(self):
        self.getTasks()
        self.getSelectedDate()
        self.model = QStandardItemModel()
        for i in range(len(self.taskDates)):
            if type(self.taskDates[i]) != int and \
                    type(self.taskDates[i]) != str and \
                    type(self.taskDates[i]) != float and \
                    str(self.taskDates[i].date().strftime('%d.%m.%Y')) == self.selectedDate:
                item = QStandardItem( str(self.objects[i]) + '   ' + str(self.tehNumbers[i])+ '   ' +
                                      str(self.toolsNames[i])+ '   ' +
                                      str(self.workNames[i]))
                self.model.appendRow(item)
        self.ui_viewTasksCalendar.tasksListView.setModel(self.model)

        self.viewTasksCalendarWindow.show()

    def closeCalendar(self):
        self.calendarWindow.close()

    def saveTask(self):
        self.getSelectedDate()
        self.objectStr = self.ui_calendarAdd.objectTextEdit.toPlainText()
        self.tehNumberStr = self.ui_calendarAdd.tehNumberTextEdit.toPlainText()
        self.toolsNameStr = self.ui_calendarAdd.toolsNameTextEdit.toPlainText()
        self.workNameStr = self.ui_calendarAdd.workNameTextEdit.toPlainText()
        self.calendarWindow.close()

    def getTasks(self):
        self.getSelectedDate()
        self.file_name = 'tasks.xlsx'
        self.df = pd.read_excel(self.file_name, sheet_name="Задание")
        self.objects = list(self.df.iloc[:, 1])
        self.tehNumbers = list(self.df.iloc[:, 4])
        self.toolsNames = list(self.df.iloc[:, 5])
        self.workNames = list(self.df.iloc[:, 11])
        self.taskDates = list(self.df.iloc[:, 13])

    def PDFinPNG(self):
        return
        self.file_name = '../resources/schema_Example.pdf'
        page = convert_from_path(self.file_name)[0]

        base_filename = 'out.png'

        page.save('out.png', 'PNG')

    def addQuotes(self, myString):
        return "'" + myString + "'"

    def openFile(self):
        self.selectedfilenameName = self.ui_addDocuments.documentsListView.selectedIndexes()[0].data()
        con = sqlite3.connect("../resources/data.db")
        cursorObj = con.cursor()
        self.selectedfilePath = cursorObj.execute(
            'SELECT documentPath FROM documents WHERE objectName = {0} AND equipName = {1} AND selectedTool = {2} AND '
            'documentName = {3}'
                .format(self.addQuotes(self.selectedObjectName), self.addQuotes(self.equipSelectedInTree.text(0)),
                self.addQuotes(self.selectedTool), self.addQuotes(self.selectedfilenameName))).fetchall()
        con.close()
        print(self.selectedfilePath)
        os.system("start " + self.selectedfilePath[0][0])

if __name__ == "__main__":
    myApp = Application()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tester.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tester(object):
    def setupUi(self, Tester):
        Tester.setObjectName("Tester")
        Tester.resize(1002, 778)
        self.centralwidget = QtWidgets.QWidget(Tester)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(420, 570, 365, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 20, 491, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logBox = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.logBox.setFont(font)
        self.logBox.setObjectName("logBox")
        self.verticalLayout.addWidget(self.logBox)
        self.status = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.resBox = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.resBox.setFont(font)
        self.resBox.setObjectName("resBox")
        self.verticalLayout.addWidget(self.resBox)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(420, 290, 560, 268))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.exportfile = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.exportfile.setFont(font)
        self.exportfile.setObjectName("exportfile")
        self.gridLayout.addWidget(self.exportfile, 6, 2, 1, 1)
        self.fileio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.fileio.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.fileio.setFont(font)
        self.fileio.setObjectName("fileio")
        self.checker = QtWidgets.QButtonGroup(Tester)
        self.checker.setObjectName("checker")
        self.checker.addButton(self.fileio)
        self.gridLayout.addWidget(self.fileio, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.inputfile = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.inputfile.setEnabled(False)
        self.inputfile.setObjectName("inputfile")
        self.gridLayout.addWidget(self.inputfile, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.TL = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.TL.setFont(font)
        self.TL.setMinimum(20)
        self.TL.setMaximum(100000)
        self.TL.setSingleStep(20)
        self.TL.setProperty("value", 1000)
        self.TL.setObjectName("TL")
        self.gridLayout.addWidget(self.TL, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.ML = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.ML.setFont(font)
        self.ML.setMinimum(1024)
        self.ML.setMaximum(999999999)
        self.ML.setSingleStep(1024)
        self.ML.setProperty("value", 262144)
        self.ML.setObjectName("ML")
        self.gridLayout.addWidget(self.ML, 2, 2, 1, 1)
        self.stopiffailed = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.stopiffailed.setFont(font)
        self.stopiffailed.setChecked(True)
        self.stopiffailed.setObjectName("stopiffailed")
        self.gridLayout.addWidget(self.stopiffailed, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.choosefile = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.choosefile.setFont(font)
        self.choosefile.setReadOnly(True)
        self.choosefile.setObjectName("choosefile")
        self.horizontalLayout_4.addWidget(self.choosefile)
        self.choosefilebtn = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.choosefilebtn.setFont(font)
        self.choosefilebtn.setObjectName("choosefilebtn")
        self.horizontalLayout_4.addWidget(self.choosefilebtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.stdio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.stdio.setFont(font)
        self.stdio.setChecked(True)
        self.stdio.setObjectName("stdio")
        self.checker.addButton(self.stdio)
        self.gridLayout.addWidget(self.stdio, 5, 0, 1, 1)
        self.outputfile = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.outputfile.setEnabled(False)
        self.outputfile.setObjectName("outputfile")
        self.gridLayout.addWidget(self.outputfile, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 5, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(20, 20, 441, 251))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.setAlternatingRowColors(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 290, 358, 147))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.addtest = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.addtest.setFont(font)
        self.addtest.setObjectName("addtest")
        self.gridLayout_2.addWidget(self.addtest, 2, 0, 1, 1)
        self.explorer = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.explorer.setFont(font)
        self.explorer.setObjectName("explorer")
        self.gridLayout_2.addWidget(self.explorer, 2, 1, 1, 1)
        self.showtest = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.showtest.setFont(font)
        self.showtest.setObjectName("showtest")
        self.gridLayout_2.addWidget(self.showtest, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.testdir = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.testdir.setFont(font)
        self.testdir.setReadOnly(True)
        self.testdir.setObjectName("testdir")
        self.gridLayout_2.addWidget(self.testdir, 0, 1, 1, 1)
        self.remtest = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.remtest.setFont(font)
        self.remtest.setObjectName("remtest")
        self.gridLayout_2.addWidget(self.remtest, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.horizontalLayout_2.addWidget(self.edit)
        self.delim = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.delim.setFont(font)
        self.delim.setObjectName("delim")
        self.horizontalLayout_2.addWidget(self.delim)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.delimiter = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.delimiter.setObjectName("delimiter")
        self.gridLayout_2.addWidget(self.delimiter, 3, 1, 1, 1)
        self.funclist = QtWidgets.QListWidget(self.centralwidget)
        self.funclist.setEnabled(False)
        self.funclist.setGeometry(QtCore.QRect(20, 570, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.funclist.setFont(font)
        self.funclist.setObjectName("funclist")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 670, 961, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.unitTest = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.unitTest.setFont(font)
        self.unitTest.setObjectName("unitTest")
        self.horizontalLayout_3.addWidget(self.unitTest)
        self.regularTest = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.regularTest.setFont(font)
        self.regularTest.setChecked(True)
        self.regularTest.setObjectName("regularTest")
        self.horizontalLayout_3.addWidget(self.regularTest)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.loadfuncs = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.loadfuncs.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.loadfuncs.setFont(font)
        self.loadfuncs.setObjectName("loadfuncs")
        self.horizontalLayout_3.addWidget(self.loadfuncs)
        self.choosefuncs = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.choosefuncs.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.choosefuncs.setFont(font)
        self.choosefuncs.setObjectName("choosefuncs")
        self.horizontalLayout_3.addWidget(self.choosefuncs)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.launch = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.launch.setFont(font)
        self.launch.setObjectName("launch")
        self.horizontalLayout_3.addWidget(self.launch)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 470, 351, 95))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.inpdata = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.inpdata.setFont(font)
        self.inpdata.setObjectName("inpdata")
        self.gridLayout_3.addWidget(self.inpdata, 1, 0, 1, 1)
        self.outdata = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.outdata.setFont(font)
        self.outdata.setObjectName("outdata")
        self.gridLayout_3.addWidget(self.outdata, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        Tester.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tester)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1002, 21))
        self.menubar.setObjectName("menubar")
        Tester.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tester)
        self.statusbar.setObjectName("statusbar")
        Tester.setStatusBar(self.statusbar)

        self.retranslateUi(Tester)
        QtCore.QMetaObject.connectSlotsByName(Tester)

    def retranslateUi(self, Tester):
        _translate = QtCore.QCoreApplication.translate
        Tester.setWindowTitle(_translate("Tester", "MainWindow"))
        self.logBox.setHtml(_translate("Tester", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test log</p></body></html>"))
        self.status.setText(_translate("Tester", "<html><head/><body><p>Статус: <span style=\" color:#747474;\">Ожидает проверки</span></p></body></html>"))
        self.resBox.setHtml(_translate("Tester", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test results</p></body></html>"))
        self.label_4.setText(_translate("Tester", "Файл вывода информации"))
        self.label.setText(_translate("Tester", "TL (ограничение по времени), мс"))
        self.exportfile.setText(_translate("Tester", "check.log"))
        self.fileio.setText(_translate("Tester", "Ввод/вывод в файл"))
        self.label_3.setText(_translate("Tester", "Файл ввода информации"))
        self.label_2.setText(_translate("Tester", "ML (ограничение по памяти), КБ (только Linux)"))
        self.label_5.setText(_translate("Tester", "Проверяемый скрипт (*.py)"))
        self.label_6.setText(_translate("Tester", "Экспорт лог-файла"))
        self.stopiffailed.setText(_translate("Tester", "Прекращать работу в случае ошибки"))
        self.choosefilebtn.setText(_translate("Tester", "Выбрать файл..."))
        self.stdio.setText(_translate("Tester", "Стандартный ввод/ вывод"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Tester", "Тест"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Tester", "Входные данные"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Tester", "Выходные данные"))
        self.addtest.setText(_translate("Tester", "Добавить тест вручную!"))
        self.explorer.setText(_translate("Tester", "Выбрать папку..."))
        self.showtest.setText(_translate("Tester", "Показать тесты"))
        self.label_7.setText(_translate("Tester", "Директория с файлами формата\n"
"x.in / x.out, где x - натуральное\n"
"число, начиная с 1"))
        self.remtest.setText(_translate("Tester", "Удалить тест"))
        self.edit.setText(_translate("Tester", "Изменить..."))
        self.delim.setText(_translate("Tester", "Разделитель..."))
        self.unitTest.setText(_translate("Tester", "Юнит-тест; main()"))
        self.regularTest.setText(_translate("Tester", "Классическая проверка"))
        self.loadfuncs.setText(_translate("Tester", "Загрузить список функций"))
        self.choosefuncs.setText(_translate("Tester", "Выбрать функцию"))
        self.launch.setText(_translate("Tester", "Запустить!"))
        self.label_8.setText(_translate("Tester", "Выходные данные"))
        self.label_10.setText(_translate("Tester", "Входные данные"))

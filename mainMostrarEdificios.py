# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMostrarEdificios.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMostrarEdificios(object):
    def setupUi(self, MainMostrarEdificios):
        MainMostrarEdificios.setObjectName("MainMostrarEdificios")
        MainMostrarEdificios.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainMostrarEdificios)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(300, 110, 261, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        MainMostrarEdificios.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMostrarEdificios)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainMostrarEdificios.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMostrarEdificios)
        self.statusbar.setObjectName("statusbar")
        MainMostrarEdificios.setStatusBar(self.statusbar)

        self.retranslateUi(MainMostrarEdificios)
        QtCore.QMetaObject.connectSlotsByName(MainMostrarEdificios)

    def retranslateUi(self, MainMostrarEdificios):
        _translate = QtCore.QCoreApplication.translate
        MainMostrarEdificios.setWindowTitle(_translate("MainMostrarEdificios", "Edificios"))
        self.label.setText(_translate("MainMostrarEdificios", "Mostrar Edificios"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainMostrarEdificios", "Edificio"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainMostrarEdificios", "Residentes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMostrarEdificios = QtWidgets.QMainWindow()
    ui = Ui_MainMostrarEdificios()
    ui.setupUi(MainMostrarEdificios)
    MainMostrarEdificios.show()
    sys.exit(app.exec_())


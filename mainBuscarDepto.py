# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainBuscarDepto.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBuscarDepto(object):
    def setupUi(self, MainBuscarDepto):
        MainBuscarDepto.setObjectName("MainBuscarDepto")
        MainBuscarDepto.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainBuscarDepto)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 30, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txtNumero = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNumero.setGeometry(QtCore.QRect(330, 100, 231, 22))
        self.txtNumero.setObjectName("txtNumero")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(600, 100, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableDepas = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDepas.setGeometry(QtCore.QRect(150, 160, 551, 301))
        self.tableDepas.setMinimumSize(QtCore.QSize(0, 191))
        self.tableDepas.setObjectName("tableDepas")
        self.tableDepas.setColumnCount(4)
        self.tableDepas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDepas.setHorizontalHeaderItem(3, item)
        self.cboBuscar = QtWidgets.QComboBox(self.centralwidget)
        self.cboBuscar.setGeometry(QtCore.QRect(150, 100, 161, 22))
        self.cboBuscar.setObjectName("cboBuscar")
        self.cboBuscar.addItem("")
        self.cboBuscar.addItem("")
        self.cboBuscar.addItem("")
        MainBuscarDepto.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBuscarDepto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainBuscarDepto.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBuscarDepto)
        self.statusbar.setObjectName("statusbar")
        MainBuscarDepto.setStatusBar(self.statusbar)

        self.retranslateUi(MainBuscarDepto)
        QtCore.QMetaObject.connectSlotsByName(MainBuscarDepto)

    def retranslateUi(self, MainBuscarDepto):
        _translate = QtCore.QCoreApplication.translate
        MainBuscarDepto.setWindowTitle(_translate("MainBuscarDepto", "MainWindow"))
        self.label.setText(_translate("MainBuscarDepto", "Buscar Departamento"))
        self.label_2.setText(_translate("MainBuscarDepto", "Buscar por"))
        self.btnBuscar.setText(_translate("MainBuscarDepto", "Buscar"))
        item = self.tableDepas.horizontalHeaderItem(0)
        item.setText(_translate("MainBuscarDepto", "N° Departamento"))
        item = self.tableDepas.horizontalHeaderItem(1)
        item.setText(_translate("MainBuscarDepto", "Edificio"))
        item = self.tableDepas.horizontalHeaderItem(2)
        item.setText(_translate("MainBuscarDepto", "Dueño"))
        item = self.tableDepas.horizontalHeaderItem(3)
        item.setText(_translate("MainBuscarDepto", "N° Residentes"))
        self.cboBuscar.setItemText(0, _translate("MainBuscarDepto", "-Seleccione opcion-"))
        self.cboBuscar.setItemText(1, _translate("MainBuscarDepto", "Numero"))
        self.cboBuscar.setItemText(2, _translate("MainBuscarDepto", "Dueño"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBuscarDepto = QtWidgets.QMainWindow()
    ui = Ui_MainBuscarDepto()
    ui.setupUi(MainBuscarDepto)
    MainBuscarDepto.show()
    sys.exit(app.exec_())


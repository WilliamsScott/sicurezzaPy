# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEliminarVehiculo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainEliminarVehiculo(object):
    def setupUi(self, MainEliminarVehiculo):
        MainEliminarVehiculo.setObjectName("MainEliminarVehiculo")
        MainEliminarVehiculo.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEliminarVehiculo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 55, 16))
        self.label_2.setObjectName("label_2")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(230, 110, 301, 22))
        self.txtRut.setObjectName("txtRut")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(550, 110, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(230, 140, 301, 22))
        self.txtNombre.setReadOnly(True)
        self.txtNombre.setObjectName("txtNombre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.tableVehiculos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVehiculos.setGeometry(QtCore.QRect(80, 200, 661, 192))
        self.tableVehiculos.setObjectName("tableVehiculos")
        self.tableVehiculos.setColumnCount(5)
        self.tableVehiculos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableVehiculos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVehiculos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVehiculos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVehiculos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVehiculos.setHorizontalHeaderItem(4, item)
        self.txtPatente = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPatente.setGeometry(QtCore.QRect(230, 450, 301, 22))
        self.txtPatente.setObjectName("txtPatente")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(550, 450, 93, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 450, 55, 16))
        self.label_4.setObjectName("label_4")
        MainEliminarVehiculo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEliminarVehiculo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEliminarVehiculo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEliminarVehiculo)
        self.statusbar.setObjectName("statusbar")
        MainEliminarVehiculo.setStatusBar(self.statusbar)

        self.retranslateUi(MainEliminarVehiculo)
        QtCore.QMetaObject.connectSlotsByName(MainEliminarVehiculo)

    def retranslateUi(self, MainEliminarVehiculo):
        _translate = QtCore.QCoreApplication.translate
        MainEliminarVehiculo.setWindowTitle(_translate("MainEliminarVehiculo", "MainWindow"))
        self.label.setText(_translate("MainEliminarVehiculo", "Eliminar Vehiculo Residente"))
        self.label_2.setText(_translate("MainEliminarVehiculo", "RUT"))
        self.btnBuscar.setText(_translate("MainEliminarVehiculo", "Buscar"))
        self.label_3.setText(_translate("MainEliminarVehiculo", "Nombre"))
        item = self.tableVehiculos.horizontalHeaderItem(0)
        item.setText(_translate("MainEliminarVehiculo", "Patente"))
        item = self.tableVehiculos.horizontalHeaderItem(1)
        item.setText(_translate("MainEliminarVehiculo", "Marca"))
        item = self.tableVehiculos.horizontalHeaderItem(2)
        item.setText(_translate("MainEliminarVehiculo", "Modelo"))
        item = self.tableVehiculos.horizontalHeaderItem(3)
        item.setText(_translate("MainEliminarVehiculo", "Estacionamiento"))
        item = self.tableVehiculos.horizontalHeaderItem(4)
        item.setText(_translate("MainEliminarVehiculo", "Eliminar"))
        self.btnEliminar.setText(_translate("MainEliminarVehiculo", "Eliminar"))
        self.label_4.setText(_translate("MainEliminarVehiculo", "Patente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEliminarVehiculo = QtWidgets.QMainWindow()
    ui = Ui_MainEliminarVehiculo()
    ui.setupUi(MainEliminarVehiculo)
    MainEliminarVehiculo.show()
    sys.exit(app.exec_())


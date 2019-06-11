# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEliminarArrendatario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainEliminarArrendatario(object):
    def setupUi(self, MainEliminarArrendatario):
        MainEliminarArrendatario.setObjectName("MainEliminarArrendatario")
        MainEliminarArrendatario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEliminarArrendatario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtArrendatario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtArrendatario.setGeometry(QtCore.QRect(260, 80, 291, 22))
        self.txtArrendatario.setObjectName("txtArrendatario")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(560, 70, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableDueno = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDueno.setGeometry(QtCore.QRect(120, 210, 521, 192))
        self.tableDueno.setObjectName("tableDueno")
        self.tableDueno.setColumnCount(4)
        self.tableDueno.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(3, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 180, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(600, 470, 93, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        MainEliminarArrendatario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEliminarArrendatario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEliminarArrendatario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEliminarArrendatario)
        self.statusbar.setObjectName("statusbar")
        MainEliminarArrendatario.setStatusBar(self.statusbar)

        self.retranslateUi(MainEliminarArrendatario)
        QtCore.QMetaObject.connectSlotsByName(MainEliminarArrendatario)

    def retranslateUi(self, MainEliminarArrendatario):
        _translate = QtCore.QCoreApplication.translate
        MainEliminarArrendatario.setWindowTitle(_translate("MainEliminarArrendatario", "MainWindow"))
        self.label.setText(_translate("MainEliminarArrendatario", "Eliminar Arrendatario"))
        self.btnBuscar.setText(_translate("MainEliminarArrendatario", "Buscar"))
        self.label_2.setText(_translate("MainEliminarArrendatario", "Rut"))
        item = self.tableDueno.horizontalHeaderItem(0)
        item.setText(_translate("MainEliminarArrendatario", "Rut"))
        item = self.tableDueno.horizontalHeaderItem(1)
        item.setText(_translate("MainEliminarArrendatario", "Nombre"))
        item = self.tableDueno.horizontalHeaderItem(2)
        item.setText(_translate("MainEliminarArrendatario", "Apellido"))
        item = self.tableDueno.horizontalHeaderItem(3)
        item.setText(_translate("MainEliminarArrendatario", "Telefono"))
        self.label_4.setText(_translate("MainEliminarArrendatario", "Datos Arrendatario"))
        self.btnEliminar.setText(_translate("MainEliminarArrendatario", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEliminarArrendatario = QtWidgets.QMainWindow()
    ui = Ui_MainEliminarArrendatario()
    ui.setupUi(MainEliminarArrendatario)
    MainEliminarArrendatario.show()
    sys.exit(app.exec_())


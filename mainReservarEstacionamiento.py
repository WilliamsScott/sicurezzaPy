# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainReservarEstacionamiento.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainReservarEstacionamiento(object):
    def setupUi(self, MainReservarEstacionamiento):
        MainReservarEstacionamiento.setObjectName("MainReservarEstacionamiento")
        MainReservarEstacionamiento.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainReservarEstacionamiento)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txtBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBuscar.setGeometry(QtCore.QRect(240, 100, 341, 22))
        self.txtBuscar.setObjectName("txtBuscar")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(590, 100, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableEstacionamiento = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEstacionamiento.setGeometry(QtCore.QRect(20, 160, 771, 221))
        self.tableEstacionamiento.setObjectName("tableEstacionamiento")
        self.tableEstacionamiento.setColumnCount(6)
        self.tableEstacionamiento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableEstacionamiento.setHorizontalHeaderItem(5, item)
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(120, 510, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(590, 510, 93, 28))
        self.btnAgregar.setObjectName("btnAgregar")
        self.cboReservar = QtWidgets.QComboBox(self.centralwidget)
        self.cboReservar.setGeometry(QtCore.QRect(320, 470, 261, 22))
        self.cboReservar.setObjectName("cboReservar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 470, 101, 20))
        self.label_3.setObjectName("label_3")
        MainReservarEstacionamiento.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainReservarEstacionamiento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainReservarEstacionamiento.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainReservarEstacionamiento)
        self.statusbar.setObjectName("statusbar")
        MainReservarEstacionamiento.setStatusBar(self.statusbar)

        self.retranslateUi(MainReservarEstacionamiento)
        QtCore.QMetaObject.connectSlotsByName(MainReservarEstacionamiento)

    def retranslateUi(self, MainReservarEstacionamiento):
        _translate = QtCore.QCoreApplication.translate
        MainReservarEstacionamiento.setWindowTitle(_translate("MainReservarEstacionamiento", "Reservar Estacionamiento"))
        self.label.setText(_translate("MainReservarEstacionamiento", "Reservar Estacionamiento"))
        self.label_2.setText(_translate("MainReservarEstacionamiento", "Residente"))
        self.btnBuscar.setText(_translate("MainReservarEstacionamiento", "Buscar"))
        item = self.tableEstacionamiento.horizontalHeaderItem(0)
        item.setText(_translate("MainReservarEstacionamiento", "Nombre"))
        item = self.tableEstacionamiento.horizontalHeaderItem(1)
        item.setText(_translate("MainReservarEstacionamiento", "Apellido"))
        item = self.tableEstacionamiento.horizontalHeaderItem(2)
        item.setText(_translate("MainReservarEstacionamiento", "Edificio"))
        item = self.tableEstacionamiento.horizontalHeaderItem(3)
        item.setText(_translate("MainReservarEstacionamiento", "Departamento"))
        item = self.tableEstacionamiento.horizontalHeaderItem(4)
        item.setText(_translate("MainReservarEstacionamiento", "Estacionamiento"))
        item = self.tableEstacionamiento.horizontalHeaderItem(5)
        item.setText(_translate("MainReservarEstacionamiento", "Estado"))
        self.btnCancelar.setText(_translate("MainReservarEstacionamiento", "Cancelar"))
        self.btnAgregar.setText(_translate("MainReservarEstacionamiento", "Reservar"))
        self.label_3.setText(_translate("MainReservarEstacionamiento", "Estacionamiento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainReservarEstacionamiento = QtWidgets.QMainWindow()
    ui = Ui_MainReservarEstacionamiento()
    ui.setupUi(MainReservarEstacionamiento)
    MainReservarEstacionamiento.show()
    sys.exit(app.exec_())


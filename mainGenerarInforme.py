# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGenerarInforme.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainGenerarInforme(object):
    def setupUi(self, MainGenerarInforme):
        MainGenerarInforme.setObjectName("MainGenerarInforme")
        MainGenerarInforme.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainGenerarInforme)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 100, 101, 31))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(250, 110, 261, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnExcel = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcel.setGeometry(QtCore.QRect(530, 110, 93, 28))
        self.btnExcel.setObjectName("btnExcel")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(50, 480, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(250, 170, 261, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 170, 121, 31))
        self.label_3.setObjectName("label_3")
        MainGenerarInforme.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainGenerarInforme)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainGenerarInforme.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainGenerarInforme)
        self.statusbar.setObjectName("statusbar")
        MainGenerarInforme.setStatusBar(self.statusbar)

        self.retranslateUi(MainGenerarInforme)
        QtCore.QMetaObject.connectSlotsByName(MainGenerarInforme)

    def retranslateUi(self, MainGenerarInforme):
        _translate = QtCore.QCoreApplication.translate
        MainGenerarInforme.setWindowTitle(_translate("MainGenerarInforme", "Generar Informe"))
        self.label.setText(_translate("MainGenerarInforme", "Generar Informe"))
        self.label_2.setText(_translate("MainGenerarInforme", "Informe sobre:"))
        self.comboBox.setItemText(0, _translate("MainGenerarInforme", "-Seleccione opcion-"))
        self.comboBox.setItemText(1, _translate("MainGenerarInforme", "Residentes"))
        self.comboBox.setItemText(2, _translate("MainGenerarInforme", "Visitas"))
        self.comboBox.setItemText(3, _translate("MainGenerarInforme", "Usuarios"))
        self.comboBox.setItemText(4, _translate("MainGenerarInforme", "Vehiculos"))
        self.comboBox.setItemText(5, _translate("MainGenerarInforme", "Estacionamientos"))
        self.comboBox.setItemText(6, _translate("MainGenerarInforme", "Departamentos"))
        self.comboBox.setItemText(7, _translate("MainGenerarInforme", "Edificios"))
        self.btnExcel.setText(_translate("MainGenerarInforme", "Generar Excel"))
        self.btnCancelar.setText(_translate("MainGenerarInforme", "Cancelar"))
        self.label_3.setText(_translate("MainGenerarInforme", "Nombre documento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGenerarInforme = QtWidgets.QMainWindow()
    ui = Ui_MainGenerarInforme()
    ui.setupUi(MainGenerarInforme)
    MainGenerarInforme.show()
    sys.exit(app.exec_())


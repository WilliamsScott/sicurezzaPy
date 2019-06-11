# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAgregarEstacionamiento.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainAgregarEstacionamiento(object):
    def setupUi(self, MainAgregarEstacionamiento):
        MainAgregarEstacionamiento.setObjectName("MainAgregarEstacionamiento")
        MainAgregarEstacionamiento.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainAgregarEstacionamiento)
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
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setEnabled(True)
        self.txtNombre.setGeometry(QtCore.QRect(240, 140, 341, 22))
        self.txtNombre.setReadOnly(True)
        self.txtNombre.setObjectName("txtNombre")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 71, 16))
        self.label_3.setObjectName("label_3")
        self.cboDepartamentos = QtWidgets.QComboBox(self.centralwidget)
        self.cboDepartamentos.setGeometry(QtCore.QRect(240, 220, 341, 22))
        self.cboDepartamentos.setObjectName("cboDepartamentos")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 220, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 260, 101, 20))
        self.label_5.setObjectName("label_5")
        self.cboEstacionamiento = QtWidgets.QComboBox(self.centralwidget)
        self.cboEstacionamiento.setGeometry(QtCore.QRect(240, 260, 341, 22))
        self.cboEstacionamiento.setObjectName("cboEstacionamiento")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(600, 380, 93, 28))
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(150, 380, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        MainAgregarEstacionamiento.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainAgregarEstacionamiento)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainAgregarEstacionamiento.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainAgregarEstacionamiento)
        self.statusbar.setObjectName("statusbar")
        MainAgregarEstacionamiento.setStatusBar(self.statusbar)

        self.retranslateUi(MainAgregarEstacionamiento)
        QtCore.QMetaObject.connectSlotsByName(MainAgregarEstacionamiento)

    def retranslateUi(self, MainAgregarEstacionamiento):
        _translate = QtCore.QCoreApplication.translate
        MainAgregarEstacionamiento.setWindowTitle(_translate("MainAgregarEstacionamiento", "Agregar Estacionamiento"))
        self.label.setText(_translate("MainAgregarEstacionamiento", "Agregar Estacionamiento"))
        self.label_2.setText(_translate("MainAgregarEstacionamiento", "Residente"))
        self.btnBuscar.setText(_translate("MainAgregarEstacionamiento", "Buscar"))
        self.label_3.setText(_translate("MainAgregarEstacionamiento", "Nombre"))
        self.label_4.setText(_translate("MainAgregarEstacionamiento", "Departamentos"))
        self.label_5.setText(_translate("MainAgregarEstacionamiento", "Estacionamiento"))
        self.btnAgregar.setText(_translate("MainAgregarEstacionamiento", "Agregar"))
        self.btnCancelar.setText(_translate("MainAgregarEstacionamiento", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainAgregarEstacionamiento = QtWidgets.QMainWindow()
    ui = Ui_MainAgregarEstacionamiento()
    ui.setupUi(MainAgregarEstacionamiento)
    MainAgregarEstacionamiento.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAgregarArrendatario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainAgregarArrendatario(object):
    def setupUi(self, MainAgregarArrendatario):
        MainAgregarArrendatario.setObjectName("MainAgregarArrendatario")
        MainAgregarArrendatario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainAgregarArrendatario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(310, 90, 251, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(310, 130, 251, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(310, 170, 251, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(310, 210, 251, 22))
        self.txtTelefono.setObjectName("txtTelefono")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 210, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 130, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 170, 55, 16))
        self.label_4.setObjectName("label_4")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(600, 340, 93, 28))
        self.btnAgregar.setObjectName("btnAgregar")
        self.cboEdficio = QtWidgets.QComboBox(self.centralwidget)
        self.cboEdficio.setGeometry(QtCore.QRect(310, 250, 251, 22))
        self.cboEdficio.setObjectName("cboEdficio")
        self.cboDepartamento = QtWidgets.QComboBox(self.centralwidget)
        self.cboDepartamento.setGeometry(QtCore.QRect(310, 290, 251, 22))
        self.cboDepartamento.setObjectName("cboDepartamento")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 250, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 290, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainAgregarArrendatario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainAgregarArrendatario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainAgregarArrendatario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainAgregarArrendatario)
        self.statusbar.setObjectName("statusbar")
        MainAgregarArrendatario.setStatusBar(self.statusbar)

        self.retranslateUi(MainAgregarArrendatario)
        QtCore.QMetaObject.connectSlotsByName(MainAgregarArrendatario)

    def retranslateUi(self, MainAgregarArrendatario):
        _translate = QtCore.QCoreApplication.translate
        MainAgregarArrendatario.setWindowTitle(_translate("MainAgregarArrendatario", "MainWindow"))
        self.label.setText(_translate("MainAgregarArrendatario", "Agregar Arrendatario"))
        self.label_5.setText(_translate("MainAgregarArrendatario", "Telefono"))
        self.label_2.setText(_translate("MainAgregarArrendatario", "Rut"))
        self.label_3.setText(_translate("MainAgregarArrendatario", "Nombre"))
        self.label_4.setText(_translate("MainAgregarArrendatario", "Apellido"))
        self.btnAgregar.setText(_translate("MainAgregarArrendatario", "Agregar"))
        self.label_6.setText(_translate("MainAgregarArrendatario", "Edificio"))
        self.label_7.setText(_translate("MainAgregarArrendatario", "Departamento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainAgregarArrendatario = QtWidgets.QMainWindow()
    ui = Ui_MainAgregarArrendatario()
    ui.setupUi(MainAgregarArrendatario)
    MainAgregarArrendatario.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEditarArrendatario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainEditarArrendatario(object):
    def setupUi(self, MainEditarArrendatario):
        MainEditarArrendatario.setObjectName("MainEditarArrendatario")
        MainEditarArrendatario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEditarArrendatario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(280, 130, 251, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(280, 170, 251, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(280, 210, 251, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(280, 250, 251, 22))
        self.txtTelefono.setObjectName("txtTelefono")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 250, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 210, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 126, 55, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 170, 55, 16))
        self.label_3.setObjectName("label_3")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(550, 130, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(560, 410, 93, 28))
        self.btnGuardar.setObjectName("btnGuardar")
        MainEditarArrendatario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEditarArrendatario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEditarArrendatario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEditarArrendatario)
        self.statusbar.setObjectName("statusbar")
        MainEditarArrendatario.setStatusBar(self.statusbar)

        self.retranslateUi(MainEditarArrendatario)
        QtCore.QMetaObject.connectSlotsByName(MainEditarArrendatario)

    def retranslateUi(self, MainEditarArrendatario):
        _translate = QtCore.QCoreApplication.translate
        MainEditarArrendatario.setWindowTitle(_translate("MainEditarArrendatario", "MainWindow"))
        self.label.setText(_translate("MainEditarArrendatario", "Editar Arrendatario"))
        self.label_5.setText(_translate("MainEditarArrendatario", "Telefono"))
        self.label_4.setText(_translate("MainEditarArrendatario", "Apellido"))
        self.label_2.setText(_translate("MainEditarArrendatario", "Rut"))
        self.label_3.setText(_translate("MainEditarArrendatario", "Nombre"))
        self.btnBuscar.setText(_translate("MainEditarArrendatario", "Buscar"))
        self.btnGuardar.setText(_translate("MainEditarArrendatario", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEditarArrendatario = QtWidgets.QMainWindow()
    ui = Ui_MainEditarArrendatario()
    ui.setupUi(MainEditarArrendatario)
    MainEditarArrendatario.show()
    sys.exit(app.exec_())


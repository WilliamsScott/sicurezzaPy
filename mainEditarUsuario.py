# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEditarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_MainEditarUsuario(object):
    def setupUi(self, MainEditarUsuario):
        MainEditarUsuario.setObjectName("MainEditarUsuario")
        MainEditarUsuario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEditarUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 210, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 250, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 290, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 330, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 410, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 370, 55, 16))
        self.label_8.setObjectName("label_8")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(180, 130, 391, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(240, 210, 391, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(240, 250, 391, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(240, 290, 391, 22))
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtCorreo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCorreo.setGeometry(QtCore.QRect(240, 330, 391, 22))
        self.txtCorreo.setObjectName("txtCorreo")
        self.txtClave = QtWidgets.QLineEdit(self.centralwidget)
        self.txtClave.setGeometry(QtCore.QRect(240, 370, 391, 22))
        self.txtClave.setObjectName("txtClave")
        self.cboTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cboTipo.setGeometry(QtCore.QRect(240, 410, 391, 22))
        self.cboTipo.setObjectName("cboTipo")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.bntBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.bntBuscar.setGeometry(QtCore.QRect(580, 120, 93, 41))
        self.bntBuscar.setObjectName("bntBuscar")
        self.btnEditar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditar.setGeometry(QtCore.QRect(540, 470, 93, 28))
        self.btnEditar.setObjectName("btnEditar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 130, 41, 16))
        self.label_9.setObjectName("label_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 81))
        self.frame.setStyleSheet("background-color:\"#350969\"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 10, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white")
        self.label.setObjectName("label")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(130, 470, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.frame.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.txtRut.raise_()
        self.txtNombre.raise_()
        self.txtApellido.raise_()
        self.txtTelefono.raise_()
        self.txtCorreo.raise_()
        self.txtClave.raise_()
        self.cboTipo.raise_()
        self.bntBuscar.raise_()
        self.btnEditar.raise_()
        self.label_9.raise_()
        self.btnCancelar.raise_()
        MainEditarUsuario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEditarUsuario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEditarUsuario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEditarUsuario)
        self.statusbar.setObjectName("statusbar")
        MainEditarUsuario.setStatusBar(self.statusbar)

        self.btnCancelar.setIcon(QIcon(QPixmap("x.png")))
        self.btnEditar.setIcon(QIcon(QPixmap("t.png")))
        self.bntBuscar.setIcon(QIcon(QPixmap("b.png")))

        self.retranslateUi(MainEditarUsuario)
        QtCore.QMetaObject.connectSlotsByName(MainEditarUsuario)

    def retranslateUi(self, MainEditarUsuario):
        _translate = QtCore.QCoreApplication.translate
        MainEditarUsuario.setWindowTitle(_translate("MainEditarUsuario", "MainWindow"))
        self.label_3.setText(_translate("MainEditarUsuario", "Nombre"))
        self.label_4.setText(_translate("MainEditarUsuario", "Apellido"))
        self.label_5.setText(_translate("MainEditarUsuario", "Telefono"))
        self.label_6.setText(_translate("MainEditarUsuario", "Correo"))
        self.label_7.setText(_translate("MainEditarUsuario", "Tipo"))
        self.label_8.setText(_translate("MainEditarUsuario", "Clave"))
        self.cboTipo.setItemText(0, _translate("MainEditarUsuario", "-Seleccione un tipo-"))
        self.cboTipo.setItemText(1, _translate("MainEditarUsuario", "Guardia"))
        self.cboTipo.setItemText(2, _translate("MainEditarUsuario", "Administrador"))
        self.bntBuscar.setText(_translate("MainEditarUsuario", "Buscar"))
        self.btnEditar.setText(_translate("MainEditarUsuario", "Aceptar"))
        self.label_9.setText(_translate("MainEditarUsuario", "RUT"))
        self.label.setText(_translate("MainEditarUsuario", "Editar Usuario"))
        self.btnCancelar.setText(_translate("MainEditarUsuario", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEditarUsuario = QtWidgets.QMainWindow()
    ui = Ui_MainEditarUsuario()
    ui.setupUi(MainEditarUsuario)
    MainEditarUsuario.show()
    sys.exit(app.exec_())

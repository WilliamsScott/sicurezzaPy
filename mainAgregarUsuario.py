# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAgregarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainAgregarUsuario(object):
    def setupUi(self, MainAgregarUsuario):
        MainAgregarUsuario.setObjectName("MainAgregarUsuario")
        MainAgregarUsuario.resize(1269, 834)
        MainAgregarUsuario.setStyleSheet("QMainWindow{\n"
"background:black;\n"
"}\n"
"\n"
"QLabel{\n"
"color:orange;\n"
"}\n"
"QLineEdit{\n"
"border:0;\n"
"border-radius: 5px;\n"
"background: rgba(248,124,0,0.7);\n"
"padding:8px;\n"
"font-size:14;\n"
"color:white;\n"
"}\n"
"QTableWidget{\n"
"border:0;\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QTableWidget::item{\n"
"    border:1px solid orange;\n"
"}\n"
"QHeaderView,QHeaderView::section{\n"
"background-color:orange;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:orange;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"background:rgb(245,124,0);\n"
"}\n"
"QDateTimeEdit{\n"
"background:rgba(245,124,0,0.7);\n"
"border-radius:5px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainAgregarUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 140, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 180, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 220, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 260, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(400, 300, 55, 16))
        self.label_8.setObjectName("label_8")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(500, 100, 371, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(500, 140, 371, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(500, 180, 371, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(500, 220, 371, 22))
        self.txtTelefono.setMaxLength(10)
        self.txtTelefono.setPlaceholderText("")
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtCorreo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCorreo.setGeometry(QtCore.QRect(500, 260, 371, 22))
        self.txtCorreo.setObjectName("txtCorreo")
        self.cboTipo = QtWidgets.QComboBox(self.centralwidget)
        self.cboTipo.setGeometry(QtCore.QRect(500, 300, 371, 21))
        self.cboTipo.setObjectName("cboTipo")
        self.cboTipo.addItem("")
        self.cboTipo.addItem("")
        self.btnAgregarUsuario = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregarUsuario.setGeometry(QtCore.QRect(780, 420, 93, 28))
        self.btnAgregarUsuario.setStyleSheet("")
        self.btnAgregarUsuario.setObjectName("btnAgregarUsuario")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(420, 420, 93, 28))
        self.btnCancelar.setStyleSheet("")
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 1281, 801))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.txtRut.raise_()
        self.txtNombre.raise_()
        self.txtApellido.raise_()
        self.txtTelefono.raise_()
        self.txtCorreo.raise_()
        self.cboTipo.raise_()
        self.btnAgregarUsuario.raise_()
        self.btnCancelar.raise_()
        MainAgregarUsuario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainAgregarUsuario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1269, 26))
        self.menubar.setObjectName("menubar")
        MainAgregarUsuario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainAgregarUsuario)
        self.statusbar.setObjectName("statusbar")
        MainAgregarUsuario.setStatusBar(self.statusbar)

        self.retranslateUi(MainAgregarUsuario)
        QtCore.QMetaObject.connectSlotsByName(MainAgregarUsuario)

    def retranslateUi(self, MainAgregarUsuario):
        _translate = QtCore.QCoreApplication.translate
        MainAgregarUsuario.setWindowTitle(_translate("MainAgregarUsuario", "MainWindow"))
        self.label.setText(_translate("MainAgregarUsuario", "Agregar Usuario"))
        self.label_2.setText(_translate("MainAgregarUsuario", "Rut"))
        self.label_3.setText(_translate("MainAgregarUsuario", "Nombre"))
        self.label_4.setText(_translate("MainAgregarUsuario", "Apellido"))
        self.label_5.setText(_translate("MainAgregarUsuario", "Telefono"))
        self.label_6.setText(_translate("MainAgregarUsuario", "Correo"))
        self.label_8.setText(_translate("MainAgregarUsuario", "Tipo"))
        self.cboTipo.setItemText(0, _translate("MainAgregarUsuario", "Guardia"))
        self.cboTipo.setItemText(1, _translate("MainAgregarUsuario", "Administrador"))
        self.btnAgregarUsuario.setText(_translate("MainAgregarUsuario", "Agregar"))
        self.btnCancelar.setText(_translate("MainAgregarUsuario", "Cancelar"))

import tesr_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainAgregarUsuario = QtWidgets.QMainWindow()
    ui = Ui_MainAgregarUsuario()
    ui.setupUi(MainAgregarUsuario)
    MainAgregarUsuario.show()
    sys.exit(app.exec_())


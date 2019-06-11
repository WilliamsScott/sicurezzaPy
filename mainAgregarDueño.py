# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAgregarDueño.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainAgregarDueno(object):
    def setupUi(self, MainAgregarDueno):
        MainAgregarDueno.setObjectName("MainAgregarDueno")
        MainAgregarDueno.resize(1272, 828)
        MainAgregarDueno.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainAgregarDueno)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 110, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 150, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 190, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 230, 55, 16))
        self.label_5.setObjectName("label_5")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(510, 110, 351, 31))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(510, 150, 351, 31))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(510, 190, 351, 31))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(510, 230, 351, 31))
        self.txtTelefono.setObjectName("txtTelefono")
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(1100, 600, 93, 28))
        self.btnAgregar.setObjectName("btnAgregar")
        self.cbtnIrDeptos = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cbtnIrDeptos.setGeometry(QtCore.QRect(470, 580, 351, 48))
        self.cbtnIrDeptos.setObjectName("cbtnIrDeptos")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1281, 801))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_6.setObjectName("label_6")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(80, 610, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.txtRut.raise_()
        self.txtNombre.raise_()
        self.txtApellido.raise_()
        self.txtTelefono.raise_()
        self.btnAgregar.raise_()
        self.cbtnIrDeptos.raise_()
        self.btnCancelar.raise_()
        MainAgregarDueno.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainAgregarDueno)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 26))
        self.menubar.setObjectName("menubar")
        MainAgregarDueno.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainAgregarDueno)
        self.statusbar.setObjectName("statusbar")
        MainAgregarDueno.setStatusBar(self.statusbar)

        self.retranslateUi(MainAgregarDueno)
        QtCore.QMetaObject.connectSlotsByName(MainAgregarDueno)

    def retranslateUi(self, MainAgregarDueno):
        _translate = QtCore.QCoreApplication.translate
        MainAgregarDueno.setWindowTitle(_translate("MainAgregarDueno", "MainWindow"))
        self.label.setText(_translate("MainAgregarDueno", "Agregar Dueño"))
        self.label_2.setText(_translate("MainAgregarDueno", "Rut"))
        self.label_3.setText(_translate("MainAgregarDueno", "Nombre"))
        self.label_4.setText(_translate("MainAgregarDueno", "Apellido"))
        self.label_5.setText(_translate("MainAgregarDueno", "Telefono"))
        self.btnAgregar.setText(_translate("MainAgregarDueno", "Agregar"))
        self.cbtnIrDeptos.setText(_translate("MainAgregarDueno", "IR A DEPARTAMENTOS"))
        self.btnCancelar.setText(_translate("MainAgregarDueno", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainAgregarDueno = QtWidgets.QMainWindow()
    ui = Ui_MainAgregarDueno()
    ui.setupUi(MainAgregarDueno)
    MainAgregarDueno.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainRR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainRR(object):
    def setupUi(self, MainRR):
        MainRR.setObjectName("MainRR")
        MainRR.resize(1274, 834)
        MainRR.setStyleSheet("QMainWindow{\n"
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
"QComboBox{\n"
"background:rgba(245,124,0,0.7);\n"
"border-radius:15px;\n"
"}\n"
"QRadioButton{\n"
"color:orange\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainRR)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 170, 55, 16))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 130, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 250, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 370, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 330, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 290, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 210, 55, 16))
        self.label_5.setObjectName("label_5")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(470, 130, 381, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(470, 170, 381, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(470, 210, 381, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.cboEdficio = QtWidgets.QComboBox(self.centralwidget)
        self.cboEdficio.setGeometry(QtCore.QRect(470, 250, 381, 21))
        self.cboEdficio.setObjectName("cboEdficio")
        self.cboDepartamento = QtWidgets.QComboBox(self.centralwidget)
        self.cboDepartamento.setGeometry(QtCore.QRect(470, 290, 381, 21))
        self.cboDepartamento.setObjectName("cboDepartamento")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(470, 330, 381, 22))
        self.txtTelefono.setObjectName("txtTelefono")
        self.rbVehiculoNo = QtWidgets.QRadioButton(self.centralwidget)
        self.rbVehiculoNo.setGeometry(QtCore.QRect(470, 370, 95, 20))
        self.rbVehiculoNo.setStyleSheet("")
        self.rbVehiculoNo.setChecked(True)
        self.rbVehiculoNo.setObjectName("rbVehiculoNo")
        self.rbVehiculoSi = QtWidgets.QRadioButton(self.centralwidget)
        self.rbVehiculoSi.setGeometry(QtCore.QRect(550, 370, 95, 20))
        self.rbVehiculoSi.setStyleSheet("")
        self.rbVehiculoSi.setObjectName("rbVehiculoSi")
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(1090, 520, 93, 28))
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(110, 500, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 1281, 801))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1190, 10, 61, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1190, 40, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_8.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.txtRut.raise_()
        self.txtNombre.raise_()
        self.txtApellido.raise_()
        self.cboEdficio.raise_()
        self.cboDepartamento.raise_()
        self.txtTelefono.raise_()
        self.rbVehiculoNo.raise_()
        self.rbVehiculoSi.raise_()
        self.btnRegistrar.raise_()
        self.btnCancelar.raise_()
        self.label_14.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        MainRR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainRR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 26))
        self.menubar.setObjectName("menubar")
        MainRR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainRR)
        self.statusbar.setObjectName("statusbar")
        MainRR.setStatusBar(self.statusbar)

        self.retranslateUi(MainRR)
        QtCore.QMetaObject.connectSlotsByName(MainRR)

    def retranslateUi(self, MainRR):
        _translate = QtCore.QCoreApplication.translate
        MainRR.setWindowTitle(_translate("MainRR", "Registrar Residente"))
        self.label_6.setText(_translate("MainRR", "Nombre"))
        self.label.setText(_translate("MainRR", "RUT"))
        self.label_2.setText(_translate("MainRR", "Edificio"))
        self.label_7.setText(_translate("MainRR", "Vehiculo"))
        self.label_3.setText(_translate("MainRR", "Telefono"))
        self.label_4.setText(_translate("MainRR", "Departamento"))
        self.label_5.setText(_translate("MainRR", "Apellido"))
        self.rbVehiculoNo.setText(_translate("MainRR", "No"))
        self.rbVehiculoSi.setText(_translate("MainRR", "Sí"))
        self.btnRegistrar.setText(_translate("MainRR", "Registrar"))
        self.btnCancelar.setText(_translate("MainRR", "Cancelar"))
        self.label_14.setText(_translate("MainRR", "Registrar Residente"))
        self.label_10.setText(_translate("MainRR", "Sicurezza"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainRR = QtWidgets.QMainWindow()
    ui = Ui_MainRR()
    ui.setupUi(MainRR)
    MainRR.show()
    sys.exit(app.exec_())


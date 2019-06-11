# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEditarDueño.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainEditarDueno(object):
    def setupUi(self, MainEditarDueno):
        MainEditarDueno.setObjectName("MainEditarDueno")
        MainEditarDueno.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEditarDueno)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 120, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 160, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 200, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 240, 55, 16))
        self.label_5.setObjectName("label_5")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(310, 120, 251, 22))
        self.txtRut.setObjectName("txtRut")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(310, 160, 251, 22))
        self.txtNombre.setObjectName("txtNombre")
        self.txtApellido = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellido.setGeometry(QtCore.QRect(310, 200, 251, 22))
        self.txtApellido.setObjectName("txtApellido")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(310, 240, 251, 22))
        self.txtTelefono.setObjectName("txtTelefono")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(580, 120, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(570, 370, 93, 28))
        self.btnGuardar.setObjectName("btnGuardar")
        MainEditarDueno.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEditarDueno)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEditarDueno.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEditarDueno)
        self.statusbar.setObjectName("statusbar")
        MainEditarDueno.setStatusBar(self.statusbar)

        self.retranslateUi(MainEditarDueno)
        QtCore.QMetaObject.connectSlotsByName(MainEditarDueno)

    def retranslateUi(self, MainEditarDueno):
        _translate = QtCore.QCoreApplication.translate
        MainEditarDueno.setWindowTitle(_translate("MainEditarDueno", "MainWindow"))
        self.label.setText(_translate("MainEditarDueno", "Editar  Dueño"))
        self.label_2.setText(_translate("MainEditarDueno", "Rut"))
        self.label_3.setText(_translate("MainEditarDueno", "Nombre"))
        self.label_4.setText(_translate("MainEditarDueno", "Apellido"))
        self.label_5.setText(_translate("MainEditarDueno", "Telefono"))
        self.btnBuscar.setText(_translate("MainEditarDueno", "Buscar"))
        self.btnGuardar.setText(_translate("MainEditarDueno", "Guardar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEditarDueno = QtWidgets.QMainWindow()
    ui = Ui_MainEditarDueno()
    ui.setupUi(MainEditarDueno)
    MainEditarDueno.show()
    sys.exit(app.exec_())


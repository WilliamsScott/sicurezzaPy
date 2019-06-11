# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 400)
        MainWindow.setMinimumSize(QtCore.QSize(550, 400))
        MainWindow.setMaximumSize(QtCore.QSize(550, 400))
        MainWindow.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(170, 130, 221, 31))
        self.txtUser.setObjectName("txtUser")
        self.txtPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPass.setGeometry(QtCore.QRect(170, 190, 221, 31))
        self.txtPass.setText("")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(340, 260, 93, 28))
        self.btnLogin.setObjectName("btnLogin")
        self.btnTest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTest.setGeometry(QtCore.QRect(120, 260, 93, 28))
        self.btnTest.setObjectName("btnTest")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 110, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 170, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 100, 55, 16))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../user.png"))
        self.label_6.setObjectName("label_6")
        self.btnConfiguracion = QtWidgets.QPushButton(self.centralwidget)
        self.btnConfiguracion.setGeometry(QtCore.QRect(230, 320, 111, 28))
        self.btnConfiguracion.setObjectName("btnConfiguracion")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-310, -40, 1021, 421))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 0, 61, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 30, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_5.raise_()
        self.txtUser.raise_()
        self.txtPass.raise_()
        self.btnLogin.raise_()
        self.btnTest.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.btnConfiguracion.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnLogin.setIcon(QIcon(QPixmap("in.png")))
        self.btnTest.setIcon(QIcon(QPixmap("broom.png")))
        self.btnConfiguracion.setIcon(QIcon(QPixmap("config.png")))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Iniciar Sesión - Sicurezza"))
        self.btnLogin.setText(_translate("MainWindow", "Iniciar"))
        self.btnTest.setText(_translate("MainWindow", "Limpiar"))
        self.label.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Clave"))
        self.btnConfiguracion.setText(_translate("MainWindow", "Configuración"))
        self.label_4.setText(_translate("MainWindow", "Condominio San Agustin, Talca"))
        self.label_3.setText(_translate("MainWindow", "Sicurezza"))
        self.label_10.setText(_translate("MainWindow", "Sicurezza"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


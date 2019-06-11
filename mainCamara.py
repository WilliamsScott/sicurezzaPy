# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainCamara.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainCamara(object):
    def setupUi(self, MainCamara):
        MainCamara.setObjectName("MainCamara")
        MainCamara.resize(1274, 840)
        MainCamara.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainCamara)
        self.centralwidget.setObjectName("centralwidget")
        self.btnVerCamara = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerCamara.setGeometry(QtCore.QRect(580, 80, 93, 28))
        self.btnVerCamara.setObjectName("btnVerCamara")
        self.btnPrueba = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrueba.setGeometry(QtCore.QRect(20, 430, 93, 28))
        self.btnPrueba.setObjectName("btnPrueba")
        self.labelPrueba = QtWidgets.QLabel(self.centralwidget)
        self.labelPrueba.setGeometry(QtCore.QRect(30, 400, 55, 16))
        self.labelPrueba.setObjectName("labelPrueba")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(50, 660, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnExcel = QtWidgets.QPushButton(self.centralwidget)
        self.btnExcel.setGeometry(QtCore.QRect(30, 490, 93, 28))
        self.btnExcel.setObjectName("btnExcel")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 0, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1281, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label.setObjectName("label")
        self.txtDireccion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccion.setGeometry(QtCore.QRect(430, 230, 381, 22))
        self.txtDireccion.setObjectName("txtDireccion")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 230, 111, 20))
        self.label_2.setObjectName("label_2")
        self.btnVerCamara_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerCamara_2.setGeometry(QtCore.QRect(820, 230, 93, 28))
        self.btnVerCamara_2.setObjectName("btnVerCamara_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1200, 10, 61, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1200, 40, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label.raise_()
        self.btnVerCamara.raise_()
        self.btnPrueba.raise_()
        self.labelPrueba.raise_()
        self.btnCancelar.raise_()
        self.btnExcel.raise_()
        self.label_14.raise_()
        self.txtDireccion.raise_()
        self.label_2.raise_()
        self.btnVerCamara_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        MainCamara.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainCamara)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1274, 26))
        self.menubar.setObjectName("menubar")
        MainCamara.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainCamara)
        self.statusbar.setObjectName("statusbar")
        MainCamara.setStatusBar(self.statusbar)
        self.actionVer_en_vivo = QtWidgets.QAction(MainCamara)
        self.actionVer_en_vivo.setObjectName("actionVer_en_vivo")

        self.retranslateUi(MainCamara)
        QtCore.QMetaObject.connectSlotsByName(MainCamara)

    def retranslateUi(self, MainCamara):
        _translate = QtCore.QCoreApplication.translate
        MainCamara.setWindowTitle(_translate("MainCamara", "MainWindow"))
        self.btnVerCamara.setText(_translate("MainCamara", "Ver cámara"))
        self.btnPrueba.setText(_translate("MainCamara", "PushButton"))
        self.labelPrueba.setText(_translate("MainCamara", "TextLabel"))
        self.btnCancelar.setText(_translate("MainCamara", "Cancelar"))
        self.btnExcel.setText(_translate("MainCamara", "excel"))
        self.label_14.setText(_translate("MainCamara", "Ver Cámara"))
        self.label_2.setText(_translate("MainCamara", "Ingresar dirección"))
        self.btnVerCamara_2.setText(_translate("MainCamara", "Ver cámara 2"))
        self.label_10.setText(_translate("MainCamara", "Sicurezza"))
        self.actionVer_en_vivo.setText(_translate("MainCamara", "Ver en vivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainCamara = QtWidgets.QMainWindow()
    ui = Ui_MainCamara()
    ui.setupUi(MainCamara)
    MainCamara.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainBuscarResidente.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBuscarR(object):
    def setupUi(self, MainBuscarR):
        MainBuscarR.setObjectName("MainBuscarR")
        MainBuscarR.resize(1191, 838)
        MainBuscarR.setMinimumSize(QtCore.QSize(1200, 830))
        MainBuscarR.setMaximumSize(QtCore.QSize(1200, 830))
        MainBuscarR.setStyleSheet("QMainWindow{\n"
"background:#16161E;\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainBuscarR)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 100, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBuscar.setGeometry(QtCore.QRect(390, 90, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtBuscar.setFont(font)
        self.txtBuscar.setObjectName("txtBuscar")
        self.btnBuscarResidente = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarResidente.setGeometry(QtCore.QRect(710, 90, 93, 28))
        self.btnBuscarResidente.setStyleSheet("")
        self.btnBuscarResidente.setObjectName("btnBuscarResidente")
        self.tableResidentes = QtWidgets.QTableWidget(self.centralwidget)
        self.tableResidentes.setGeometry(QtCore.QRect(80, 180, 1001, 311))
        self.tableResidentes.setObjectName("tableResidentes")
        self.tableResidentes.setColumnCount(8)
        self.tableResidentes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResidentes.setHorizontalHeaderItem(7, item)
        self.tableResidentes.verticalHeader().setVisible(False)
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(50, 570, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:orange\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(-80, -20, 1281, 831))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1120, 10, 61, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1120, 40, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_3.raise_()
        self.label.raise_()
        self.txtBuscar.raise_()
        self.btnBuscarResidente.raise_()
        self.tableResidentes.raise_()
        self.btnCancelar.raise_()
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        MainBuscarR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBuscarR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 26))
        self.menubar.setObjectName("menubar")
        MainBuscarR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBuscarR)
        self.statusbar.setObjectName("statusbar")
        MainBuscarR.setStatusBar(self.statusbar)

        self.retranslateUi(MainBuscarR)
        QtCore.QMetaObject.connectSlotsByName(MainBuscarR)

    def retranslateUi(self, MainBuscarR):
        _translate = QtCore.QCoreApplication.translate
        MainBuscarR.setWindowTitle(_translate("MainBuscarR", "MainWindow"))
        self.label.setText(_translate("MainBuscarR", "Rut"))
        self.btnBuscarResidente.setText(_translate("MainBuscarR", "Buscar"))
        item = self.tableResidentes.horizontalHeaderItem(0)
        item.setText(_translate("MainBuscarR", "RUT"))
        item = self.tableResidentes.horizontalHeaderItem(1)
        item.setText(_translate("MainBuscarR", "Nombre"))
        item = self.tableResidentes.horizontalHeaderItem(2)
        item.setText(_translate("MainBuscarR", "Apellido"))
        item = self.tableResidentes.horizontalHeaderItem(3)
        item.setText(_translate("MainBuscarR", "Edificio"))
        item = self.tableResidentes.horizontalHeaderItem(4)
        item.setText(_translate("MainBuscarR", "Departamento"))
        item = self.tableResidentes.horizontalHeaderItem(5)
        item.setText(_translate("MainBuscarR", "Telefono"))
        item = self.tableResidentes.horizontalHeaderItem(6)
        item.setText(_translate("MainBuscarR", "Vehiculo"))
        item = self.tableResidentes.horizontalHeaderItem(7)
        item.setText(_translate("MainBuscarR", "Fecha"))
        self.btnCancelar.setText(_translate("MainBuscarR", "Cancelar"))
        self.label_2.setText(_translate("MainBuscarR", "Buscar Residente"))
        self.label_8.setText(_translate("MainBuscarR", "Sicurezza"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBuscarR = QtWidgets.QMainWindow()
    ui = Ui_MainBuscarR()
    ui.setupUi(MainBuscarR)
    MainBuscarR.show()
    sys.exit(app.exec_())


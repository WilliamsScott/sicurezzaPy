# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainBuscarVisita.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBuscarV(object):
    def setupUi(self, MainBuscarV):
        MainBuscarV.setObjectName("MainBuscarV")
        MainBuscarV.resize(1200, 830)
        MainBuscarV.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget = QtWidgets.QWidget(MainBuscarV)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtBuscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBuscar.setGeometry(QtCore.QRect(430, 130, 401, 31))
        self.txtBuscar.setStyleSheet("")
        self.txtBuscar.setObjectName("txtBuscar")
        self.btnBuscarVisita = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarVisita.setGeometry(QtCore.QRect(860, 240, 93, 28))
        self.btnBuscarVisita.setObjectName("btnBuscarVisita")
        self.tableVisitas = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVisitas.setGeometry(QtCore.QRect(30, 320, 1131, 311))
        self.tableVisitas.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableVisitas.setObjectName("tableVisitas")
        self.tableVisitas.setColumnCount(9)
        self.tableVisitas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVisitas.setHorizontalHeaderItem(8, item)
        self.tableVisitas.verticalHeader().setVisible(False)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 200, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.fecha1 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fecha1.setGeometry(QtCore.QRect(490, 200, 341, 22))
        self.fecha1.setObjectName("fecha1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 200, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 240, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.fecha2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.fecha2.setGeometry(QtCore.QRect(490, 240, 341, 22))
        self.fecha2.setObjectName("fecha2")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(40, 710, 93, 28))
        self.btnCancelar.setObjectName("btnCancelar")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 1251, 791))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1130, 10, 61, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1130, 40, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.cboBuscarV = QtWidgets.QComboBox(self.centralwidget)
        self.cboBuscarV.setGeometry(QtCore.QRect(430, 90, 401, 31))
        self.cboBuscarV.setObjectName("cboBuscarV")
        self.cboBuscarV.addItem("")
        self.cboBuscarV.addItem("")
        self.cboBuscarV.addItem("")
        self.cboBuscarV.addItem("")
        self.label_6.raise_()
        self.label.raise_()
        self.txtBuscar.raise_()
        self.btnBuscarVisita.raise_()
        self.tableVisitas.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.fecha1.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.fecha2.raise_()
        self.btnCancelar.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.cboBuscarV.raise_()
        MainBuscarV.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBuscarV)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainBuscarV.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBuscarV)
        self.statusbar.setObjectName("statusbar")
        MainBuscarV.setStatusBar(self.statusbar)

        self.retranslateUi(MainBuscarV)
        QtCore.QMetaObject.connectSlotsByName(MainBuscarV)

    def retranslateUi(self, MainBuscarV):
        _translate = QtCore.QCoreApplication.translate
        MainBuscarV.setWindowTitle(_translate("MainBuscarV", "MainWindow"))
        self.label.setText(_translate("MainBuscarV", "Nombre o RUT"))
        self.btnBuscarVisita.setText(_translate("MainBuscarV", "Buscar"))
        item = self.tableVisitas.horizontalHeaderItem(0)
        item.setText(_translate("MainBuscarV", "RUT"))
        item = self.tableVisitas.horizontalHeaderItem(1)
        item.setText(_translate("MainBuscarV", "Nombre"))
        item = self.tableVisitas.horizontalHeaderItem(2)
        item.setText(_translate("MainBuscarV", "Apellido"))
        item = self.tableVisitas.horizontalHeaderItem(3)
        item.setText(_translate("MainBuscarV", "Edificio"))
        item = self.tableVisitas.horizontalHeaderItem(4)
        item.setText(_translate("MainBuscarV", "Departamento"))
        item = self.tableVisitas.horizontalHeaderItem(5)
        item.setText(_translate("MainBuscarV", "Telefono"))
        item = self.tableVisitas.horizontalHeaderItem(6)
        item.setText(_translate("MainBuscarV", "Vehiculo"))
        item = self.tableVisitas.horizontalHeaderItem(7)
        item.setText(_translate("MainBuscarV", "Fecha"))
        item = self.tableVisitas.horizontalHeaderItem(8)
        item.setText(_translate("MainBuscarV", "Registrado por"))
        self.label_2.setText(_translate("MainBuscarV", "Buscar Visita"))
        self.label_3.setText(_translate("MainBuscarV", "Fecha (dd/mm/aaaa)"))
        self.label_4.setText(_translate("MainBuscarV", "Desde"))
        self.label_5.setText(_translate("MainBuscarV", "Hasta"))
        self.btnCancelar.setText(_translate("MainBuscarV", "Cancelar"))
        self.label_8.setText(_translate("MainBuscarV", "Sicurezza"))
        self.label_9.setText(_translate("MainBuscarV", "Buscar por"))
        self.cboBuscarV.setItemText(0, _translate("MainBuscarV", "-Seleccione opcion-"))
        self.cboBuscarV.setItemText(1, _translate("MainBuscarV", "RUT"))
        self.cboBuscarV.setItemText(2, _translate("MainBuscarV", "Fecha"))
        self.cboBuscarV.setItemText(3, _translate("MainBuscarV", "RUT y fecha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBuscarV = QtWidgets.QMainWindow()
    ui = Ui_MainBuscarV()
    ui.setupUi(MainBuscarV)
    MainBuscarV.show()
    sys.exit(app.exec_())


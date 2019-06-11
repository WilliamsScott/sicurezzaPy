# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainBuscarArrendatario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBuscarArrendatario(object):
    def setupUi(self, MainBuscarArrendatario):
        MainBuscarArrendatario.setObjectName("MainBuscarArrendatario")
        MainBuscarArrendatario.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainBuscarArrendatario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 110, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtArrendatario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtArrendatario.setGeometry(QtCore.QRect(220, 110, 291, 22))
        self.txtArrendatario.setObjectName("txtArrendatario")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(540, 110, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableDueno = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDueno.setGeometry(QtCore.QRect(130, 240, 521, 192))
        self.tableDueno.setObjectName("tableDueno")
        self.tableDueno.setColumnCount(4)
        self.tableDueno.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDueno.setHorizontalHeaderItem(3, item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainBuscarArrendatario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBuscarArrendatario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainBuscarArrendatario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBuscarArrendatario)
        self.statusbar.setObjectName("statusbar")
        MainBuscarArrendatario.setStatusBar(self.statusbar)

        self.retranslateUi(MainBuscarArrendatario)
        QtCore.QMetaObject.connectSlotsByName(MainBuscarArrendatario)

    def retranslateUi(self, MainBuscarArrendatario):
        _translate = QtCore.QCoreApplication.translate
        MainBuscarArrendatario.setWindowTitle(_translate("MainBuscarArrendatario", "MainWindow"))
        self.label.setText(_translate("MainBuscarArrendatario", "Buscar Arrendatario"))
        self.label_2.setText(_translate("MainBuscarArrendatario", "Rut"))
        self.btnBuscar.setText(_translate("MainBuscarArrendatario", "Buscar"))
        item = self.tableDueno.horizontalHeaderItem(0)
        item.setText(_translate("MainBuscarArrendatario", "Rut"))
        item = self.tableDueno.horizontalHeaderItem(1)
        item.setText(_translate("MainBuscarArrendatario", "Nombre"))
        item = self.tableDueno.horizontalHeaderItem(2)
        item.setText(_translate("MainBuscarArrendatario", "Apellido"))
        item = self.tableDueno.horizontalHeaderItem(3)
        item.setText(_translate("MainBuscarArrendatario", "Telefono"))
        self.label_4.setText(_translate("MainBuscarArrendatario", "Datos Arrendatario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBuscarArrendatario = QtWidgets.QMainWindow()
    ui = Ui_MainBuscarArrendatario()
    ui.setupUi(MainBuscarArrendatario)
    MainBuscarArrendatario.show()
    sys.exit(app.exec_())


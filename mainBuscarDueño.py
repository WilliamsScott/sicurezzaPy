# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainBuscarDueño.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainBuscarDueno(object):
    def setupUi(self, MainBuscarDueno):
        MainBuscarDueno.setObjectName("MainBuscarDueno")
        MainBuscarDueno.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainBuscarDueno)
        self.centralwidget.setObjectName("centralwidget")
        self.cboDepartamento = QtWidgets.QComboBox(self.centralwidget)
        self.cboDepartamento.setGeometry(QtCore.QRect(300, 120, 251, 22))
        self.cboDepartamento.setObjectName("cboDepartamento")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cboEdficio = QtWidgets.QComboBox(self.centralwidget)
        self.cboEdficio.setGeometry(QtCore.QRect(300, 80, 251, 22))
        self.cboEdficio.setObjectName("cboEdficio")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableDueno = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDueno.setGeometry(QtCore.QRect(130, 230, 521, 192))
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
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(570, 150, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        MainBuscarDueno.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainBuscarDueno)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainBuscarDueno.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainBuscarDueno)
        self.statusbar.setObjectName("statusbar")
        MainBuscarDueno.setStatusBar(self.statusbar)

        self.retranslateUi(MainBuscarDueno)
        QtCore.QMetaObject.connectSlotsByName(MainBuscarDueno)

    def retranslateUi(self, MainBuscarDueno):
        _translate = QtCore.QCoreApplication.translate
        MainBuscarDueno.setWindowTitle(_translate("MainBuscarDueno", "MainWindow"))
        self.label.setText(_translate("MainBuscarDueno", "Buscar Dueño"))
        self.label_2.setText(_translate("MainBuscarDueno", "Edificio"))
        self.label_4.setText(_translate("MainBuscarDueno", "Datos Dueño"))
        self.label_3.setText(_translate("MainBuscarDueno", "Departamento"))
        item = self.tableDueno.horizontalHeaderItem(0)
        item.setText(_translate("MainBuscarDueno", "Rut Dueño"))
        item = self.tableDueno.horizontalHeaderItem(1)
        item.setText(_translate("MainBuscarDueno", "Nombre"))
        item = self.tableDueno.horizontalHeaderItem(2)
        item.setText(_translate("MainBuscarDueno", "Apellido"))
        item = self.tableDueno.horizontalHeaderItem(3)
        item.setText(_translate("MainBuscarDueno", "Telefono"))
        self.btnBuscar.setText(_translate("MainBuscarDueno", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainBuscarDueno = QtWidgets.QMainWindow()
    ui = Ui_MainBuscarDueno()
    ui.setupUi(MainBuscarDueno)
    MainBuscarDueno.show()
    sys.exit(app.exec_())


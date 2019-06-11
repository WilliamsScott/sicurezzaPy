# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainEliminarDueño.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainEliminarDueno(object):
    def setupUi(self, MainEliminarDueno):
        MainEliminarDueno.setObjectName("MainEliminarDueno")
        MainEliminarDueno.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainEliminarDueno)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 170, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cboEdficio = QtWidgets.QComboBox(self.centralwidget)
        self.cboEdficio.setGeometry(QtCore.QRect(250, 130, 251, 22))
        self.cboEdficio.setObjectName("cboEdficio")
        self.cboDepartamento = QtWidgets.QComboBox(self.centralwidget)
        self.cboDepartamento.setGeometry(QtCore.QRect(250, 170, 251, 22))
        self.cboDepartamento.setObjectName("cboDepartamento")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(520, 200, 93, 28))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableDueno = QtWidgets.QTableWidget(self.centralwidget)
        self.tableDueno.setGeometry(QtCore.QRect(80, 280, 521, 192))
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
        self.label_4.setGeometry(QtCore.QRect(280, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(520, 490, 93, 28))
        self.btnEliminar.setObjectName("btnEliminar")
        MainEliminarDueno.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainEliminarDueno)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainEliminarDueno.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainEliminarDueno)
        self.statusbar.setObjectName("statusbar")
        MainEliminarDueno.setStatusBar(self.statusbar)

        self.retranslateUi(MainEliminarDueno)
        QtCore.QMetaObject.connectSlotsByName(MainEliminarDueno)

    def retranslateUi(self, MainEliminarDueno):
        _translate = QtCore.QCoreApplication.translate
        MainEliminarDueno.setWindowTitle(_translate("MainEliminarDueno", "MainWindow"))
        self.label.setText(_translate("MainEliminarDueno", "Eliminar Dueño"))
        self.label_2.setText(_translate("MainEliminarDueno", "Edificio"))
        self.label_3.setText(_translate("MainEliminarDueno", "Departamento"))
        self.btnBuscar.setText(_translate("MainEliminarDueno", "Buscar"))
        item = self.tableDueno.horizontalHeaderItem(0)
        item.setText(_translate("MainEliminarDueno", "Rut Dueño"))
        item = self.tableDueno.horizontalHeaderItem(1)
        item.setText(_translate("MainEliminarDueno", "Nombre"))
        item = self.tableDueno.horizontalHeaderItem(2)
        item.setText(_translate("MainEliminarDueno", "Apellido"))
        item = self.tableDueno.horizontalHeaderItem(3)
        item.setText(_translate("MainEliminarDueno", "Telefono"))
        self.label_4.setText(_translate("MainEliminarDueno", "Datos Dueño"))
        self.btnEliminar.setText(_translate("MainEliminarDueno", "Eliminar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainEliminarDueno = QtWidgets.QMainWindow()
    ui = Ui_MainEliminarDueno()
    ui.setupUi(MainEliminarDueno)
    MainEliminarDueno.show()
    sys.exit(app.exec_())


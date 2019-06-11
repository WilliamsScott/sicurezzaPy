# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainHabilitarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainHabilitarUsuario(object):
    def setupUi(self, MainHabilitarUsuario):
        MainHabilitarUsuario.setObjectName("MainHabilitarUsuario")
        MainHabilitarUsuario.resize(800, 600)
        MainHabilitarUsuario.setMinimumSize(QtCore.QSize(800, 600))
        MainHabilitarUsuario.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainHabilitarUsuario)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 40, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtRut = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRut.setGeometry(QtCore.QRect(170, 100, 391, 22))
        self.txtRut.setObjectName("txtRut")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(580, 90, 93, 41))
        self.btnBuscar.setObjectName("btnBuscar")
        self.tableUser = QtWidgets.QTableWidget(self.centralwidget)
        self.tableUser.setGeometry(QtCore.QRect(160, 160, 511, 91))
        self.tableUser.setObjectName("tableUser")
        self.tableUser.setColumnCount(4)
        self.tableUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUser.setHorizontalHeaderItem(3, item)
        self.btnDeshabilitar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeshabilitar.setEnabled(False)
        self.btnDeshabilitar.setGeometry(QtCore.QRect(430, 360, 93, 28))
        self.btnDeshabilitar.setObjectName("btnDeshabilitar")
        self.btnHabilitar = QtWidgets.QPushButton(self.centralwidget)
        self.btnHabilitar.setEnabled(True)
        self.btnHabilitar.setGeometry(QtCore.QRect(570, 360, 93, 28))
        self.btnHabilitar.setStyleSheet("")
        self.btnHabilitar.setObjectName("btnHabilitar")
        MainHabilitarUsuario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainHabilitarUsuario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainHabilitarUsuario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainHabilitarUsuario)
        self.statusbar.setObjectName("statusbar")
        MainHabilitarUsuario.setStatusBar(self.statusbar)

        self.retranslateUi(MainHabilitarUsuario)
        QtCore.QMetaObject.connectSlotsByName(MainHabilitarUsuario)

    def retranslateUi(self, MainHabilitarUsuario):
        _translate = QtCore.QCoreApplication.translate
        MainHabilitarUsuario.setWindowTitle(_translate("MainHabilitarUsuario", "MainWindow"))
        self.label.setText(_translate("MainHabilitarUsuario", "Habilitar / Deshabilitar Usuario"))
        self.btnBuscar.setText(_translate("MainHabilitarUsuario", "Buscar"))
        item = self.tableUser.horizontalHeaderItem(0)
        item.setText(_translate("MainHabilitarUsuario", "RUT"))
        item = self.tableUser.horizontalHeaderItem(1)
        item.setText(_translate("MainHabilitarUsuario", "Nombre"))
        item = self.tableUser.horizontalHeaderItem(2)
        item.setText(_translate("MainHabilitarUsuario", "Apellido"))
        item = self.tableUser.horizontalHeaderItem(3)
        item.setText(_translate("MainHabilitarUsuario", "Estado"))
        self.btnDeshabilitar.setText(_translate("MainHabilitarUsuario", "Deshabilitar"))
        self.btnHabilitar.setText(_translate("MainHabilitarUsuario", "Habilitar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainHabilitarUsuario = QtWidgets.QMainWindow()
    ui = Ui_MainHabilitarUsuario()
    ui.setupUi(MainHabilitarUsuario)
    MainHabilitarUsuario.show()
    sys.exit(app.exec_())


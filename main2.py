# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main2(object):
    def setupUi(self, main2):
        main2.setObjectName("main2")
        main2.resize(1216, 830)
        main2.setMinimumSize(QtCore.QSize(1216, 830))
        main2.setMaximumSize(QtCore.QSize(1216, 830))
        main2.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget = QtWidgets.QWidget(main2)
        self.centralwidget.setStyleSheet("QMainWindow{\n"
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
        self.centralwidget.setObjectName("centralwidget")
        self.tableTest = QtWidgets.QTableWidget(self.centralwidget)
        self.tableTest.setGeometry(QtCore.QRect(470, 120, 251, 561))
        self.tableTest.setStyleSheet("border-radius:10px;\n"
"")
        self.tableTest.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableTest.setObjectName("tableTest")
        self.tableTest.setColumnCount(2)
        self.tableTest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTest.setHorizontalHeaderItem(1, item)
        self.tableTest.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 50, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 440, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1221, 801))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fondo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1150, 10, 61, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1150, 40, 55, 16))
        self.label_8.setObjectName("label_8")
        self.btnRevisar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRevisar.setGeometry(QtCore.QRect(730, 120, 93, 28))
        self.btnRevisar.setObjectName("btnRevisar")
        self.label_2.raise_()
        self.tableTest.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.btnRevisar.raise_()
        main2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1216, 26))
        self.menubar.setObjectName("menubar")
        self.menuC_maras = QtWidgets.QMenu(self.menubar)
        self.menuC_maras.setObjectName("menuC_maras")
        self.menuResidentes = QtWidgets.QMenu(self.menubar)
        self.menuResidentes.setObjectName("menuResidentes")
        self.menuVisitas = QtWidgets.QMenu(self.menubar)
        self.menuVisitas.setObjectName("menuVisitas")
        self.menuVehiculos = QtWidgets.QMenu(self.menubar)
        self.menuVehiculos.setObjectName("menuVehiculos")
        self.menuAdministraci_n = QtWidgets.QMenu(self.menubar)
        self.menuAdministraci_n.setObjectName("menuAdministraci_n")
        self.menuAdministraci_n_2 = QtWidgets.QMenu(self.menubar)
        self.menuAdministraci_n_2.setObjectName("menuAdministraci_n_2")
        self.menuDue_os = QtWidgets.QMenu(self.menuAdministraci_n_2)
        self.menuDue_os.setObjectName("menuDue_os")
        self.menuArrendatarios = QtWidgets.QMenu(self.menuAdministraci_n_2)
        self.menuArrendatarios.setObjectName("menuArrendatarios")
        self.menuUsuarios = QtWidgets.QMenu(self.menubar)
        self.menuUsuarios.setObjectName("menuUsuarios")
        main2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main2)
        self.statusbar.setObjectName("statusbar")
        main2.setStatusBar(self.statusbar)
        self.actionVerCamara = QtWidgets.QAction(main2)
        self.actionVerCamara.setObjectName("actionVerCamara")
        self.actionAgregar_Residente = QtWidgets.QAction(main2)
        self.actionAgregar_Residente.setObjectName("actionAgregar_Residente")
        self.actionEditar_Residente = QtWidgets.QAction(main2)
        self.actionEditar_Residente.setObjectName("actionEditar_Residente")
        self.actionBuscar_Residente = QtWidgets.QAction(main2)
        self.actionBuscar_Residente.setObjectName("actionBuscar_Residente")
        self.actionEliminar_Residente = QtWidgets.QAction(main2)
        self.actionEliminar_Residente.setObjectName("actionEliminar_Residente")
        self.actionBuscar_vehiculo = QtWidgets.QAction(main2)
        self.actionBuscar_vehiculo.setObjectName("actionBuscar_vehiculo")
        self.actionA_adir_vehiculo_residente = QtWidgets.QAction(main2)
        self.actionA_adir_vehiculo_residente.setObjectName("actionA_adir_vehiculo_residente")
        self.actionEliminar_vehiculo_residente = QtWidgets.QAction(main2)
        self.actionEliminar_vehiculo_residente.setObjectName("actionEliminar_vehiculo_residente")
        self.actionAgregarVisita = QtWidgets.QAction(main2)
        self.actionAgregarVisita.setObjectName("actionAgregarVisita")
        self.actionBuscar_visita = QtWidgets.QAction(main2)
        self.actionBuscar_visita.setObjectName("actionBuscar_visita")
        self.actionVer_en_vivo_2 = QtWidgets.QAction(main2)
        self.actionVer_en_vivo_2.setObjectName("actionVer_en_vivo_2")
        self.actionAgregar_estacionamiento = QtWidgets.QAction(main2)
        self.actionAgregar_estacionamiento.setObjectName("actionAgregar_estacionamiento")
        self.actionQuitar_estacionamiento = QtWidgets.QAction(main2)
        self.actionQuitar_estacionamiento.setObjectName("actionQuitar_estacionamiento")
        self.actionReservar_estacionamiento = QtWidgets.QAction(main2)
        self.actionReservar_estacionamiento.setObjectName("actionReservar_estacionamiento")
        self.actionAgregar_Usuario = QtWidgets.QAction(main2)
        self.actionAgregar_Usuario.setObjectName("actionAgregar_Usuario")
        self.actionEditar_Usuario = QtWidgets.QAction(main2)
        self.actionEditar_Usuario.setObjectName("actionEditar_Usuario")
        self.actionQuitar_Usuario = QtWidgets.QAction(main2)
        self.actionQuitar_Usuario.setObjectName("actionQuitar_Usuario")
        self.actionMostar_Edificios = QtWidgets.QAction(main2)
        self.actionMostar_Edificios.setObjectName("actionMostar_Edificios")
        self.actionBuscar_Departamento = QtWidgets.QAction(main2)
        self.actionBuscar_Departamento.setObjectName("actionBuscar_Departamento")
        self.actionEditar_Departamento = QtWidgets.QAction(main2)
        self.actionEditar_Departamento.setObjectName("actionEditar_Departamento")
        self.actionAgregar = QtWidgets.QAction(main2)
        self.actionAgregar.setObjectName("actionAgregar")
        self.actionEditar = QtWidgets.QAction(main2)
        self.actionEditar.setObjectName("actionEditar")
        self.actionEliminar = QtWidgets.QAction(main2)
        self.actionEliminar.setObjectName("actionEliminar")
        self.actionBuscar = QtWidgets.QAction(main2)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionAgregar_2 = QtWidgets.QAction(main2)
        self.actionAgregar_2.setObjectName("actionAgregar_2")
        self.actionQuitar = QtWidgets.QAction(main2)
        self.actionQuitar.setObjectName("actionQuitar")
        self.actionBuscar_2 = QtWidgets.QAction(main2)
        self.actionBuscar_2.setObjectName("actionBuscar_2")
        self.actionEditar_2 = QtWidgets.QAction(main2)
        self.actionEditar_2.setObjectName("actionEditar_2")
        self.actionEliminar_2 = QtWidgets.QAction(main2)
        self.actionEliminar_2.setObjectName("actionEliminar_2")
        self.actionBuscar_3 = QtWidgets.QAction(main2)
        self.actionBuscar_3.setObjectName("actionBuscar_3")
        self.actionAsignar = QtWidgets.QAction(main2)
        self.actionAsignar.setObjectName("actionAsignar")
        self.actionGenerar_Informe = QtWidgets.QAction(main2)
        self.actionGenerar_Informe.setObjectName("actionGenerar_Informe")
        self.menuC_maras.addAction(self.actionVerCamara)
        self.menuResidentes.addAction(self.actionAgregar_Residente)
        self.menuResidentes.addAction(self.actionEditar_Residente)
        self.menuResidentes.addAction(self.actionBuscar_Residente)
        self.menuResidentes.addAction(self.actionEliminar_Residente)
        self.menuVisitas.addAction(self.actionAgregarVisita)
        self.menuVisitas.addAction(self.actionBuscar_visita)
        self.menuVehiculos.addAction(self.actionBuscar_vehiculo)
        self.menuVehiculos.addAction(self.actionA_adir_vehiculo_residente)
        self.menuVehiculos.addAction(self.actionEliminar_vehiculo_residente)
        self.menuAdministraci_n.addAction(self.actionVer_en_vivo_2)
        self.menuAdministraci_n.addAction(self.actionAgregar_estacionamiento)
        self.menuAdministraci_n.addAction(self.actionQuitar_estacionamiento)
        self.menuAdministraci_n.addAction(self.actionReservar_estacionamiento)
        self.menuDue_os.addAction(self.actionAgregar)
        self.menuDue_os.addAction(self.actionEditar)
        self.menuDue_os.addAction(self.actionEliminar)
        self.menuDue_os.addAction(self.actionBuscar_2)
        self.menuDue_os.addAction(self.actionAsignar)
        self.menuArrendatarios.addAction(self.actionAgregar_2)
        self.menuArrendatarios.addAction(self.actionEditar_2)
        self.menuArrendatarios.addAction(self.actionEliminar_2)
        self.menuArrendatarios.addAction(self.actionBuscar_3)
        self.menuAdministraci_n_2.addAction(self.actionMostar_Edificios)
        self.menuAdministraci_n_2.addAction(self.actionBuscar_Departamento)
        self.menuAdministraci_n_2.addAction(self.actionEditar_Departamento)
        self.menuAdministraci_n_2.addAction(self.menuDue_os.menuAction())
        self.menuAdministraci_n_2.addAction(self.menuArrendatarios.menuAction())
        self.menuAdministraci_n_2.addAction(self.actionGenerar_Informe)
        self.menuUsuarios.addAction(self.actionAgregar_Usuario)
        self.menuUsuarios.addAction(self.actionEditar_Usuario)
        self.menuUsuarios.addAction(self.actionQuitar_Usuario)
        self.menubar.addAction(self.menuC_maras.menuAction())
        self.menubar.addAction(self.menuResidentes.menuAction())
        self.menubar.addAction(self.menuVisitas.menuAction())
        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuVehiculos.menuAction())
        self.menubar.addAction(self.menuAdministraci_n.menuAction())
        self.menubar.addAction(self.menuAdministraci_n_2.menuAction())

        self.retranslateUi(main2)
        QtCore.QMetaObject.connectSlotsByName(main2)

    def retranslateUi(self, main2):
        _translate = QtCore.QCoreApplication.translate
        main2.setWindowTitle(_translate("main2", "Menu Principal"))
        item = self.tableTest.horizontalHeaderItem(0)
        item.setText(_translate("main2", "Número"))
        item = self.tableTest.horizontalHeaderItem(1)
        item.setText(_translate("main2", "Estado"))
        self.label.setText(_translate("main2", "Estacionamientos"))
        self.label_8.setText(_translate("main2", "Sicurezza"))
        self.btnRevisar.setText(_translate("main2", "Revisar"))
        self.menuC_maras.setTitle(_translate("main2", "Cámaras"))
        self.menuResidentes.setTitle(_translate("main2", "Residentes"))
        self.menuVisitas.setTitle(_translate("main2", "Visitas"))
        self.menuVehiculos.setTitle(_translate("main2", "Vehiculos"))
        self.menuAdministraci_n.setTitle(_translate("main2", "Estacionamientos"))
        self.menuAdministraci_n_2.setTitle(_translate("main2", "Administración"))
        self.menuDue_os.setTitle(_translate("main2", "Dueños"))
        self.menuArrendatarios.setTitle(_translate("main2", "Arrendatarios"))
        self.menuUsuarios.setTitle(_translate("main2", "Usuarios"))
        self.actionVerCamara.setText(_translate("main2", "Ver en vivo"))
        self.actionAgregar_Residente.setText(_translate("main2", "Agregar Residente"))
        self.actionEditar_Residente.setText(_translate("main2", "Editar Residente"))
        self.actionBuscar_Residente.setText(_translate("main2", "Buscar Residente"))
        self.actionEliminar_Residente.setText(_translate("main2", "Eliminar Residente"))
        self.actionBuscar_vehiculo.setText(_translate("main2", "Buscar vehiculo"))
        self.actionA_adir_vehiculo_residente.setText(_translate("main2", "Añadir vehiculo residente"))
        self.actionEliminar_vehiculo_residente.setText(_translate("main2", "Eliminar vehiculo residente"))
        self.actionAgregarVisita.setText(_translate("main2", "Agregar visita"))
        self.actionBuscar_visita.setText(_translate("main2", "Buscar visita"))
        self.actionVer_en_vivo_2.setText(_translate("main2", "Ver en vivo"))
        self.actionAgregar_estacionamiento.setText(_translate("main2", "Agregar estacionamiento"))
        self.actionQuitar_estacionamiento.setText(_translate("main2", "Quitar estacionamiento"))
        self.actionReservar_estacionamiento.setText(_translate("main2", "Reservar estacionamiento"))
        self.actionAgregar_Usuario.setText(_translate("main2", "Agregar Usuario"))
        self.actionEditar_Usuario.setText(_translate("main2", "Editar Usuario"))
        self.actionQuitar_Usuario.setText(_translate("main2", "Habilitar/ Deshabilitar Usuario"))
        self.actionMostar_Edificios.setText(_translate("main2", "Mostar Edificios"))
        self.actionBuscar_Departamento.setText(_translate("main2", "Buscar Departamento"))
        self.actionEditar_Departamento.setText(_translate("main2", "Editar Departamento"))
        self.actionAgregar.setText(_translate("main2", "Agregar"))
        self.actionEditar.setText(_translate("main2", "Editar"))
        self.actionEliminar.setText(_translate("main2", "Eliminar"))
        self.actionBuscar.setText(_translate("main2", "Buscar"))
        self.actionAgregar_2.setText(_translate("main2", "Agregar"))
        self.actionQuitar.setText(_translate("main2", "Quitar"))
        self.actionBuscar_2.setText(_translate("main2", "Buscar"))
        self.actionEditar_2.setText(_translate("main2", "Editar"))
        self.actionEliminar_2.setText(_translate("main2", "Eliminar"))
        self.actionBuscar_3.setText(_translate("main2", "Buscar"))
        self.actionAsignar.setText(_translate("main2", "Asignar"))
        self.actionGenerar_Informe.setText(_translate("main2", "Generar Informe"))

import tesr_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main2 = QtWidgets.QMainWindow()
    ui = Ui_main2()
    ui.setupUi(main2)
    main2.show()
    sys.exit(app.exec_())


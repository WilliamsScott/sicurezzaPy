from login_ui import *
import mysql.connector
from main2 import *
import numpy as np
import cv2
import xlwt
import time
import asyncio
import tracemalloc
from datetime import datetime
from itertools import cycle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from mainCamara import *
from mainRV import *
from mainBuscarVisita import *
from mainRR import *
from mainER import *
from mainBuscarResidente import*
from mainEliminarResidente import *
from mainAgregarUsuario import *
from mainEditarUsuario import *
from mainHabilitarUsuario import *
from mainBuscarVehiculo import *
from mainAgregarVehiculo import *
from mainEliminarVehiculo import *
from mainBuscarDepto import *
from mainMostrarEdificios import *
from mainAgregarDueño import *
from mainEditarDueño import *
from mainEliminarDueño import*
from mainReservarEstacionamiento import *
from mainAsignarDueño import *
from mainBuscarDueño import *
from mainAgregarArrendatario import *
from mainEditarArrendatario import *
from mainBuscarArrendatario import *
from mainEliminarArrendatario import*
from mainGenerarInforme import *

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sic"
)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.startLogin()

    def startLogin(self):
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnTest.clicked.connect(self.test)



    def aviso(self, title, message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def startCamara(self):
        self.ui=Ui_MainCamara()
        self.ui.setupUi(self)
        self.ui.btnVerCamara.clicked.connect(self.verCamara)
        self.ui.btnPrueba.clicked.connect(self.hola)
        self.ui.actionVer_en_vivo.triggered.connect(self.irMain)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startGenerarInforme(self):
        self.ui=Ui_MainGenerarInforme()
        self.ui.setupUi(self)
        self.ui.btnExcel.clicked.connect(self.informe)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def irMain(self):
        self.ui=Ui_main2()
        self.ui.setupUi(self)
        self.ui.btnRevisar.clicked.connect(self.irMain)
        self.setMinimumSize(QtCore.QSize(16777215, 16777215))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cargarEstacionamiento()
        self.ui.actionVerCamara.triggered.connect(self.startCamara)
        self.ui.actionAgregarVisita.triggered.connect(self.startVisita1)
        self.ui.actionBuscar_visita.triggered.connect(self.startBuscarVisita)
        self.ui.actionAgregar_Residente.triggered.connect(self.startResidente1)
        self.ui.actionEditar_Residente.triggered.connect(self.startResidente2)
        self.ui.actionBuscar_Residente.triggered.connect(self.startResidente3)
        self.ui.actionEliminar_Residente.triggered.connect(self.startResidente4)
        self.ui.actionAgregar_Usuario.triggered.connect(self.startAddUser)
        self.ui.actionEditar_Usuario.triggered.connect(self.startEditUser)
        self.ui.actionQuitar_Usuario.triggered.connect(self.startEnableUser)
        self.ui.actionBuscar_vehiculo.triggered.connect(self.startBuscarVehiculo)
        self.ui.actionA_adir_vehiculo_residente.triggered.connect(self.startAgregarVehiculo)
        self.ui.actionEliminar_vehiculo_residente.triggered.connect(self.startEliminarVehiculo)
        self.ui.actionBuscar_Departamento.triggered.connect(self.startBuscarDepto)
        self.ui.actionAgregar.triggered.connect(self.startDueno1)
        self.ui.actionEditar.triggered.connect(self.startDueno2)
        self.ui.actionEliminar.triggered.connect(self.startDueno4)
        self.ui.actionReservar_estacionamiento.triggered.connect(self.startReservarEstacionamiento)
        self.ui.actionAsignar.triggered.connect(self.startAsignarDueno)
        self.ui.actionBuscar_2.triggered.connect(self.startBuscarDueno)
        self.ui.actionMostar_Edificios.triggered.connect(self.startMostrarEdificios)
        self.ui.actionAgregar_2.triggered.connect(self.startArrendatario1)
        self.ui.actionEditar_2.triggered.connect(self.startArrendatario2)
        self.ui.actionBuscar_3.triggered.connect(self.startArrendatario3)
        self.ui.actionEliminar_2.triggered.connect(self.startArrendatario4)
        self.ui.actionGenerar_Informe.triggered.connect(self.startGenerarInforme)




    def startVisita1(self):
        self.ui=Ui_MainRV()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.llenarComboEstacionamiento()
        self.ui.btnBuscarVisitaR.clicked.connect(self.agregarBuscarVisita)
        self.ui.btnRegistrar.clicked.connect(self.agregarVisita)
        self.ui.rbVehiculoSi.clicked.connect(self.agregarVehiculoCbo)
        self.ui.rbVehiculoNo.clicked.connect(self.agregarVehiculoCbo2)
        self.ui.btnCancelar.clicked.connect(self.irMain)
        x=str(self.user)
        print(x)




    def startResidente1(self):
        self.ui=Ui_MainRR()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        #self.llenarComboEstacionamientoR()
        self.ui.btnRegistrar.clicked.connect(self.agregarResidente)
        self.ui.rbVehiculoSi.clicked.connect(self.agregarVehiculoCbo)
        self.ui.rbVehiculoNo.clicked.connect(self.agregarVehiculoCbo2)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startResidente2(self):
        self.ui=Ui_MainER()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.ui.btnBuscarR.clicked.connect(self.buscarEditarResidente)
        self.ui.btnEditar.clicked.connect(self.editarResidente)
        self.ui.btnCancelar.clicked.connect(self.irMain)


    def startResidente3(self):
        self.ui=Ui_MainBuscarR()
        self.ui.setupUi(self)
        self.cargarResidentes()
        self.cargarResidentes2()
        self.ui.btnBuscarResidente.clicked.connect(self.buscarResidente)
        self.ui.btnCancelar.clicked.connect(self.irMain)


    def startAddUser(self):
        self.ui=Ui_MainAgregarUsuario()
        self.ui.setupUi(self)
        self.ui.btnAgregarUsuario.clicked.connect(self.agregarUsuario)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startEditUser(self):
        self.ui=Ui_MainEditarUsuario()
        self.ui.setupUi(self)
        self.ui.bntBuscar.clicked.connect(self.buscarEditarUsuario)
        self.ui.btnEditar.clicked.connect(self.editarUsuario)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startEnableUser(self):
        self.ui=Ui_MainHabilitarUsuario()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarHabilitarUsuario)
        self.ui.btnDeshabilitar.clicked.connect(self.deshabilitarUsuario)
        self.ui.btnHabilitar.clicked.connect(self.habilitarUsuario)

    def startResidente4(self):
        self.ui=Ui_MainElimR()
        self.ui.setupUi(self)
        self.ui.btnBuscarResidente.clicked.connect(self.buscarEliminarResidente)
        self.ui.btnEliminar.clicked.connect(self.eliminarResidente)
        self.ui.tableResidentes.doubleClicked.connect(self.pruebaClick)
        self.ui.btnCancelar.clicked.connect(self.irMain)


    def startBuscarVisita(self):
        self.ui=Ui_MainBuscarV()
        self.ui.setupUi(self)
        self.cargarVisitas()
        self.ui.btnBuscarVisita.clicked.connect(self.buscarVisita)
        self.ui.btnCancelar.clicked.connect(self.irMain)
        #self.ui.calendarWidget.clicked[QtCore.QDate].connect(self.calendario)

    def startBuscarVehiculo(self):
        self.ui=Ui_MainBuscarVehiculo()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarVehiculo)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startEliminarVehiculo(self):
        self.ui=Ui_MainEliminarVehiculo()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarResidenteEV)
        self.ui.btnEliminar.clicked.connect(self.eliminarVehiculoR)

    def startAgregarVehiculo(self):
        self.ui=Ui_MainAgregarVehiculo()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarResidenteAV)
        self.ui.btnAgregar.clicked.connect(self.agregarVehiculoResidente)
        self.ui.btnCancelar.clicked.connect(self.irMain)
        self.ui.btnIrEstacionamientos.clicked.connect(self.startReservarEstacionamiento)

    def startBuscarDepto(self):
        self.ui=Ui_MainBuscarDepto()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarDepto)

    def startMostrarEdificios(self):
        self.ui=Ui_MainMostrarEdificios()
        self.ui.setupUi(self)
        self.cargarEdificios()

    def startDueno1(self):
        self.ui=Ui_MainAgregarDueno()
        self.ui.setupUi(self)
        self.ui.btnAgregar.clicked.connect(self.agregarDueno)
        self.ui.cbtnIrDeptos.clicked.connect(self.btnLink)
        self.ui.btnCancelar.clicked.connect(self.irMain)
    def startDueno2(self):
        self.ui=Ui_MainEditarDueno()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarDueno)
        self.ui.btnGuardar.clicked.connect(self.editarDueno)

    def startDueno4(self):
        self.ui=Ui_MainEliminarDueno()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.ui.btnBuscar.clicked.connect(self.buscarDuenoEl)
        self.ui.btnEliminar.clicked.connect(self.eliminarDueno)
    def startBuscarDueno(self):
        self.ui=Ui_MainBuscarDueno()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.ui.btnBuscar.clicked.connect(self.buscarDuenoEl)

    def btnLink(self):
        self.startAsignarDueno()

    def calendario(self):
        cal=self.ui.calendarWidget
        date=cal.selectedDate()
        self.ui.txtBuscar.setText(date.toString())
        print(str(date))

    def startReservarEstacionamiento(self):
        self.ui=Ui_MainReservarEstacionamiento()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarResidenteEst)
        self.ui.btnAgregar.clicked.connect(self.reservarEstacionamiento)
        self.ui.btnCancelar.clicked.connect(self.irMain)

    def startAsignarDueno(self):
        self.ui=Ui_MainAsignarDueno()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.ui.btnBuscar.clicked.connect(self.buscarDuenoEl)
        self.ui.btnGuardar.clicked.connect(self.asignarDueno)

    def startArrendatario1(self):
        self.ui=Ui_MainAgregarArrendatario()
        self.ui.setupUi(self)
        self.llenarCombo()
        self.ui.cboEdficio.currentIndexChanged.connect(self.llenarCombo2)
        self.llenarCombo2()
        self.ui.btnAgregar.clicked.connect(self.agregarArrendatario)

    def startArrendatario2(self):
        self.ui=Ui_MainEditarArrendatario()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarArrendatario)
        self.ui.btnGuardar.clicked.connect(self.editarArrendatario)

    def startArrendatario3(self):
        self.ui=Ui_MainBuscarArrendatario()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarArrendatariob)

    def startArrendatario4(self):
        self.ui=Ui_MainEliminarArrendatario()
        self.ui.setupUi(self)
        self.ui.btnBuscar.clicked.connect(self.buscarArrendatariob)
        self.ui.btnEliminar.clicked.connect(self.eliminarArrendatario)

    def getu(self):
        self.ui=Ui_main2()
        self.ui.setupUi(self)
        self.ui2=Ui_MainRV()
        self.ui2.setupUi(self)
        x=self.ui.label.text()
        print(x)

    user=None

    def login(self):

        user = self.ui.txtUser.text()
        clv = self.ui.txtPass.text()
        cursor=db.cursor()
        cursor.execute("select * from usuario where rut = '"+user+"' and clave = '"+clv+"'")
        data = cursor.fetchall()

        if(len(data)>0):
            if (data[0][7]==1):
                self.ui=Ui_main2()
                self.ui.setupUi(self)
                n=data[0][1]
                a= data[0][2]
                self.user=data[0][0]
                self.cargarEstacionamiento()
                self.ui.btnRevisar.clicked.connect(self.irMain)
                self.ui.actionVerCamara.triggered.connect(self.startCamara)
                self.ui.actionAgregarVisita.triggered.connect(self.startVisita1)
                self.ui.actionBuscar_visita.triggered.connect(self.startBuscarVisita)
                self.ui.actionAgregar_Residente.triggered.connect(self.startResidente1)
                self.ui.actionEditar_Residente.triggered.connect(self.startResidente2)
                self.ui.actionBuscar_Residente.triggered.connect(self.startResidente3)
                self.ui.actionEliminar_Residente.triggered.connect(self.startResidente4)
                self.ui.actionAgregar_Usuario.triggered.connect(self.startAddUser)
                self.ui.actionEditar_Usuario.triggered.connect(self.startEditUser)
                self.ui.actionQuitar_Usuario.triggered.connect(self.startEnableUser)
                self.ui.actionBuscar_vehiculo.triggered.connect(self.startBuscarVehiculo)
                self.ui.actionA_adir_vehiculo_residente.triggered.connect(self.startAgregarVehiculo)
                self.ui.actionEliminar_vehiculo_residente.triggered.connect(self.startEliminarVehiculo)
                self.ui.actionBuscar_Departamento.triggered.connect(self.startBuscarDepto)
                self.ui.actionAgregar.triggered.connect(self.startDueno1)
                self.ui.actionEditar.triggered.connect(self.startDueno2)
                self.ui.actionEliminar.triggered.connect(self.startDueno4)
                self.ui.actionReservar_estacionamiento.triggered.connect(self.startReservarEstacionamiento)
                self.ui.actionAsignar.triggered.connect(self.startAsignarDueno)
                self.ui.actionBuscar_2.triggered.connect(self.startBuscarDueno)
                self.ui.actionMostar_Edificios.triggered.connect(self.startMostrarEdificios)
                self.ui.actionAgregar_2.triggered.connect(self.startArrendatario1)
                self.ui.actionEditar_2.triggered.connect(self.startArrendatario2)
                self.ui.actionBuscar_3.triggered.connect(self.startArrendatario3)
                self.ui.actionEliminar_2.triggered.connect(self.startArrendatario4)
                self.ui.actionGenerar_Informe.triggered.connect(self.startGenerarInforme)


            else:
                self.aviso("Error", "Usuario Deshabilitado")

        else:
            self.aviso("Error", "Datos incorrectos")



    def test(self):
        self.ui.txtUser.setText("")
        self.ui.txtPass.setText("")

    def revisarEstacionamiento(self):
        table = self.ui.tableTest
        cur=db.cursor()
        cur.execute("select * from estacionamientovisita")
        data=cur.fetchall()
        numero = str(data[0][0])
        estado = data[0][1]
        db.commit()
        print (estado)

    #@asyncio.coroutine
    def cargarEstacionamiento(self):
        #while True:
            cur = db.cursor()
            query = "select * from estacionamientovisita"
            cur.execute(query)
            data = cur.fetchall()

            #yield from asyncio.sleep(5)
            #await asyncio.sleep(5)
            table = self.ui.tableTest
            for e in data:
                numero = str(e[0])
                estado = e[1]
                print(numero)
                rows = table.rowCount()
                table.insertRow(rows)

                table.setItem(rows, 0, QtWidgets.QTableWidgetItem(numero))
                if (estado == 0):
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem("Disponible"))
                else:
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem("Ocupado"))

            db.commit()

    #loop = asyncio.get_event_loop()
    #tasks=[asyncio.ensure_future(cargarEstacionamiento)]
    #loop.run_until_complete(asyncio.wait(tasks))
    #loop.close()

    def cargarVisitas(self):
        cur=db.cursor()
        query="SELECT visita.*, vehiculovisita.patente, edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita left join edificio on visita.edificio=edificio.id"
        cur.execute(query)
        data=cur.fetchall()
        table=self.ui.tableVisitas
        for v in data:
            rut=str(v[1])
            nombre=str(v[2])
            apellido = str(v[3])
            departamento = str(v[5])
            telefono = str(v[6])
            fecha = str(v[7])
            usuario = str(v[8])
            patente = str(v[9])
            ed = str(v[10])
            rows=table.rowCount()
            table.insertRow(rows)

            table.setItem(rows,0,QtWidgets.QTableWidgetItem(rut))
            table.setItem(rows,1,QtWidgets.QTableWidgetItem(nombre))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(ed))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
            table.setItem(rows, 7, QtWidgets.QTableWidgetItem(fecha))
            table.setItem(rows, 8, QtWidgets.QTableWidgetItem(usuario))

    def pruebaClick(self):
        table=self.ui.tableResidentes
        for idx in table.selectionModel().selectedIndexes():
            fila = idx.row()
            columna = idx.column()
            selected=table.selectedIndexes()
            dato1=selected[0].data()
            x=table.takeItem(fila,0)
            print(x)



            print (fila, columna, dato1)
        #table=self.ui.tableResidentes
        #selected=table.selectedIndexes()
        #dato1=selected[0].data
        #print (selected,dato1)


    def cargarResidentes(self):
        cur = db.cursor()
        # cur.execute("SELECT residente.*, vehiculoresidente.patente from residente join vehiculoresidente on residente.rut=vehiculoresidente.residente")
        cur.execute("select * from residente")
        data = cur.fetchall()

        table = self.ui.tableResidentes
        for r in data:
            rut = str(r[0])
            nombre = str(r[1])
            apellido = str(r[2])
            edificio = str(r[3])
            departamento = str(r[4])
            telefono = str(r[5])
            rows = table.rowCount()
            table.insertRow(rows)

            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(edificio))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))

    def cargarResidentes2(self):
        cur = db.cursor()
        cur.execute("SELECT residente.*, vehiculoresidente.patente from residente join vehiculoresidente on residente.rut=vehiculoresidente.residente")

        data = cur.fetchall()

        table = self.ui.tableResidentes
        for r in data:
            rut = str(r[0])
            nombre = str(r[1])
            apellido = str(r[2])
            edificio = str(r[3])
            departamento = str(r[4])
            telefono = str(r[5])
            patente = str(r[6])
            rows = table.rowCount()
            table.insertRow(rows)

            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(edificio))
            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))

    def cargarEdificios(self):
        cur=db.cursor()
        cur.execute("select * from edificio")
        data=cur.fetchall()
        table=self.ui.tableWidget
        for e in data:
            id=str(e[0])
            nombre=str(e[1])
            cur.execute("select * from residente where edificio='"+id+"'")
            residentes=cur.fetchall()
            r=str(len(residentes))
            rows = table.rowCount()
            table.insertRow(rows)
            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(nombre))
            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(r))



    def verCamara(self):
        try:
            cap = cv2.VideoCapture('http://192.168.3.156:4747/mjpegfeed?640x480')
            # = cv2.VideoCapture('http://admin:@192.168.3.96')

            while (True):
                ret, frame = cap.read()

                cv2.imshow('Camara 1', frame)

                if cv2.waitKey(20) & 0xFF == ord('q'):
                    break

            cap.release()
        except:
            pass
            self.aviso("Error","Camara no conectada")


    def hola(self):
        self.ui.labelPrueba.setText("caca")

    def agregarVehiculoCbo(self):

            self.ui.label_13.setEnabled(True)
            self.ui.label_8.setEnabled(True)
            self.ui.label_9.setEnabled(True)
            self.ui.label_10.setEnabled(True)
            self.ui.label_11.setEnabled(True)
            self.ui.txtPatente.setEnabled(True)
            self.ui.txtMarca.setEnabled(True)
            self.ui.txtModelo.setEnabled(True)
            self.ui.cboNEstacionamento.setEnabled(True)

    def agregarVehiculoCbo2(self):

            self.ui.label_13.setEnabled(False)
            self.ui.label_8.setEnabled(False)
            self.ui.label_9.setEnabled(False)
            self.ui.label_10.setEnabled(False)
            self.ui.label_11.setEnabled(False)
            self.ui.txtPatente.setEnabled(False)
            self.ui.txtMarca.setEnabled(False)
            self.ui.txtModelo.setEnabled(False)
            self.ui.cboNEstacionamento.setEnabled(False)

    def agregarBuscarVisita(self):
        rut=self.ui.txtRut.text()
        cursor = db.cursor()
        rut2 = self.validarRut(rut)
        if rut2 != False:
            rut2 = str(rut2)
            cursor.execute("select nombre,apellido,telefono from visita where rut = '"+rut2+"'")
            mysql=cursor.fetchall()
            le=(len(mysql)-1)
            if (mysql!=0):

                nombre = str(mysql[le][0])
                apellido = str(mysql[le][1])
                telefono = str(mysql[le][2])
                self.ui.txtNombre.setText(nombre)
                self.ui.txtApellido.setText(apellido)
                self.ui.txtTelefono.setText(telefono)
            else:
                self.aviso("No encontrado", "No se encontro el rut")
        else:
            self.aviso("Error", "Revise Rut")

    def agregarVisita(self):
        rut=self.ui.txtRut.text()
        nombre=self.ui.txtNombre.text()
        apellido= self.ui.txtApellido.text()
        edificio=self.ui.cboEdficio.currentText()
        departamento=self.ui.cboDepartamento.currentText()
        telefono= self.ui.txtTelefono.text()

        patente = self.ui.txtPatente.text()
        marca = self.ui.txtMarca.text()
        modelo = self.ui.txtModelo.text()
        usuario=self.user


        if (rut == "" or nombre == "" or apellido == "" or edificio == "" or departamento == "" or telefono == ""):
            self.aviso("Error", "Ingrese todos los datos")
        else:
            x = self.validarRut(rut)
            if x != False:
                x = str(x)

                cursor = db.cursor()
                idDepartamento = cursor.execute("select id from departamento where numero = '" + departamento + "'")
                idDepartamento = cursor.fetchone()
                idDepartamento = str(idDepartamento[0])

                idEdificio = cursor.execute("select id from edificio where nombre = '" + edificio + "'")
                idEdificio = cursor.fetchone()
                idEdificio = str(idEdificio[0])

                sql = cursor.execute("insert into visita (rut,nombre,apellido,edificio,departamento,telefono,usuario) values ('" + x + "','" + nombre + "','" + apellido + "','" + idEdificio + "','" + idDepartamento + "','" + telefono + "','" + usuario + "')")

                db.commit()

                self.aviso("Registro Exitoso", "Visita Registrada")
                self.ui.txtRut.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")

                if (patente != "" and marca != "" and modelo != ""):
                    estacionamiento = self.ui.cboNEstacionamento.currentText()
                    cursor = db.cursor()
                    cursor.execute("select * from visita where rut ='"+x+"'")
                    idVisita = cursor.fetchall()
                    le=(len(idVisita)-1)
                    if  idVisita!=0:
                        idv=str(idVisita[le][0])
                    #ultimo=len(idVisita)-1
                    #idVisita = str(idVisita[ultimo])
                        print (idv)
                        cursor.execute("insert into vehiculovisita (patente,marca,modelo,numeroEstacionamiento,visita) values ('" + patente + "','" + marca + "','" + modelo + "','" + estacionamiento + "','" + idv + "')")
                        db.commit()
                        self.aviso("Registro Exitoso", "Vehiculo Registrado")
                        self.ui.txtPatente.setText("")
                        self.ui.txtMarca.setText("")
                        self.ui.txtModelo.setText("")
            else:
                self.aviso("Error", "Revise Rut")









    def agregarResidente(self):
        rut = self.ui.txtRut.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        edificio = self.ui.cboEdficio.currentText()
        departamento = self.ui.cboDepartamento.currentText()
        telefono = self.ui.txtTelefono.text()

        rut2 = self.validarRut(rut)


        if(rut=="" or nombre =="" or apellido=="" or edificio=="" or departamento=="" or telefono==""):
            self.aviso("Error", "Ingrese todos los datos")
        else:
            if rut2 != False:
                rut2 = str(rut2)

                cursor = db.cursor()
                idDepartamento = cursor.execute("select id from departamento where numero = '" + departamento + "'")
                idDepartamento = cursor.fetchone()
                idDepartamento = str(idDepartamento[0])

                idEdificio = cursor.execute("select id from edificio where nombre = '" + edificio + "'")
                idEdificio = cursor.fetchone()
                idEdificio = str(idEdificio[0])
                sql = cursor.execute("insert into residente (rut,nombre,apellido,edificio,departamento,telefono) values ('" + rut2 + "','" + nombre + "','" + apellido + "','" + idEdificio + "','" + idDepartamento + "','" + telefono + "')")
                db.commit()
                self.aviso("Registro Exitoso", "Residente Registrado")
                self.ui.txtRut.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
            else:
                self.aviso("Error", "Revise Rut")

    def agregarVehiculoResidente(self):
        patente=self.ui.txtPatente.text()
        marca=self.ui.txtMarca.text()
        modelo=self.ui.txtModelo.text()
        estacionamiento=self.ui.cboEstacionamiento.currentText()
        residente=self.ui.txtRut.text()
        if  (patente=="" or marca=="" or modelo=="" or estacionamiento=="" or residente==""):
            self.aviso("Error","Complete todos los campos")
        else:
            cur=db.cursor()
            cur.execute("insert into vehiculoresidente (patente,marca,modelo,numeroEstacionamiento,residente) values ('"+patente+"','"+marca+"','"+modelo+"','"+estacionamiento+"','"+residente+"')")
            db.commit()
            self.aviso("Registro exitoso", "Vehiculo Registrado")
            self.ui.txtPatente.setText("")
            self.ui.txtMarca.setText("")
            self.ui.txtModelo.setText("")
            self.ui.txtRut.setText("")
            self.ui.txtNombre.setText("")

    def buscarDepto(self):
        numero=self.ui.txtNumero.text()
        table=self.ui.tableDepas
        opcion=self.ui.cboBuscar.currentText()
        cur=db.cursor()
        if (opcion=="-Seleccione opcion-"):
            self.aviso("Error","Seleccione una opcion")
        elif (opcion=="Numero"):
            cur.execute(
                "SELECT departamento.*, edificio.nombre,dueño.rut from departamento join edificio on departamento.edificio=edificio.id join dueño on departamento.dueño=dueño.rut where departamento.numero='" + numero + "'")
            data=cur.fetchall()
            while (table.rowCount() > 0):
                table.removeRow(0)
            if  (len(data)!=0):
                for d in data:
                    id=str(d[0])
                    numero=str(d[1])
                    edificio=str(d[4])
                    dueño = str(d[5])
                    rows = table.rowCount()
                    table.insertRow(rows)
                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(numero))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(edificio))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(dueño))

                    cur.execute("select * from residente where departamento ='"+id+"'")
                    data2=cur.fetchall()
                    cantidad=str(len(data2))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(cantidad))
            else:
                self.aviso("Error","No se encontro el numero")
        elif (opcion=="Dueño"):
            if numero=="":
                self.aviso("Error", "Ingrese un Rut")
            else:
                rut2 = self.validarRut(numero)
                if rut2 != False:
                    rut2 = str(rut2)
                    cur.execute("SELECT departamento.*, edificio.nombre,dueño.rut from departamento join edificio on departamento.edificio=edificio.id join dueño on departamento.dueño=dueño.rut where dueño.rut='"+rut2+"'")
                    data = cur.fetchall()
                    while (table.rowCount() > 0):
                        table.removeRow(0)
                    if (len(data) != 0):
                        for d in data:
                            id = str(d[0])
                            numero = str(d[1])
                            edificio = str(d[4])
                            dueño = str(d[5])
                            rows = table.rowCount()
                            table.insertRow(rows)
                            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(numero))
                            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(edificio))
                            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(dueño))

                            cur.execute("select * from residente where departamento ='" + id + "'")
                            data2 = cur.fetchall()
                            cantidad = str(len(data2))
                            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(cantidad))
                    else:
                        self.aviso("Error", "Rut no encontrado")
                else:
                    self.aviso("Error", "Revise Rut")

    def buscarVisita(self):
        buscar=self.ui.txtBuscar.text()
        table = self.ui.tableVisitas
        busqueda=self.ui.cboBuscarV.currentText()
        cur = db.cursor()
        fecha1=self.ui.fecha1.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        fecha2 = self.ui.fecha2.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        print (fecha1,fecha2)
        x=self.validarRut(buscar)
        if  busqueda=="-Seleccione opcion-":
            self.aviso("Error", "Seleccione una opcion")
        else:
            if  (busqueda=="RUT"):
                if x != False:
                    x = str(x)
                    query = "SELECT visita.*, vehiculovisita.patente, edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita join edificio on edificio.id=visita.edificio WHERE visita.rut ='"+x+"'"
                    cur.execute(query)
                    data = cur.fetchall()

                    while (table.rowCount() > 0):
                        table.removeRow(0)
                    if  (len(data)>0):
                        for v in data:
                            rut = str(v[1])
                            nombre = str(v[2])
                            apellido = str(v[3])
                            edificio = str(v[4])
                            departamento = str(v[5])
                            telefono = str(v[6])
                            fecha = str(v[7])
                            usuario=str(v[8])
                            patente = str(v[9])
                            ed = str(v[10])
                            rows = table.rowCount()
                            table.insertRow(rows)

                            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(ed))
                            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
                            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
                            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
                            table.setItem(rows, 7, QtWidgets.QTableWidgetItem(fecha))
                            table.setItem(rows, 8, QtWidgets.QTableWidgetItem(usuario))
                    else:
                        self.aviso("Error", "No se encontro el rut")
                else:
                    self.aviso("Error", "Revise Rut")

            elif busqueda=="Fecha":
                query = "SELECT visita.*, vehiculovisita.patente,edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita join edificio on edificio.id=visita.edificio WHERE visita.fecha between '" + fecha1 + "' and '"+fecha2+"'"
                cur.execute(query)
                data = cur.fetchall()
                while (table.rowCount() > 0):
                    table.removeRow(0)
                if (len(data) > 0):
                    for v in data:
                        rut = str(v[1])
                        nombre = str(v[2])
                        apellido = str(v[3])
                        edificio = str(v[4])
                        departamento = str(v[5])
                        telefono = str(v[6])
                        fecha = str(v[7])
                        patente = str(v[9])
                        usuario = str(v[8])
                        ed = str(v[10])
                        rows = table.rowCount()
                        table.insertRow(rows)

                        table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                        table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                        table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                        table.setItem(rows, 3, QtWidgets.QTableWidgetItem(ed))
                        table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
                        table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
                        table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
                        table.setItem(rows, 7, QtWidgets.QTableWidgetItem(fecha))
                        table.setItem(rows, 8, QtWidgets.QTableWidgetItem(usuario))

            elif busqueda=="RUT y fecha":
                if x != False:
                    x = str(x)
                    query = "SELECT visita.*, vehiculovisita.patente,edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita join edificio on edificio.id=visita.edificio WHERE visita.rut='"+x+"' and visita.fecha between '" + fecha1 + "' and '" + fecha2 + "'"
                    cur.execute(query)
                    data = cur.fetchall()
                    while (table.rowCount() > 0):
                        table.removeRow(0)
                    if (len(data) > 0):
                        for v in data:
                            rut = str(v[1])
                            nombre = str(v[2])
                            apellido = str(v[3])
                            edificio = str(v[4])
                            departamento = str(v[5])
                            telefono = str(v[6])
                            fecha = str(v[7])
                            patente = str(v[9])
                            usuario = str(v[8])
                            ed = str(v[10])
                            rows = table.rowCount()
                            table.insertRow(rows)

                            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(ed))
                            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
                            table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
                            table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
                            table.setItem(rows, 7, QtWidgets.QTableWidgetItem(fecha))
                            table.setItem(rows, 8, QtWidgets.QTableWidgetItem(usuario))
                else:
                    self.aviso("Error", "Revise Rut")
            else:
                self.aviso("Error", "Seleccione una opcion")


    def buscarResidente(self):
        buscar=self.ui.txtBuscar.text()
        table=self.ui.tableResidentes
        rut2 = self.validarRut(buscar)

        cur=db.cursor()
        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("SELECT residente.*, vehiculoresidente.patente from residente left join vehiculoresidente on residente.rut=vehiculoresidente.residente WHERE residente.rut ='"+rut2+"'")
            data=cur.fetchall()
            while (table.rowCount() > 0):
                table.removeRow(0)
            if  (len(data)>0):
                for v in data:
                    rut = str(v[0])
                    nombre = str(v[1])
                    apellido = str(v[2])
                    edificio = str(v[3])
                    departamento = str(v[4])
                    telefono = str(v[5])
                    patente = str(v[6])

                    rows = table.rowCount()
                    table.insertRow(rows)

                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(edificio))
                    table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
                    table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
                    table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
            else:
                self.aviso("Error","Rut no encontrado")
        else:
            self.aviso("Error", "Revise Rut")


    def buscarVehiculo(self):
        buscarpor=self.ui.cboBuscar.currentText()
        if  (buscarpor=='-Buscar por-'):
            self.aviso('Error','Seleccione una opcion')
        elif (buscarpor=="Patente"):
            buscar=self.ui.txtBuscar.text()
            table=self.ui.tableVehiculos
            cur=db.cursor()
            cur.execute("select * from vehiculoresidente where patente ='"+buscar+"'")
            data=cur.fetchall()
            if (len(data)>0):
                while (table.rowCount() > 0):
                    table.removeRow(0)
                for v in data:
                    patente=str(v[0])
                    marca=str(v[1])
                    modelo = str(v[2])
                    estacionamiento = str(v[3])
                    dueño = str(v[4])
                    rows = table.rowCount()
                    table.insertRow(rows)
                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(patente))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(marca))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(modelo))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estacionamiento))
                    table.setItem(rows, 4, QtWidgets.QTableWidgetItem(dueño))
                    table.setItem(rows, 5, QtWidgets.QTableWidgetItem('Residente'))
            else:
                cur.execute("select * from vehiculovisita where patente ='" + buscar + "'")
                data = cur.fetchall()
                if (len(data)>0):
                    while (table.rowCount() > 0):
                        table.removeRow(0)
                    for v in data:
                        patente=str(v[0])
                        marca=str(v[1])
                        modelo = str(v[2])
                        estacionamiento = str(v[3])
                        dueño = str(v[4])
                        rows = table.rowCount()
                        table.insertRow(rows)
                        table.setItem(rows, 0, QtWidgets.QTableWidgetItem(patente))
                        table.setItem(rows, 1, QtWidgets.QTableWidgetItem(marca))
                        table.setItem(rows, 2, QtWidgets.QTableWidgetItem(modelo))
                        table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estacionamiento))
                        table.setItem(rows, 4, QtWidgets.QTableWidgetItem(dueño))
                        table.setItem(rows, 5, QtWidgets.QTableWidgetItem('Visita'))
                else:
                    self.aviso('Error','Patente no encontrada')
                    table.removeRow(0)
        else:
            buscar = self.ui.txtBuscar.text()
            table = self.ui.tableVehiculos
            cur = db.cursor()
            rut2 = self.validarRut(buscar)
            if rut2 != False:
                rut2 = str(rut2)

                cur.execute("select * from vehiculoresidente where residente ='" + rut2 + "'")
                data = cur.fetchall()
                if (len(data) > 0):
                    while (table.rowCount() > 0):
                        table.removeRow(0)
                    for v in data:
                        patente = str(v[0])
                        marca = str(v[1])
                        modelo = str(v[2])
                        estacionamiento = str(v[3])
                        dueño = str(v[4])
                        rows = table.rowCount()
                        table.insertRow(rows)
                        table.setItem(rows, 0, QtWidgets.QTableWidgetItem(patente))
                        table.setItem(rows, 1, QtWidgets.QTableWidgetItem(marca))
                        table.setItem(rows, 2, QtWidgets.QTableWidgetItem(modelo))
                        table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estacionamiento))
                        table.setItem(rows, 4, QtWidgets.QTableWidgetItem(dueño))
                        table.setItem(rows, 5, QtWidgets.QTableWidgetItem('Residente'))
                else:
                    cur.execute("select vehiculovisita.* from vehiculovisita join visita on visita.id=vehiculovisita.visita where visita.rut='" + rut2 + "'")
                    data = cur.fetchall()
                    if (len(data) > 0):
                        while (table.rowCount() > 0):
                            table.removeRow(0)
                        for v in data:
                            patente = str(v[0])
                            marca = str(v[1])
                            modelo = str(v[2])
                            estacionamiento = str(v[3])
                            dueño = str(v[4])
                            rows = table.rowCount()
                            table.insertRow(rows)
                            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(patente))
                            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(marca))
                            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(modelo))
                            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estacionamiento))
                            table.setItem(rows, 4, QtWidgets.QTableWidgetItem(rut2))
                            table.setItem(rows, 5, QtWidgets.QTableWidgetItem('Visita'))
                    else:
                        self.aviso('Error', 'Rut no encontrado')
                        table.removeRow(0)
            else:
                self.aviso('Error', 'Revise Rut')

    def buscarDueno(self):
        rut=self.ui.txtRut.text()
        rut2 = self.validarRut(rut)
        cur = db.cursor()
        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("select * from dueño where rut='"+rut2+"'")
            data=cur.fetchall()
            if (len(data)!=0):
                for d in data:
                    nombre=str(d[1])
                    apellido=str(d[2])
                    telefono=str(d[3])
                    self.ui.txtNombre.setText(nombre)
                    self.ui.txtApellido.setText(apellido)
                    self.ui.txtTelefono.setText(telefono)
            else:
                self.aviso("Error","Rut no encontrado")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
        else:
            self.aviso("Error", "Revise Rut")

    def buscarArrendatario(self):
        rut=self.ui.txtRut.text()
        cur = db.cursor()
        rut2 = self.validarRut(rut)
        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("select * from arrendatario where rut='"+rut2+"'")
            data=cur.fetchall()
            if  (len(data)!=0):
                for d in data:
                    nombre=str(d[1])
                    apellido = str(d[2])
                    telefono = str(d[3])
                    self.ui.txtNombre.setText(nombre)
                    self.ui.txtApellido.setText(apellido)
                    self.ui.txtTelefono.setText(telefono)
            else:
                self.aviso("Error","Rut no encontrado")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
        else:
            self.aviso("Error", "Revise Rut")
    def buscarArrendatariob(self):
        rut=self.ui.txtArrendatario.text()
        table = self.ui.tableDueno
        cur=db.cursor()
        rut2 = self.validarRut(rut)
        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("select * from arrendatario where rut='"+rut2+"'")
            data=cur.fetchall()
            if  (len(data)!=0):
                while (table.rowCount() > 0):
                    table.removeRow(0)
                for d in data:
                    r = str(d[0])
                    nombre = str(d[1])
                    apellido = str(d[2])
                    telefono = str(d[3])
                    rows = table.rowCount()
                    table.insertRow(rows)
                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(r))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(telefono))
            else:
                self.aviso("Error", "Rut no encontrado")
                table.removeRow(0)
        else:
            self.aviso("Error", "Revise Rut")

    def buscarEditarResidente(self):
        rut = self.ui.txtRut.text()
        cursor = db.cursor()
        rut2 = self.validarRut(rut)
        if rut2 != False:
            rut2 = str(rut2)
            cursor.execute("select * from residente where rut = '" + rut2 + "'")
            mysql = cursor.fetchone()

            if (mysql != None):
                nombre = str(mysql[1])
                apellido = str(mysql[2])
                telefono = str(mysql[5])
                print(nombre, apellido, telefono)
                self.ui.txtNombre.setText(nombre)
                self.ui.txtApellido.setText(apellido)
                self.ui.txtTelefono.setText(telefono)
            else:
                self.aviso("Error", "Rut no encontrado")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
        else:
            self.aviso("Error", "Revise Rut")

    def buscarResidenteEst(self):
        rut=self.ui.txtBuscar.text()
        table=self.ui.tableEstacionamiento
        cursor=db.cursor()
        cursor.execute("SELECT residente.*, estacionamientoresidente.* from residente left join estacionamientoresidente on residente.departamento=estacionamientoresidente.departamento WHERE residente.rut='"+rut+"'")
        residente=cursor.fetchall()
        while (table.rowCount() > 0):
            table.removeRow(0)
        self.ui.cboReservar.clear()
        if  (len(residente)>0):
            for res in residente:
                nombre=str(res[1])
                apellido = str(res[2])
                edificio = str(res[3])
                depa=str(res[4])
                estacionamiento=str(res[6])
                r2=str(res[7])
                rows = table.rowCount()
                table.insertRow(rows)


                table.setItem(rows, 0, QtWidgets.QTableWidgetItem(nombre))
                table.setItem(rows, 1, QtWidgets.QTableWidgetItem(apellido))
                table.setItem(rows, 2, QtWidgets.QTableWidgetItem(edificio))
                table.setItem(rows, 3, QtWidgets.QTableWidgetItem(depa))
                table.setItem(rows, 4, QtWidgets.QTableWidgetItem(estacionamiento))
                cursor.execute("select * from estacionamientoresidente where departamento='" + depa + "'")
                x = cursor.fetchall()
                for e in x:
                    res2 = e[1]
                    if res2 != None:
                        table.setItem(rows, 5, QtWidgets.QTableWidgetItem("Reservado"))
                    else:
                        table.setItem(rows, 5, QtWidgets.QTableWidgetItem("No Reservado"))
                        self.ui.cboReservar.addItem(estacionamiento)

        else:
            self.aviso("Error", "No se encontro el rut")

    def reservarEstacionamiento(self):
        rut=self.ui.txtBuscar.text()
        estacionamiento=self.ui.cboReservar.currentText()
        table = self.ui.tableEstacionamiento
        cur = db.cursor()
        if  rut=="":
            self.aviso("Error", "Ingrese un Rut")
        elif estacionamiento=="":
            self.aviso("Error", "No hay estacionamientos")
        else:
            cur.execute("SELECT estacionamientoresidente.residente FROM residente join estacionamientoresidente on estacionamientoresidente.departamento = residente.departamento where rut='"+rut+"'")
            data=cur.fetchall()
            for d in data:
                r2=d[0]
                if  r2==None:
                    cur.execute("update estacionamientoresidente set residente='" + rut + "' where numero='" + estacionamiento + "'")
                    db.commit()
                    self.aviso("Listo", "Estacionamiento Reservado")
                    while (table.rowCount() > 0):
                        table.removeRow(0)
                else:
                    self.aviso("Error", "No se pudo reservar")







    def buscarEliminarResidente(self):
        rut=self.ui.txtBuscar.text()
        table=self.ui.tableResidentes
        cursor = db.cursor()
        rut2 = self.validarRut(rut)
        if rut=="":
            self.aviso("Error", "Ingrese un Rut")
        elif rut2 != False:
            rut2 = str(rut2)
            cursor.execute("SELECT residente.*, vehiculoresidente.patente, edificio.nombre from residente left join vehiculoresidente on residente.rut=vehiculoresidente.residente JOIN  edificio on edificio.id = residente.edificio WHERE residente.rut ='"+rut2+"'")
            data= cursor.fetchall()
            while (table.rowCount() > 0):
                table.removeRow(0)
            if  (len(data)>0):
                for v in data:
                    rut = str(v[0])
                    nombre = str(v[1])
                    apellido = str(v[2])
                    edificio = str(v[3])
                    departamento = str(v[4])
                    telefono = str(v[5])
                    patente = str(v[6])
                    ed = str(v[7])
                    rows = table.rowCount()
                    table.insertRow(rows)

                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(ed))
                    table.setItem(rows, 4, QtWidgets.QTableWidgetItem(departamento))
                    table.setItem(rows, 5, QtWidgets.QTableWidgetItem(telefono))
                    table.setItem(rows, 6, QtWidgets.QTableWidgetItem(patente))
                    table.setItem(rows, 7, QtWidgets.QTableWidgetItem("Eliminar"))
            else:
               self.aviso("Error","Rut no encontrado")
        else:
            self.aviso("Error", "Revise Rut")

    def buscarEditarUsuario(self):
        rut=self.ui.txtRut.text()
        cursor = db.cursor()
        rut2 = self.validarRut(rut)

        if rut2 != False:
            rut2 = str(rut2)
            cursor.execute("select * from usuario where rut='" + rut2 + "'")
            mysql = cursor.fetchone()
            if  (mysql!=None):
                nombre = str(mysql[1])
                apellido = str(mysql[2])
                telefono = str(mysql[3])
                correo = str(mysql[4])
                tipo = str(mysql[6])
                self.ui.txtNombre.setText(nombre)
                self.ui.txtApellido.setText(apellido)
                self.ui.txtTelefono.setText(telefono)
                self.ui.txtCorreo.setText(correo)
                if (tipo=='0'):
                    self.ui.cboTipo.setCurrentText("Guardia")
                else:
                    self.ui.cboTipo.setCurrentText("Administrador")
            else:
                self.aviso("Error", "No se encontro el Rut")
        else:
            self.aviso("Error", "Revise Rut")


    def buscarHabilitarUsuario(self):
        rut=self.ui.txtRut.text()
        table= self.ui.tableUser
        x = self.validarRut(rut)
        if x != False:
            x = str(x)
            print (x)
            cursor=db.cursor()
            cursor.execute("select * from usuario where rut='"+x+"'")
            mysql=cursor.fetchone()
            if  (mysql!=None):
                r = str(mysql[0])
                nombre = str(mysql[1])
                apellido = str(mysql[2])
                estado = str(mysql[7])
                while (table.rowCount() > 0):
                    table.removeRow(0)
                if  (estado=='1'):
                    estado2='Habilitado'
                    self.ui.btnDeshabilitar.setEnabled(True)
                    self.ui.btnHabilitar.setEnabled(False)
                else:
                    estado2 = 'Deshabilitado'
                    self.ui.btnDeshabilitar.setEnabled(False)
                    self.ui.btnHabilitar.setEnabled(True)
                rows = table.rowCount()
                table.insertRow(rows)

                table.setItem(rows, 0, QtWidgets.QTableWidgetItem(r))
                table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estado2))
            else:
                self.aviso("Error", "No se encontro el rut")
        else:
            self.aviso("Error", "Revise el Rut")

    def buscarResidenteAV(self):
        rut=self.ui.txtRut.text()
        cur=db.cursor()
        rut2 = self.validarRut(rut)


        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("select nombre, apellido from residente where rut = '"+rut2+"'")
            data=cur.fetchone()
            if  (data!=None):
                nombre=str(data[0])
                apellido = str(data[1])
                self.ui.txtNombre.setText(nombre+" "+apellido)
                cur.execute("select * from estacionamientoresidente where residente='"+rut2+"'")
                lista=cur.fetchall()
                if (len(lista)>0):
                    for e in lista:
                        self.ui.cboEstacionamiento.addItem(str(e[0]))
                else:
                    self.aviso("Aviso", "Residente sin estacionamientos")
            else:
                self.aviso("Error","Rut no encondrado")
        else:
            self.aviso("Error", "Revise Rut")


    def buscarResidenteEV(self):
        rut = self.ui.txtRut.text()
        table=self.ui.tableVehiculos
        cur = db.cursor()
        rut2 = self.validarRut(rut)
        if  rut=="":
            self.aviso("Error","Ingrese un Rut")
        else:
            if rut2 != False:
                rut2 = str(rut2)

                cur.execute("select nombre, apellido from residente where rut = '" + rut2 + "'")
                data = cur.fetchone()
                if (data != None):
                    nombre = str(data[0])
                    apellido = str(data[1])
                    self.ui.txtNombre.setText(nombre + " " + apellido)
                    cur.execute("select * from vehiculoresidente where residente='" + rut2 + "'")
                    lista = cur.fetchall()
                    if len(lista)>0:
                        while (table.rowCount() > 0):
                            table.removeRow(0)
                        for v in lista:
                            patente=str(v[0])
                            marca = str(v[1])
                            modelo = str(v[2])
                            estacionamiento = str(v[3])

                            rows = table.rowCount()
                            table.insertRow(rows)

                            table.setItem(rows, 0, QtWidgets.QTableWidgetItem(patente))
                            table.setItem(rows, 1, QtWidgets.QTableWidgetItem(marca))
                            table.setItem(rows, 2, QtWidgets.QTableWidgetItem(modelo))
                            table.setItem(rows, 3, QtWidgets.QTableWidgetItem(estacionamiento))
                            table.setItem(rows, 4, QtWidgets.QTableWidgetItem('ELIMINAR'))
                    else:
                        self.aviso("Aviso", "No hay vehiculos")
                else:
                    self.aviso("Error", "Rut no encondrado")
                    self.ui.txtRut.setText("")
                    self.ui.txtNombre.setText("")
            else:
                self.aviso("Error", "Revise Rut")


    def buscarDuenoEl(self):
        edificio=self.ui.cboEdficio.currentText()
        depa=self.ui.cboDepartamento.currentText()
        table=self.ui.tableDueno

        cur=db.cursor()
        e2=cur.execute("select id from edificio where nombre='"+edificio+"'")
        e2=cur.fetchone()
        e2=str(e2[0])
        d2=cur.execute("select departamento.dueño from departamento where numero='"+depa+"' and edificio='"+e2+"'")
        d2=cur.fetchone()
        d2=str(d2[0])
        if  (len(d2)!=None):
            cur.execute("select * from dueño where rut='"+d2+"'")
            lista=cur.fetchall()
            if  (len(lista)>0):
                while(table.rowCount()>0):
                    table.removeRow(0)

                for d in lista:
                    rut = str(d[0])
                    nombre=str(d[1])
                    apellido=str(d[2])
                    telefono=str(d[3])
                    rows = table.rowCount()
                    table.insertRow(rows)
                    table.setItem(rows, 0, QtWidgets.QTableWidgetItem(rut))
                    table.setItem(rows, 1, QtWidgets.QTableWidgetItem(nombre))
                    table.setItem(rows, 2, QtWidgets.QTableWidgetItem(apellido))
                    table.setItem(rows, 3, QtWidgets.QTableWidgetItem(telefono))
            else:
                while (table.rowCount() > 0):
                    table.removeRow(0)
                rows = table.rowCount()
                table.insertRow(rows)
                table.setItem(rows, 0, QtWidgets.QTableWidgetItem("X"))
                table.setItem(rows, 1, QtWidgets.QTableWidgetItem("X"))
                table.setItem(rows, 2, QtWidgets.QTableWidgetItem("X"))
                table.setItem(rows, 3, QtWidgets.QTableWidgetItem("X"))

        else:
            self.aviso("Error", "Dueño no encondrado")

    def eliminarDueno(self):
        edificio = self.ui.cboEdficio.currentText()
        depa = self.ui.cboDepartamento.currentText()
        table = self.ui.tableDueno

        cur = db.cursor()
        e2 = cur.execute("select id from edificio where nombre='" + edificio + "'")
        e2 = cur.fetchone()
        e2 = str(e2[0])
        d2 = cur.execute(
            "select departamento.dueño from departamento where numero='" + depa + "' and edificio='" + e2 + "'")
        d2 = cur.fetchone()
        d2 = str(d2[0])
        if  (len(d2)!=None):
            cur.execute("update departamento set dueño ='Condominio' where numero='"+depa+"' and edificio='"+e2+"'")
            db.commit()
            self.aviso("Listo", "Dueño eliminado")
            table.removeRow(0)
        else:
            self.aviso("Error", "Dueño no encondrado")

    def eliminarArrendatario(self):
        rut=self.ui.txtArrendatario.text()
        table = self.ui.tableDueno
        cur=db.cursor()
        rut2 = self.validarRut(rut)

        if rut2 != False:
            rut2 = str(rut2)
            cur.execute("select * from arrendatario where rut='"+rut2+"'")
            data=cur.fetchall()
            if  (len(data)>0):
                for d in data:
                    rut2=str(d[0])
                    cur.execute("delete from arrendatario where rut='"+rut2+"'")
                    db.commit()
                    self.aviso("Listo", "Arrendatario eliminado")
                    self.ui.txtArrendatario.setText("")
                    table.removeRow(0)
            else:
                self.aviso("Error", "Revise Rut")
        else:
            self.aviso("Error", "Revise Rut")


    def editarDueno(self):
        rut=self.ui.txtRut.text()
        nombre=self.ui.txtNombre.text()
        apellido=self.ui.txtApellido.text()
        telefono=self.ui.txtTelefono.text()
        rut2 = self.validarRut(rut)

        if  (rut=="" or nombre=="" or apellido=="" or telefono==""):
            self.aviso("Error", "Complete todos los campos")
        else:
            cur = db.cursor()
            if rut2 != False:
                rut2 = str(rut2)
                cur.execute("select * from dueño where rut='"+rut2+"'")
                data=cur.fetchone()
                if  (data!= None):
                    cur.execute("update dueño set nombre='"+nombre+"', apellido='"+apellido+"',telefono='"+telefono+"' where rut='"+rut2+"'")
                    db.commit()
                    self.aviso("Listo", "Dueño actualizado")
                    self.ui.txtRut.setText("")
                    self.ui.txtNombre.setText("")
                    self.ui.txtApellido.setText("")
                    self.ui.txtTelefono.setText("")
                else:
                    self.aviso("Error", "Revise Rut")
            else:
                self.aviso("Error", "Revise Rut")

    def editarArrendatario(self):
        rut = self.ui.txtRut.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        telefono = self.ui.txtTelefono.text()
        rut2 = self.validarRut(rut)

        if (rut == "" or nombre == "" or apellido == "" or telefono == ""):
            self.aviso("Error", "Complete todos los campos")
        else:
            if rut2 != False:
                rut2 = str(rut2)
                cur = db.cursor()
                cur.execute("select * from arrendatario where rut='" + rut2+ "'")
                data = cur.fetchone()
                if (data != None):
                    cur.execute(
                        "update arrendatario set nombre='" + nombre + "', apellido='" + apellido + "',telefono='" + telefono + "' where rut='" + rut2 + "'")
                    db.commit()
                    self.aviso("Listo", "Arrendatario actualizado")
                    self.ui.txtRut.setText("")
                    self.ui.txtNombre.setText("")
                    self.ui.txtApellido.setText("")
                    self.ui.txtTelefono.setText("")
                else:
                    self.aviso("Error", "Revise Rut")
            else:
                self.aviso("Error", "Revise Rut")

    def asignarDueno(self):
        nuevo=self.ui.txtNuevoDueno.text()
        edificio = self.ui.cboEdficio.currentText()
        depa = self.ui.cboDepartamento.currentText()
        table = self.ui.tableDueno
        cur = db.cursor()
        rut2 = self.validarRut(nuevo)
        if nuevo=="":
            self.aviso("Error", "Ingrese un Rut")
        else:
            if rut2 != False:
                rut2 = str(rut2)
                cur.execute("select * from dueño where rut='"+rut2+"'")
                due=cur.fetchall()
                if  (len(due)>0):
                    e2 = cur.execute("select id from edificio where nombre='" + edificio + "'")
                    e2 = cur.fetchone()
                    e2 = str(e2[0])
                    d2 = cur.execute("select departamento.dueño from departamento where numero='" + depa + "' and edificio='" + e2 + "'")
                    d2 = cur.fetchone()
                    d2 = str(d2[0])
                    if (len(d2) != None):
                        cur.execute("update departamento set dueño ='"+rut2+"' where numero='" + depa + "' and edificio='" + e2 + "'")
                        db.commit()
                        self.aviso("Listo", "Dueño asignado")
                        self.ui.txtNuevoDueno.setText("")
                        table.removeRow(0)
                    else:
                        self.aviso("Error", "Dueño no encondrado")
                else:
                    self.aviso("Error", "Rut no encondrado")
            else:
                self.aviso("Error", "Revise Rut")

    def editarResidente(self):
        rut=self.ui.txtRut.text()
        nombre=self.ui.txtNombre.text()
        apellido=self.ui.txtApellido.text()
        edificio = self.ui.cboEdficio.currentText()
        departamento = self.ui.cboDepartamento.currentText()
        telefono = self.ui.txtTelefono.text()
        rut2 = self.validarRut(rut)

        if (rut=="" or nombre =="" or apellido=="" or edificio=="" or departamento=="" or telefono==""):
            self.aviso("Error", "Ingrese todos los datos")
        else:
            if rut2 != False:
                rut2 = str(rut2)
                cursor = db.cursor()
                idDepartamento = cursor.execute("select id from departamento where numero = '" + departamento + "'")
                idDepartamento = cursor.fetchone()
                idDepartamento = str(idDepartamento[0])

                idEdificio = cursor.execute("select id from edificio where nombre = '" + edificio + "'")
                idEdificio = cursor.fetchone()
                idEdificio = str(idEdificio[0])
                cursor.execute("update residente set nombre='"+nombre+"', apellido='"+apellido+"',edificio='"+idEdificio+"',departamento='"+idDepartamento+"',telefono='"+telefono+"' where rut='"+rut2+"'")
                db.commit()
                self.aviso("Actualizacion Exitosa", "Residente Actualizado")
                self.ui.txtRut.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
            else:
                self.aviso("Error", "Revise Rut")

    def editarUsuario(self):
        rut = self.ui.txtRut.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        telefono = self.ui.txtTelefono.text()
        correo = self.ui.txtCorreo.text()
        clave = self.ui.txtClave.text()
        tipo = self.ui.cboTipo.currentText()

        rut2 = self.validarRut(rut)
        if rut2 != False:
            rut2 = str(rut2)

            if (rut == "" or nombre == "" or apellido == "" or correo == "" or clave == "" or telefono == "" or tipo == ""):
                self.aviso("Error", "Ingrese todos los datos")
            else:
                cursor=db.cursor()
                cursor.execute("update usuario set nombre='"+nombre+"', apellido='"+apellido+"', telefono='"+telefono+"', correo='"+correo+"', clave='"+clave+"', tipo='"+tipo+"' where rut='"+rut2+"'")
                db.commit()
                self.aviso("Actualizacion Exitosa", "Usuario Actualizado")
                self.ui.txtRut.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")
                self.ui.txtCorreo.setText("")
                self.ui.txtClave.setText("")
                self.ui.cboTipo.setCurrentText("-Seleccione un tipo-")
        else:
            self.aviso("Error", "Revise Rut")




    def agregarUsuario(self):
        rut=self.ui.txtRut.text()
        nombre=self.ui.txtNombre.text()
        apellido=self.ui.txtApellido.text()
        telefono=self.ui.txtTelefono.text()
        correo=self.ui.txtCorreo.text()
        tipo=self.ui.cboTipo.currentText()
        cursor=db.cursor()

        x = self.validarRut(rut)
        if x != False:
            x = str(x)
            cursor.execute("select * from usuario where rut = '" + x + "'")
            user = cursor.fetchone()

            if (rut=="" or nombre =="" or apellido=="" or correo=="" or telefono==""):
                self.aviso("Error", "Ingrese todos los datos")

            elif (user!=None) :
                self.aviso("Error", "Rut ya registrado")
            else:
                if (tipo=="Guardia"):
                    tipo2=str(0)
                    cursor.execute("insert into usuario (rut,nombre,apellido,telefono,correo,clave,tipo,estado) values('"+x+"','"+nombre+"','"+apellido+"','"+telefono+"','"+correo+"','1234','"+tipo2+"','1')")
                    db.commit()
                    self.aviso("Listo", "Usuario registrado")
                    self.ui.txtRut.setText("")
                    self.ui.txtNombre.setText("")
                    self.ui.txtApellido.setText("")
                    self.ui.txtTelefono.setText("")
                    self.ui.txtCorreo.setText("")

                else:
                    tipo2=str(1)
                    cursor.execute("insert into usuario (rut,nombre,apellido,telefono,correo,clave,tipo,estado) values('"+x+"','"+nombre+"','"+apellido+"','"+telefono+"','"+correo+"','1234','"+tipo2+"','1')")
                    db.commit()
                    self.aviso("Listo", "Usuario registrado")
                    self.ui.txtRut.setText("")
                    self.ui.txtNombre.setText("")
                    self.ui.txtApellido.setText("")
                    self.ui.txtTelefono.setText("")
                    self.ui.txtCorreo.setText("")
        else:
            self.aviso("Error", "Revise Rut")



    def agregarDueno(self):
        rut=self.ui.txtRut.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        telefono = self.ui.txtTelefono.text()
        x = self.validarRut(rut)
        if x != False:
            x = str(x)
            cur = db.cursor()
            cur.execute("select * from dueño where rut='" + x + "'")
            dueño = cur.fetchone()
            if (rut == "" or nombre == "" or apellido == "" or telefono == ""):
                self.aviso("Error", "Ingrese todos los datos")
            elif (dueño != None):
                self.aviso("Error", "Rut ya registrado")
            else:
                cur.execute(
                    "insert into dueño (rut,nombre,apellido,telefono) values('" + x + "','" + nombre + "','" + apellido + "','" + telefono + "')")
                db.commit()
                self.aviso("Listo", "Dueño registrado")
                self.ui.txtRut.setText("")
                self.ui.txtNombre.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtTelefono.setText("")

        else:
            self.aviso("Error", "Revise el Rut")



    def agregarArrendatario(self):
        rut = self.ui.txtRut.text()
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        telefono = self.ui.txtTelefono.text()
        edificio=self.ui.cboEdficio.currentText()
        departamento = self.ui.cboDepartamento.currentText()
        cur = db.cursor()
        rut2 = self.validarRut(rut)


        if  (rut=="" or nombre=="" or apellido=="" or telefono==""):
            self.aviso("Error", "Ingrese todos los datos")

        else:
            if rut2 != False:
                rut2 = str(rut2)
                cur.execute("select * from arrendatario where rut='" + rut2 + "'")
                arrendatario = cur.fetchone()
                if arrendatario==None:
                    cur.execute("SELECT * FROM departamento join edificio on edificio.id= departamento.edificio WHERE edificio.nombre='"+edificio+"' and departamento.numero='"+departamento+"'")
                    depa=cur.fetchall()
                    if  (len(depa)>0):
                        for d in depa:
                            id = str(d[0])
                            cur.execute("select * from arrendatario where departamento='"+id+"'")
                            ad=cur.fetchall()
                            if len(ad)>0:
                                self.aviso("Error", "Departamento ya tiene arrendatario")
                            else:
                                cur.execute("insert into arrendatario (rut,nombre,apellido,telefono,departamento) values('"+rut2+"','"+nombre+"','"+apellido+"','"+telefono+"','"+id+"')")
                                db.commit()
                                self.aviso("Listo", "Arrendatario Registrado")
                                self.ui.txtRut.setText("")
                                self.ui.txtNombre.setText("")
                                self.ui.txtApellido.setText("")
                                self.ui.txtTelefono.setText("")
                    else:
                        self.aviso("Error", "Departamento no encontrado")
                else:
                    self.aviso("Error", "Rut ya registrado")
            else:
                self.aviso("Error", "Revise Rut")

    def deshabilitarUsuario(self):
        rut=self.ui.txtRut.text()
        table = self.ui.tableUser
        cursor=db.cursor()
        cursor.execute("UPDATE usuario set estado = 0 where rut='"+rut+"'")
        db.commit()
        self.aviso("Listo", "Usuario Deshabilitado")
        self.ui.txtRut.setText("")
        table.removeRow(0)

    def habilitarUsuario(self):
        rut=self.ui.txtRut.text()
        table=self.ui.tableUser
        cursor=db.cursor()
        cursor.execute("UPDATE usuario set estado = 1 where rut='"+rut+"'")
        db.commit()
        self.aviso("Listo", "Usuario Habilitado")
        self.ui.txtRut.setText("")
        table.removeRow(0)

    def eliminarVehiculoR(self):
        patente=self.ui.txtPatente.text()
        table=self.ui.tableVehiculos
        if  (patente!=""):
            cur=db.cursor()

            cur.execute("select * from vehiculoresidente where patente='"+patente+"'")
            data=cur.fetchall()
            if  (len(data)>0):
                cur.execute("delete from vehiculoresidente where patente='"+patente+"'")
                db.commit()
                self.aviso("Listo", "Vehiculo Eliminado")
                self.ui.txtPatente.setText("")
                table.removeRow(0)
            else:
                self.aviso("Error", "Vehiculo no encontrado")
        else:
            self.aviso("Error", "Ingrese una patente")

    def eliminarResidente(self):
        rut=self.ui.txtBuscar.text()
        table = self.ui.tableResidentes
        rut2 = self.validarRut(rut)

        cur=db.cursor()

        if (rut==""):
            self.aviso("Error", "Ingrese un Rut")
        else:
            if rut2 != False:
                rut2 = str(rut2)
                cur.execute("select * from residente where rut='" + rut2 + "'")
                data = cur.fetchall()

                if  (len(data)>0):
                    cur.execute("DELETE from vehiculoresidente where residente='"+rut2+"'")
                    db.commit()
                    cur.execute("DELETE from estacionamientoresidente where residente='"+rut2+"'")
                    db.commit()
                    cur.execute("DELETE from residente where rut='" + rut2 + "'")
                    db.commit()
                    self.aviso("Listo","Residente Eliminado")
                    table.removeRow(0)
                else:
                    self.aviso("Error","Rut no encontrado")
            else:
                self.aviso("Error", "Revise Rut")



    def llenarCombo(self):
        cursor=db.cursor()
        sql=cursor.execute("select nombre from edificio")
        lista=cursor.fetchall()

        print(lista)
        i = 0
        for i in lista:
            self.ui.cboEdficio.addItem(i[0])

    def llenarCombo2(self):
        edificio = self.ui.cboEdficio.currentText()
        cursor=db.cursor()
        sql=cursor.execute("select departamento.numero from departamento join edificio on edificio.id= departamento.edificio where edificio.nombre = '"+edificio+"' ")
        departamentos=cursor.fetchall()


        self.ui.cboDepartamento.clear()

        for i in departamentos:
            self.ui.cboDepartamento.addItem(str(i[0]))

    def llenarComboEstacionamiento(self):
        cursor=db.cursor()
        sql=cursor.execute("select numero from estacionamientovisita where estado = 0 ")
        disponibles=cursor.fetchall()

        self.ui.cboNEstacionamento.clear()
        for e in disponibles:
            self.ui.cboNEstacionamento.addItem(str(e[0]))

    def llenarComboEstacionamientoR(self):
        rut=self.ui.txtRut.text()
        cursor=db.cursor()
        sql=cursor.execute("select numero from estacionamientoresidente where residente = '"+rut+"' ")
        disponibles=cursor.fetchall()

        self.ui.cboNEstacionamento.clear()
        for e in disponibles:
            self.ui.cboNEstacionamento.addItem(str(e[0]))


    def informe(self):
        seleccion=self.ui.comboBox.currentText()
        doc=self.ui.txtNombre.text()
        import itertools
        from random import randint
        from statistics import mean
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        def grouper(iterable, n):
            args = [iter(iterable)] * n
            return itertools.zip_longest(*args)
        if seleccion=="-Seleccione opcion-":
            self.aviso("Error","Seleccione una opcion de informe")

        elif seleccion=="Visitas":
            try:
                def export_to_pdf(data):
                    if doc=="":
                        c = canvas.Canvas("informe_visitas.pdf", pagesize=A4)
                    else:
                        c = canvas.Canvas(doc+".pdf", pagesize=A4)
                    w, h = A4
                    max_rows_per_page = 45
                    # Margin.
                    x_offset = 25
                    y_offset = 25
                    # Space between rows.
                    padding = 15
                    c.drawImage("logo.png", 50, h - 200, width=50, height=50)

                    xlist = [x + x_offset for x in [0, 80, 200, 300, 345, 470,550]]
                    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]

                    for rows in grouper(data, max_rows_per_page):
                        rows = tuple(filter(bool, rows))
                        c.grid(xlist, ylist[:len(rows) + 1])
                        for y, row in zip(ylist[:-1], rows):
                            for x, cell in zip(xlist, row):
                                c.drawString(x + 2, y - padding + 3, str(cell))
                        c.showPage()

                    c.save()

                datax = [("RUT", "VISITA", "EDIFICIO", "DEPTO", "FECHA","USUARIO")]


                cur = db.cursor()
                cur.execute("SELECT visita.*, vehiculovisita.patente, edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita join edificio on visita.edificio=edificio.id")
                data=cur.fetchall()

                for v in data:
                    rut = str(v[1])
                    nombre = str(v[2])
                    apellido = str(v[3])
                    departamento = str(v[5])
                    telefono = str(v[6])
                    fecha = str(v[7])
                    usuario = str(v[8])
                    patente = str(v[9])
                    ed = str(v[10])
                    datax.append((rut,nombre+" "+apellido,ed,departamento,fecha,usuario))

                export_to_pdf(datax)
                self.aviso("Listo", "Informe generado")

            except:
                self.aviso("Error", "No se pudo generar PDF")
        elif seleccion=="Usuarios":
           # try:
                def export_to_pdf(data):

                    if doc == "":
                        c = canvas.Canvas("informe_usuarios.pdf", pagesize=A4)

                    else:
                        c = canvas.Canvas(doc + ".pdf", pagesize=A4)

                    w, h = A4
                    max_rows_per_page = 45
                    # Margin.
                    x_offset = 25
                    y_offset = 25
                    # Space between rows.
                    padding = 15
                    c.drawImage("logo.png", 50, h - 200, width=50, height=50)

                    xlist = [x + x_offset for x in [0, 80, 200, 400]]
                    ylist = [h - y_offset - i * padding for i in range(max_rows_per_page + 1)]
                    c.drawString(30, h - 400, "Línea")
                    for rows in grouper(data, max_rows_per_page):
                        rows = tuple(filter(bool, rows))
                        c.grid(xlist, ylist[:len(rows) + 1])
                        for y, row in zip(ylist[:-1], rows):
                            for x, cell in zip(xlist, row):
                                c.drawString(x + 2, y - padding + 3, str(cell))
                        c.showPage()

                    c.save()

                datax = [("RUT", "USUARIO", "VISITAS REGISTRADAS")]


                cur = db.cursor()
                cur.execute("select * from usuario")
                data=cur.fetchall()

                for u in data:
                    rut = str(u[0])
                    nombre = str(u[1])
                    apellido = str(u[2])

                    cur.execute("select * from visita where usuario='"+rut+"'")
                    d2=cur.fetchall()
                    cantidad=str(len(d2))


                    datax.append((rut,nombre+" "+apellido,cantidad))
                export_to_pdf(datax)
                self.aviso("Listo","Informe generado")
           # except:
             #   self.aviso("Error", "No se pudo generar PDF")





           # doc=self.ui.txtNombre.text()

        #try:
           # style0 = xlwt.easyxf('font: name Times New Roman, color-index blue, bold on',
    #                   num_format_str='#,##0.00')
            #style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

            #wb = xlwt.Workbook()
            #ws = wb.add_sheet('Hoja reporte')

            #ws.write(0, 0, "Reporte", style0)
           # ws.write(1, 0, datetime.now(), style1)
            #ws.write(2, 0, "Visitas")
           # ws.write(2, 1, "Edificio")
           # ws.write(2, 2, "Departamento")
           # cur=db.cursor()
            #cur.execute("SELECT visita.*, vehiculovisita.patente, edificio.nombre from visita left join vehiculovisita on visita.id=vehiculovisita.visita join edificio on visita.edificio=edificio.id")
           #  cur.execute("select * from visita")
           # data=cur.fetchall()
           # x=len(data)
           #  ws.write(3,0,x)




            #ws.write(2, 2, xlwt.Formula("A3+B3"))

           #  wb.save(doc+'.xls')
            #  self.aviso("Listo","Excel creado")
        #except:
        #    self.aviso("Error","No se pudo generar excel")

    def validarRut(self, rut):
        try:
            rut = rut.upper();
            r2=rut.replace(".", "")
            rut = rut.replace("-", "")
            rut = rut.replace(".", "")
            aux = rut[:-1]
            dv = rut[-1:]

            revertido = map(int, reversed(str(aux)))
            factors = cycle(range(2, 8))
            s = sum(d * f for d, f in zip(revertido, factors))
            res = (-s) % 11

            if str(res) == dv:

                return r2
            elif dv == "K" and res == 10:
                return r2
            else:
                return False
        except:
            return False

if __name__=="__main__":

    app=QtWidgets.QApplication([])
    window=MainWindow()
    window.show()
    app.exec_()
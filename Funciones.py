#funciones
import os
import numpy as np

escenario=np.arange(100).reshape(10,10)

lista_rut=[]
lista_asientos=[]

contador_entradas=[]

precio_plat=120000
precio_gold=80000
precio_silv=50000
cont_plat=0
cont_gold=0
cont_silv=0
cont_total=0




def mostrar_opciones():
    os.system('cls')
    
    print("""MENÚ
    1. Comprar entradas.
    2. Mostrar ubicaciones disponibles.
    3. Ver listado de asistentes.
    4. Mostrar ganancias totales.
    5. Salir""")
    

def validar_opciones():
    while True:
        try:
            opc=int(input("Ingrese una opción: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("Error! El valor ingresado debe ser de 1 a 5.")
        except:
            print("Error! El valor ingresado no es un entero")

def comprar_entradas():
    while True:
        try:
            num_entradas=int(input("Ingrese el numero de entradas a comprar(1-3): "))
            
            if num_entradas in (1,2,3):
                return num_entradas
            else:
                print("Error! El valor ingresado debe ser de 1 a 3.")
        except:
            print("Error! El valor ingresado no es un entero.")

def contar_entradas(num_entradas):
    contador_entradas=contador_entradas+num_entradas

def selec_ub():
    while True:
        try:
            print(escenario)
            asiento=int(input("Ingrese el asiento: "))
            if asiento>=0 and asiento<=19:
                return asiento
            elif asiento>=20 and asiento<=49:

                return asiento
            elif asiento>=50 and asiento<=99:
                return asiento
            else:
                print("Error! El valor ingresado debe ser de 1 a 100.")
        except:
            print("Error! El valor ingresado no es un entero.")

def cont_asiento(asiento):

    if asiento>=0 and asiento<=19:
        cont_plat=cont_plat+1
    elif asiento>=20 and asiento<=49:
        cont_gold=cont_gold+1
    else:
        cont_silv=cont_silv+1 

            

def ub_disp():
    while True:
        try:
            print(escenario)
            resp=int(input("¿Desea volver? 1.Sí 2.No: "))
            if resp==1:
                    break
            elif resp==2:
                    print(lista_rut)
            else:
                    print("Error! El valor ingresado debe ser 1 o 2")
        except:
            print("Error! el valor ingresado no es un entero.")

def validar_rut():
    while True:
        try:
            rut=int(input("ingrese su rut sin puntos ni guion ni dígito verificador: "))
            if rut>=100000 and rut<=9999999:
                return rut
            else:
                print("Error! El valor ingresado debe contener entre 6 y 7 dígitos.")
        except:
            print("Error! el valor ingresado no es un entero.")

def ver_asistentes():
    while True:
        try:
            print(lista_rut)
            resp=int(input("¿Desea volver? 1.Sí 2.No: "))
            if resp==1:
                break
            elif resp==2:
                print(lista_rut)
            else:
                print("Error! El valor ingresado debe ser 1 o 2")
        except:
            print("Error! el valor ingresado no es un entero.")

def mostrar_ganancias():
    while True:
        try:

            acum_plat=precio_plat*cont_plat
            acum_gold=precio_gold*cont_gold
            acum_silv=precio_silv*cont_silv
            cont_total=cont_plat+cont_gold+cont_silv
            acum_total=acum_plat+acum_gold+acum_silv
            print("""Tipo entrada   Cantidad    Total""")
            print("-----------------------------------------")
            print("platinum $",precio_plat , cont_plat , acum_plat )
            print("-----------------------------------------")
            print("Gold $",precio_gold , cont_gold , acum_gold )
            print("-----------------------------------------")
            print("Silver $",precio_silv , cont_silv , acum_silv )
            print("-----------------------------------------")
            print("Total " , cont_total , acum_total )
            
            resp=int(input("¿Desea volver? 1.Sí 2.No: "))
            if resp==1:
                break
            elif resp==2:
                print("""Tipo entrada   Cantidad    Total""")
                print("-----------------------------------------")
                print("platinum $",precio_plat , cont_plat , acum_plat )
                print("-----------------------------------------")
                print("Gold $",precio_gold , cont_gold , acum_gold )
                print("-----------------------------------------")
                print("Silver $",precio_silv , cont_silv , acum_silv )
                print("-----------------------------------------")
                print("Total " , cont_total , acum_total )
            else:
                print("Error! El valor ingresado debe ser 1 o 2")
        except:
            print("Error! el valor ingresado no es un entero.")

def salir():
    while True:
        try:
            sal=int(input("¿Desea salir? 1.Sí 2.No: "))
            if sal==1:
                exit
            elif sal==2:
                break
            else:
                print("Error! El valor ingresado debe ser 1 o 2")
        except:
            print("Error! el valor ingresado no es un entero.")


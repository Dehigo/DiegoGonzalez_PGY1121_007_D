#DiegoGonzalez_PGY1121_007_D

import Funciones as fn

while True:
    try:
        fn.mostrar_opciones()
        opc=fn.validar_opciones()
        if opc==1:
            fn.comprar_entradas()
            fn.contar_entradas()
            fn.cont_asiento()
            fn.selec_ub()
            fn.validar_rut()
            print("La compra se ha realizado con éxito.")
        elif opc==2:
            fn.ub_disp()
        elif opc==3:
            fn.ver_asistentes()
        elif opc==4:
            fn.mostrar_ganancias()
        else:
            fn.salir()
            print("Gracias por la preferencia")
    except:
        print("Error! Ingrese un número entero")



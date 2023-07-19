def cargar_ventas(pack_gigas, semana):
    for i in range(7):
        print("\nDia %s de ventas:\n"%semana[i])
        pack1 = int(input("Ingrese cuantos pack de 1GB se vendio: "))
        pack1 = verificar_entrada(pack1)
        pack_gigas[0].append(pack1)
        
        pack2 = int(input("Ingrese cuantos pack de 2GB se vendio: "))
        pack2 = verificar_entrada(pack2)
        pack_gigas[1].append(pack2)
        
        pack3 = int(input("Ingrese cuantos pack de 3GB se vendio: "))
        pack3 = verificar_entrada(pack3)
        pack_gigas[2].append(pack3)
        
        pack5 = int(input("Ingrese cuantos pack de 5GB se vendio: "))
        pack5 = verificar_entrada(pack5)
        pack_gigas[3].append(pack5)
     
    print("\nFinalizada la carga.")
    continuar()
    mostrar_carga(pack_gigas, semana)
    return pack_gigas       

#----------------------------------------------------------------

def calcular_ganancias(pack_gigas, pack_precios):
    ganancias = 0
    contador = -1
    for i in pack_gigas:
        contador += 1
        for j in i:
            ganancias += j * pack_precios[contador]
           
    print("Las ganancias fueron de %i"%ganancias)
    print("\nSe finalizo el calculo de ganancias.")
    continuar()
    return ganancias

#------------------------------------------------------------

def can_gigas_vendidas(pack_gigas):
    total_gigas = 0
    for i in pack_gigas:
        for j in i:
            total_gigas += j

    print("\nLa cantidad de gigas vendidas fueron: %i"%total_gigas)
    print("Se finalizo el calculo de cant de gigas vendidas.")
    continuar()
    return total_gigas

#------------------------------------------------------------

def cal_promedio_ventas():
    total = can_gigas_vendidas() / 4
    
    print("El promedio de gigas es de: %i"%total)
    print("Se finalizo el promedio de ventas.")
    continuar()
    return total

#-------------------------------------------------------------

def verificar_entrada(venta):
    while venta < 0:
        print("\nERROR: Su eleccion no es valida o a sido 0.")
        venta = int(input("Vuelva a ingresar: "))
        
    return venta

#-------------------------------------------------------------

def mostrar_carga(pack, semana):
    contador = 0
    contador2 = 0
    gigapack = ["1", "2", "3", "5"]
    for i in pack:
        print("\nPack de %s GIGAS"%gigapack[contador])
        contador += 1
        contador2 = 0
        for j in i:
            print("%s: %i"%(semana[contador2], j) )
            contador2 += 1
        
    print("\nSe finalizo la muestra de productos.")
    continuar()

#------------------------------------------------------------- 
        
def continuar():
    input("Presione una tecla para continuar.")

#--------------####### MAIN #######--------------------------#

pack_precios = [315, 555, 965, 1620]
pack_1gb = []
pack_2gb = []
pack_3gb = []
pack_5gb = []
pack_gigas = [pack_1gb, pack_2gb, pack_3gb, pack_5gb]
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

 
###### PAQUETE DE DATOS ########
#   1GB -> $315  -> IND( 0 )    #
#   2GB -> $555  -> IND( 1 )    #
#   3GB -> $965  -> IND( 2 )    #
#   5GB -> $1620 -> IND( 3 )    #
#-------------------------------#

decision = ""

while decision != "salir":
    print("\n----MENU----\n")
    print("( 1 ) Para cargar ventas")
    print("( 2 ) Para calcular ganancias")
    print("( 3 ) Para calcular gigas vendidas")
    print("( 4 ) Para calcular promedio de ventas")
    print("( 5 ) Para salir\n")
    decision = input("Seleccione una opcion: ")
    
    if decision == "1":
        pack_gigas = cargar_ventas(pack_gigas, semana)
        
    elif decision == "2":
        ganancias = calcular_ganancias(pack_gigas, pack_precios)
        
    elif decision == "3":
        gigas_vendidas = can_gigas_vendidas(pack_gigas)
        
    elif decision == "4":
        promedio = cal_promedio_ventas()
    
    elif decision == "5":
        pass
    
    else:
        input("ERROR: Esa opcion no es correcta vuelva a ingresar.")
        continuar()
    




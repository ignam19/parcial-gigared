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
     

    return pack_gigas       

#----------------------------------------------------------------

def calcular_ganancias(pack_gigas, pack_precios):
    ganancias = 0
    contador = -1
    for i in pack_gigas:
        contador += 1
        for j in i:
            ganancias += j * pack_precios[contador]
           
    
    return ganancias

#------------------------------------------------------------

def can_gigas_vendidas(pack_gigas):
    gigas = [1, 2, 3, 5]
    total_gigas = 0
    for i in range(4):
        for j in range(7):
            total_gigas += pack_gigas[i][j] * gigas[i]

    return total_gigas

#------------------------------------------------------------

def cal_promedio_ventas(pack_gigas):
    total = can_gigas_vendidas(pack_gigas) / 4
    
    return total

#-------------------------------------------------------------

def verificar_entrada(venta):
    while venta < 0:
        print("\nERROR: Su eleccion no es valida o a sido 0.")
        venta = int(input("Vuelva a ingresar: "))
        
    return venta

#-------------------------------------------------------------

def mostrar_carga(pack, semana):
    gigapack = ["1", "2", "3", "5"]
    for i in range(4):
        print("\nPack de %s GIGAS"%gigapack[i])
        for j in range(7):
            print("%s: %i"%(semana[j], pack[i][j]) )
           
        
    print("\nSe finalizo la muestra de productos.")
   
#------------------------------------------------------------- 
        
def continuar():
    input("Presione una tecla para continuar.\n")

#------------------------------------------------------------

def gan_sem(pack_gigas, precios):
    gigas = ["1", "2", "3", "5"]
    ganancia_sem_pack = [0, 0, 0, 0]
    #-----------------
    # IND 0 = PACK 1GB
    # IND 1 = PACK 2GB
    # IND 2 = PACK 3GB
    # IND 3 = PACK 5GB
    #-----------------
    for i in range(4):
        for j in range(7):
            ganancia_sem_pack[i] += pack_gigas[i][j] * precios[i]
            
    
    
    
    for i in range(4):
        print("La ganancia semanal del pack de %s GIGAS fue de %i"%(gigas[i], ganancia_sem_pack[i]))
   
    continuar()
    return ganancia_sem_pack
            
#------------------------------------------------------------

def gigas_xpack(pack_gigas):
    gigas = ["1", "2", "3", "5"]
    venta_xpack = [0,0,0,0]
    #-----------------
    # IND 0 = PACK 1GB
    # IND 1 = PACK 2GB
    # IND 2 = PACK 3GB
    # IND 3 = PACK 5GB
    #-----------------
    for i in range(4):
        for j in range(7):
            venta_xpack[i] += pack_gigas[i][j] * int(gigas[i])
        
    
    
    for i in range(4):
        print("La cantidad de gigas vendida del pack %s GIGAS fue de: %i "%(gigas[i], venta_xpack[i]))
   
    continuar()
    return venta_xpack
  
#------------------------------------------------------------

def promedio_xpack(pack):
    promedios = [0,0,0,0]
    gigas = [1, 2, 3, 5]
    
    for i in range(4):
        promedios[i] += (pack[i] / gigas[i]) / 7
    
    for i in range(4):
        print("El promedio de gigas vendida del pack %s GIGAS fue de: %.2f "%(str(gigas[i]), promedios[i]))
            
    continuar()
    return promedios
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
        mostrar_carga(pack_gigas, semana)
        
    elif decision == "2":
        ganancias = calcular_ganancias(pack_gigas, pack_precios)
        print("Las ganancias fueron de %i"%ganancias)
        
    elif decision == "3":
        gigas_vendidas = can_gigas_vendidas(pack_gigas)
        print("\nLa cantidad de gigas vendidas fueron: %i"%gigas_vendidas)
        
    elif decision == "4":
        promedio = cal_promedio_ventas(pack_gigas)
        print("El promedio de gigas es de: %i"%promedio)
    
    elif decision == "5":
        decision = "salir"
    
    else:
        input("ERROR: Esa opcion no es correcta vuelva a ingresar.")
    
    print("Se acaba de finalizar el proceso.")    
    continuar()


ganancia_semanal = gan_sem(pack_gigas, pack_precios)

cant_gigas_xpack = gigas_xpack(pack_gigas)

promedio_ventas_xpack = promedio_xpack(cant_gigas_xpack)
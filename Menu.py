#encoding: utf-8
#Autor: Pablo Alejandro Sánchez Tadeo, A01377515
#Menu que selecciona entre recolectar insectos y numero mayor

#Funcion para encontar el numero mayor de un grupo de numeros
def encontrarMayor() :
    n = 1
    numMayor = -1
    while n != -1 :
        n = int( input("Ingresa un numero mayor a -1"))
        if numMayor < n :
            numMayor = n
    
    if numMayor != -1 :        
        print("El mayor es:",numMayor)
    else :
        print("No hay datos para encontrar el valor mayor")

#Funcion para calcular el tiempo que se tarda alguien en recolectar 30 insectos
def recoleccionDeInsectos() :
    insectos = int( input("insectos recolectados hoy"))
    dia = 1
    total = insectos
    print("Despues de ",dia," dia(s), has recolectado ",total," insectos")
    
    if total <= 30 :
        print("Te hace falta recolectar ",30-total," insectos")
    
    while total < 30 :
        dia = dia + 1
        insectos = int( input("insectos recolectados hoy"))
        total = total +insectos      
        print("Despues de ",dia," dia(s), has recolectado ",total," insectos")
        if total <= 30 :
            print("Te hace falta recolectar ",30-total," insectos")
        
    if total > 30 :
        print("Te has pasado con ",total-30," insectos")
        
    print("Felicidades, has llegado a la meta")

#Funcion principal
def main () :
    opcion = int( input(" 1. Encontrar mayor \n 2. Recoleccion de insectos \n 3. Salir"))
    while opcion != 3 :
        if opcion == 1 :
            encontrarMayor() 
        elif opcion == 2 :
            recoleccionDeInsectos() 
        elif opcion != 3 :
            print("Esa opcion no está disponible, ingresa otra")
        
        opcion = int( input(" 1. Encontrar mayor \n 2. Recoleccion de insectos \n 3. Salir"))
    
main()
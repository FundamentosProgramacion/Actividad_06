#encoding: UTF-8
#David Salvador Ruiz Roa
#Tarea 6

def mayor():
    n=0
    mayor = 0
    while n != -1:
        numero = int(input("Ingrese un numero (-1 para salir)"))
        n = numero
        if n>mayor:
            mayor = n
            print("el numero mayor es:",mayor)
        else:
            print("el numero mayor es:",mayor)
    main()
    
def insecto():
    insecto = int(input("Ingrese el numero de insectos recolectados hoy (-1 para salir)"))
    dia = 0
    while insecto <= 29:
        dia+=1
        print("Despues de",dia,"dia(s)")
        print("Has acumulado",insecto,"insecto(s)")
        print("Te hacen falta",30-insecto,"insecto(s)")
        insectos = int(input("Ingrese el numero de insectos recolectados hoy"))
        insecto+=insectos
    print ('Felicidades Has terminado la colección')
    main()
    
def main():
    opcion = int(input("1. Mayor\n2. Insectos\n3. Salir\n4. Digite un número\n"))
    while opcion != 3 :
        if opcion == 1:
            mayor()
        elif opcion ==2:
            insecto()
        else:
            a=1
    print("terminado")        
main()
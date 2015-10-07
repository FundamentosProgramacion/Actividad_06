#Encoding:UTF-8
#Autor: Paola Castillo Nacif
#Menu entre la funcion insectos y la funcion calcular mayor

def calcularMayor():
    mayor=0
    numero=0
    while numero!=-1:
        numero=int(input("Inserte numero"))
        n=numero
        if n>mayor:
            mayor=n
    if mayor==0:
        print("No hay datos para encontrar el mayor valor")
    else:
        print("El mayor es:",mayor)
        
def calcInsectos():
    insectos=int(input("Insectos recolectados hoy"))
    dias=1
    numeroIns=insectos
    numeroInsFaltantes=30-numeroIns
    numeroInsRestantes=numeroIns-30
    print("Despues de",dias,"dia(s) de recoleccion has acumulado",numeroIns,"insectos")
    if numeroIns<=30:
        print("Te hace falta recolectar",numeroInsFaltantes,"insectos")
        
    while numeroIns<30:
        dias=dias+1
        insectos=int(input("Insectos recolectados hoy"))
        numeroIns=numeroIns+insectos
        numeroInsFaltantes=30-numeroIns
        numeroInsRestantes=numeroIns-30
        print("Despues de",dias,"dia(s) de recoleccion has acumulado",numeroIns,"insectos")
        if numeroIns<=30:
            print("Te hace falta recolectar",numeroInsFaltantes,"insectos")
    if numeroIns==30:
        print("Felicidades, haz llegado a la meta")
    if numeroIns>30:
        print("Te has pasado con",numeroInsRestantes,"insectos.\nFelicidades, haz llegado a la meta")
        

def main():
    opcion=int(input("1.Encontrar Mayor\n2.Recolectar Insectos\n3.Salir\nTeclea tu opcion"))
    while opcion!=3:
        if opcion==1:
            #funcion numeros
            calcularMayor()
        elif opcion==2:
            #funcion insectos
            calcInsectos()
        else:
            print("Opcion incorrecta, intenta nuevamente")
        opcion=int(input("1.Encontrar Mayor\n2.RecolectarInsectos\n3.Salir\nTeclea tu opcion"))
main()
        
     
        
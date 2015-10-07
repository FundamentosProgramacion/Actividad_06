#Encoding:UTF-8
#Autor: Paola Castillo Nacif
#Descripcion: Insectos, dias

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
        print("Te has pasado con",numeroInsRestantes,"insectos.\nFelicidades, has llegado ala meta")
   
def main():
    calcInsectos()
main()
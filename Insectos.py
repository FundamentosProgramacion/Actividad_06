#encoding: UTF-8
#Autor: Hector Manuel Takami Flores
#Calcula insectos recolectados


def calculaInsectos():
    dias=0
    insectos=0
    insectosAtrapados=0
    insectosFaltantes=0
    insectosSobrantes=0
    insectos=int(input("Insectos recolectados hoy"))
    insectosAtrapados=insectosAtrapados+insectos
    insectosFaltantes=30-insectosAtrapados
    insectosSobrantes=insectosAtrapados-30
    while insectosFaltantes<30:
        dias=dias+1
        if insectosAtrapados<30:
           insectosFaltantes=30-insectosAtrapados
           print("Despues de",dias,"dias(s) de recoleccion has acumulado",insectosAtrapados,"insectos")
           print("Te hacen falta recolectar",insectosFaltantes,"insectos")
           insectos=int(input("Insectos recolectados hoy"))
           insectosAtrapados=insectosAtrapados+insectos
           
        elif insectosAtrapados==30:
            insectosFaltantes=30-insectosAtrapados
            print("Despues de",dias,"dia(s) de recoleccion has acumulado",insectosAtrapados,"insectos")
            print("Te hacen falta recolectar 0 insectos")
            print("Felicidades has llegado a la meta")
            insectosFaltantes=700
                                   
        elif insectosAtrapados>30:
            insectosSobrantes=insectosAtrapados-30
            print("Despues de",dias,"dia(s) de recoleccion has acumulado",insectosAtrapados,"insectos")
            print("Te has pasado con",insectosSobrantes,"insectos")
            print("Felicidades has llegado a la meta")
            insectosFaltantes=700
                       
        else:
            print("")
            
    
    
        
        
def main():
    calculaInsectos()
main()
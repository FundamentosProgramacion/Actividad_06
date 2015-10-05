#encoding:UTF-8
#Autor:Hector Manuel Takami Flores
#Menu para seleccionar funcion 

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
    opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))

            
            
def calculaElMayor():
    mayor=0
    numero=0
    while numero!=-1:
          numero=int(input("Numero"))
          print(numero)
          if numero>mayor:
            mayor=numero
            
          elif numero<0:
            print("No hay datos para encontrar el valor mayor")
            numero=-1
            
            print("")
    if mayor==0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es:",mayor)           
    opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))
         
          
def main():
    opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))
    while opcion!=3:
        if opcion==1:
           calculaElMayor()
        elif opcion==2:
             calculaInsectos()
        elif opcion==3:
             opcion=3
        else:
            print(" Error\n Profavor, intenta nuevamente")
            opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))            
main()            
                       
            
           
        
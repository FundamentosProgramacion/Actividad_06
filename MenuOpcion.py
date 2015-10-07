#encoding:UTF-8
#Autor:Mauricio Medrano, A01272273
#Menu para seleccionar funcion 

def insectosRecolectados():
    d=0
    insectos=0
    insectosRecolectados=0
    insectosQFaltan=0
    insectosQSobran=0
    insectos=int(input("Insectos recolectados hoy"))
    insectosRecolectados=insectosRecolectados+insectos
    insectosQFaltan=30-insectosRecolectados
    insectosQSobran=insectosRecolectados-30
    while insectosQFaltan<30:
        d = d+1
        if insectosRecolectados<30:
           insectosQFaltan=30-insectosAtrapados
           print("Despues de",d,"dias(s) de recoleccion has acumulado",insectosRecolectados,"insectos")
           print("Te hacen falta recolectar",insectosQFaltan,"insectos")
           insectos=int(input("Insectos recolectados hoy"))
           insectosRecolectados=insectosRecolectados+insectos
                      
        elif insectosAtrapados==30:
            insectosQFaltan=30-insectosRecolectados
            print("Despues de",d,"dia(s) de recoleccion has acumulado",insectosRecolectados,"insectos")
            print("Te hacen falta recolectar 0 insectos")
            print("Felicidades has llegado a la meta")
            insectosFaltantes=31
                                   
        elif insectosAtrapados>30:
            insectosQSobran=insectosRecolectados-30
            print("Despues de",d,"dia(s) de recoleccion has acumulado",insectosRecolectados,"insectos")
            print("Te has pasado con",insectosQSobran,"insectos")
            print("Felicidades has llegado a la meta")
            insectosQFaltan=31
                       
        else : 
            opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))

            
            
def ElMayor():
    m=0
    n=0
    while n!=-1:
          n=int(input("Numero"))
          
          if n>m:
           m=n
            
          elif n<0:
            print("No hay datos para encontrar el valor mayor")
            n=-1
            
            print("")
    if m==0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es:",m)           
    opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))
         
          
+def main():
    opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))
    while opcion!=3:
        if opcion==1:
            ElMayor()
        elif opcion==2:
             insectosRecolectados()
        elif opcion==3:
             opcion=3
        else:
           opcion=int(input("1.Encontar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opcion:"))            
main()            
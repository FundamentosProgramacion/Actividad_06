# encoding: UTF-8   
#Autor: Erenssto Cruz López A01169052   
# Uso de while para saber numero de insectos y el numero mayor que tecela un usuario.

    

def main ():
    opcion = int(input("\n1.Encontrar mayor\n2.Recolectar insectos\n3.Salir,\nTecla tu opcion"))
    while opcion!=3:
        if opcion==1:
           h=-1
           num=0
           while num!=-1:
                 num=int(input("\nTeclea un valor entero positivo\nPara terminar teclea -1"))
                 if num>h:
                    h=num
           if h==-1:
              print("No hay datos para encontrar el valor mayor")
              break
           else:
              print("El numero mayor es",h)
              break
        
        elif opcion==2:
             ins=0
             ins2=0
             day=0
             faltantes=30
             
    
             while ins2!=30:
                   
                   ins=int(input("Insectos recolectados hoy"))
                  
                   if ins<=30:
                      ins2=ins2+ins
                      day=day+1
                      faltantes=faltantes-ins
                      print("Despues de",day,"dia(s) de recoleccin has acomulado",ins2,"insectos\nTe hace falta recolectar",faltantes)
                      if faltantes==0:
                         print("Felicidades has llegado a la meta")
                         if  ins==30:   
                            break
                   elif ins>30:    
                        ins2=ins2+ins
                        day=day+1
                        faltantes=ins-faltantes
                        print("Despues de",day,"dia(s) de recoleccin has acomulado",ins2,"insectos\nTe te has pasado con",faltantes,"\nFelicidades has llegado a la meta")
                        if ins>30:
                           break  
main()
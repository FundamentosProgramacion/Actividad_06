#Encoding: UTF-8
#Autor: Manuel Zavala Gmez
#Actividad 6

def encontrarMayor(num,lista):
    print("El numero ms alto es: ", max(lista))
    
def recolectarInsectos(dia,insectos,acumlador):
    while acumlador<30:
        insectos=int(input("Numero de insectos recolectados de hoy"))
        if insectos<=30:
            dia=dia+1
            acumlador=insectos+acumlador
            oper=30-acumlador
            print("Despues %.0f da(s)de recoleccion has recolectado %.0f insectos"%(dia,acumlador))
            print("Te hace falta recolectar %.0f insectos"% oper)
        elif acumlador==30:
            print("Felicidades, has llegado a la meta")
        elif insectos==30:
            print("Felicidades, has llegado a la meta")
    
    

def main():
    opcion=int(input("1.Encontrar Mayor\n2.Recolectar insectos \n3.Salir"))
    while opcion!=3:
        if opcion==1:
            lista=[]
            num=int(input("Teclea tu nmero"))
            while num!=-1:
                print(num)
                num=int(input("Teclea otro número"))
                lista.append(num)
            encontrarMayor(num,lista)    
            
            
            
        elif opcion==2:
            dia=0
            acumlador=0
            insectos=0
    
            recolectarInsectos(dia,insectos,acumlador)
                  
            
            
        else:
            print("Opcion incorrecta, intenta nuevamente")
        opcion=int(input("1.Encontrar Mayor\n2.Recolectar insectos \n3.Salir"))
            
    
main()
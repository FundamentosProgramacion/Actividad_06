#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso
#Insectos

def contarInsectos():
    insectos=0
    dias=0
    restantes=1
    while(restantes>0):
        insectos+=int(input("¿Cuantos insectos recolectaste hoy"))
        dias+=1
        restantes=30-insectos
        print("Despues de %i dias(s) de recoleccion has acumulado %i insectos"%(dias,insectos))
        if(restantes>=0):
            print("Te hace falta recolectar %i insectos"%restantes)
    if(restantes<0):
        print("Te has pasado con %i insectos"%(-1*restantes))
    print("Felicidades has llegado a la meta")
    
    
def main():
    contarInsectos()
main()





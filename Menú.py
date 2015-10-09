#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso
#Menu

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
    
    
def calcularMayor():
    n=0
    h=0
    while n!=-1:
        n=int(input("Numero(para terminar colocar -1)"))
        print(n)
        if n>h:
            h=n
    if h==0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es",h)
        
        
def encontrarMayor():
    calcularMayor()
    
def recolectarInsectos():
    contarInsectos()
    
    
def main():
    a=0
    while a!=3:
        a=int(input("""1.Encontrar Mayor
2.Recolectar insectos
3.Salir
Teclea tu opcion"""))
        if a==1:
            encontrarMayor()
        elif a==2:
            recolectarInsectos()

main()





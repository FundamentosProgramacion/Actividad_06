#encoding:UTF-8
#Jorge Daniel Jurez Ruiz
#Numeros enteros

def contarInsectos():
    i=0
    d=0
    while i<30:
        h=int(input("Insectos recolectados hoy"))
        i=i+h
        d=d+1
        ir=30-i
        print("Despues de",d,"día(s) de recolección has acumulado",i,"insectos")
        if i<=30:
            print("Te falta recolectar",ir,"insectos")
        if i>=30:
            p=i-30
            if p!=0:
                print("Te has pasado por",p,"insectos")
            print("Felicidades has llegado a la meta")

def calcularMayor():
    n=0
    h=0
    while n!=-1:
        n=int(input("Numero"))
        print (n)
        g=n
        if g>h:
            h=g
    if h==0:
        print("No hay datos para encontar el valor mayor")
    else:
        print ("El mayor es",h)
            
def encontrarMayor():
    calcularMayor()    

def recolectarInsectos():
    contarInsectos()


def main():
    a=0
    while a!=3:
        a=int(input("""1.Encontrar mayor
2.Recolectar insectos
3.Salir
Tecle su opción"""))
        if a==1:
            encontrarMayor()
        elif a==2:
            recolectarInsectos()
            
main()
        
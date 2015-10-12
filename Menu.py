# encoding: UTF-8
# Autor: Humberto Serra Mendieta
# Menu de programas

def calcularInsec():
    insectos=int(input("Cuantos insectos recolectaste hoy"))
    dias=1
    while insectos<30:
        faltainsec=30-insectos
        print("Despues de %i dia(s) de recoleccion, has acumulado %i insectos"%(dias,insectos))
        print("Te hace falta recolectar %i insectos"%faltainsec)
        dias=dias+1
        insectos=insectos+(int(input("Cuantos insectos recolectaste hoy")))

    if insectos==30:
        print("Despues de %i dia(s) de recoleccion, has acumulado %i insectos"%(dias,insectos))   
        print("Te hace falta recolectar 0 insectos")
        print("Felicidades has llegado a la meta")      
    elif insectos>30:
        sobrainsec=insectos-30
        print("Despues de %i dia(s) de recoleccion, has acumulado %i insectos"%(dias,insectos))   
        print("Te has pasado con %i insectos"%sobrainsec)
        print("Felicidades has llegado a la meta") 
def calcularMayor():
    numero=0
    mayor=0
    print("Datos de entrada")
    while numero!=-1:
        numero=int(input("Inserte numero"))
        print(numero)
        if numero>mayor:
            mayor=numero
    if mayor==0:
        print("No hay datos de entrada")
    else:
        print("el mayor es",mayor)
        
def main():
    opcion=0
    while opcion!=3:
        opcion=int(input("""1. Encontrar mayor
        2. Recolectar insectos
        3. Salir
        Teclee su opcion"""))
        if opcion==1:
           calcularMayor()
        elif opcion==2:
            calcularInsec()
            
main()
            
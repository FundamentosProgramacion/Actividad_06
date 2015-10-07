#encoding: UTF-8
#Autor: Pablo Alejandro Sanchez Tadeo, A01377515
#Contador de insectos

def main() :
    insectos = int( input("insectos recolectados hoy"))
    dia = 1
    total = insectos
    print("Despues de ",dia," dia(s), has recolectado ",total," insectos")
    
    if total <= 30 :
        print("Te hace falta recolectar ",30-total," insectos")
    
    while total < 30 :
        dia = dia + 1
        insectos = int( input("insectos recolectados hoy"))
        total = total +insectos      
        print("Despues de ",dia," dia(s), has recolectado ",total," insectos")
        if total <= 30 :
            print("Te hace falta recolectar ",30-total," insectos")
        
    if total > 30 :
        print("Te has pasado con ",total-30," insectos")
        
    print("Felicidades, has llegado a la meta")
        
main()
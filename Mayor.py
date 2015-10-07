#Encoding:UTF-8
#Autor:Paola Castillo Nacif
#El programa encontrara el mayor numero y terminara cuando el usuario introduzca -1

def calcularMayor():
    mayor=0
    numero=0
    while numero!=-1:
        numero=int(input("Inserte numero"))
        n=numero
        if n>mayor:
            mayor=n
        
    if mayor==0:
        print("No hay datos para encontrar el mayor valor")
    else:
        print("El mayor es:",mayor) 

def main():
    calcularMayor()
main()
    
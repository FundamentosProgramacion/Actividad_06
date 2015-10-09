#Encoding: UTF-8
#Autor: Abraham Gandaria Alonso
#Mayor

def main ():
    n=1
    numMayor= -1
    while n !=-1:
        n=int(input("Ingresa un numero mayor a -1"))
        if numMayor<n:
            numMayor=n
            
    if numMayor !=-1:
        print("El mayor es:", numMayor)
        
    else:
        print("No hay datos para encontrar el valor mayor")
        
        
        
main()
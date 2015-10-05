#encoding: UTF-8
#Autor:Hector Manuel Takami Flores
#Calcula el numero mayor


def calculaElMayor():
    mayor=0
    numero=0
    while numero!=-1:
          numero=int(input("Numero"))
          print(numero)
          if numero>mayor:
            mayor=numero
          elif numero<0:
            print("No hay datos para encontrar el valor mayor")
            numero=-1
          else:
            print("")
    if mayor==0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es:",mayor)
        
        
def main():         
    calculaElMayor()            
main()         
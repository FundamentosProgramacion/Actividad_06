#encoding: UTF-8
#Autor:Hector Mauricio Medrano, A01272273
#Calcula el numero mayor


def main():
    m=0
    n=0
    while n!=-1:
          numero=int(input("Numero"))
          
          if n>m:
            m=n
          elif n<0:
            print("No hay datos para encontrar el valor mayor")
            numero=-1
         elif m==0:
        print("No hay datos para encontrar el valor mayor")
    else:
        print("El mayor es:",m)
main()          

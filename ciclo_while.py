#encoding: UTF-8
#Autor: Brian Saggiante, A01377511
#Ciclos While

def contarInsectos():
   ins=0
   dia=0
   while ins<30:
       hoy=int(input('Insectos recolectados hoy'))
       ins=ins+hoy
       dia=dia+1
       ir=30-ins
       print('Despues de',dia,'dias de recoleccion has acumulado',ins,'insectos')
       if ins<=30:
          print('Te falta recolectar',ir,'insectos')
       if ins>=30:
           falt=ins-30
           if falt!=0:
               print('Te has pasado por',falt,'insectos')
           print('Felicidades has llegado a la meta')

def calcularMayor():
    num=0
    may=0
    while num!=-1:
        num=int(input('Teclea numero'))
        print(num)
        n=num
        if n>may:
            may=n
    if may==0:
        print('No hay datos para encontar el valor mayor')
    else:
        print ('El numero mayor es',may)
            
def encontrarMayor():
    calcularMayor()    

def recolectarInsectos():
    contarInsectos()


def main():
    m=0
    while m!=3:
        m=int(input('''1.Recolectar Insectos
2.Encontrar Mayor
3.Salir
    Tecle su opcion'''))
        if m==1:
            recolectarInsectos()
        elif m==2:
            encontrarMayor()          
main()
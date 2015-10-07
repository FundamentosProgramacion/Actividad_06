# encoding UTF-8
# Autor: Mauricio Medrano, A01272273 
# Calculando reooleccion de insectos 

def main ():
    d = 0 # Dias de recoleccion 
    insectos = 0
    insectosRecolectados = 0 
    insectosQFaltan = 0 
    insectosQSobran = 0 
    insectos = int(input("Cuantos insectos recolectaste hoy?"))
    insectosRecolectados=insectosRecolectados+insectos
    insectosQFaltan=30-insectosRecolectados
    insectosQSobran=insectosRecolectados-30
    while insectosQFaltan <= 30: 
         d = d + 1 
         if insectosRecolectados < 30: 
            insectosQFaltan = 30 - insectosRecolectados
            print ( "Despues de", d, "dia(s) de recoleccion has acumulado",insectosRecolectados,"insectos")
            print ( "Te hacen faltan recolectar", insectosQFaltan, "insectos") 
            insectos = int ( input ("Cuantos insectos recolectaste hoy?"))
            insectosRecolectados=insectosRecolectados+insectos
            
         
         elif insectosRecolectados==30: 
            insectosQFaltan = 0 
            print ( "Despues de", d, "dia(s) de recoleccion has acumulado", insectosRecolectados,"insectos")
            print ("Te hacen falta recolecta", insectosQFaltan, "insectos") 
            print ("Felicidades has llegado a la meta")
            insectosQFaltan = 31
            
         elif insectosRecolectados > 30: 
            insectosQSobran = insectosRecolectados - 30 
            print ("Despues de", d, "dia(s) de recoleccion has acumulado", insectosRecolectados, "insectos") 
            print ("Te has pasado por", insectosQSobran, "insectos") 
            print ("Felicidades has llegado a la meta") 
            insectosQFaltan = 31
         
              
main()
# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Registra el numero de insectos recolectados al pasar los días y cuántos faltan.

def recolectarInsectos ():  #Registra todos los insectos recolectados
        insectos = 0
        dias = 0
        restantes = 1
        while (restantes > 0):
                insectos += int (input ("¿Cuantos insectos recolectaste hoy?"))
                dias += 1
                restantes = 30 - insectos
                print ("Despues de %i dia(s) de recoleccion has acumulado %i insectos." % (dias, insectos))
                if (restantes >= 0): 
                        print ("Te hace falta recolectar %i insectos." % restantes)
        if (restantes < 0):
                print ("Te has pasado con %i insectos." % (-1*restantes))
        print ("Felicidades has llegado a la meta.")


def main ():
        recolectarInsectos ()

main ()

# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Crea un menu para hacerl elprograma del numero mayor o de la recoleccion de insectos.

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


def obtenerMayor ():  #Obtiene el numero mayor
	n1 = int (input ("Teclea un numero entero positivo"))
	mayor = -1
	while (n1 != -1):
		if (n1>=mayor):
			mayor = n1
		n1 = int (input ("Teclea un numero entero positivo"))
	if (mayor == -1):
		print ("No hay datos para encontrar el valor mayor.")
	else:
		print ("El mayor es: %i" % mayor)

def imprimirMenu ():
	opcion = int (input("1. Encontrar mayor \n2. Recolectar insectos \n3. Salir"))
	while (opcion != 3):
		if (opcion == 1):
			obtenerMayor()
		elif (opcion == 2):
			recolectarInsectos()
		else:
			print ("Opcion invalida. Intenta de nuevo.")
		opcion = int ( input ("1. Encontrar mayor \n2. Recolectar insectos \n3. Salir"))

def main():
	imprimirMenu()

main()

# encoding: UTF-8
# Autor: Sergio Hernandez
# Descripcion: Obtiene el numero mayor de un conjunto de valores enteros positivos

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

def main ():
	obtenerMayor()

main ()

#encoding: UTF-8
#Autor: Astrid M Villegas Berdejo
#Tarea 6
def main ():
    opcion = int( input("1.Encontrar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opción"))
    while opcion !=3:
        if opcion == 1:
            n = int( input("Teclea un número"))
            recibirNumeros (n)
            opcion = int( input("1.Encontrar mayor \n2.Recolectar insectos\n3.Salir\nTeclea tu opción"))
        elif opcion == 2:
            ni = int( input("Insectos recolectados hoy"))
            dia = 1
            contarInsectos (ni,dia)
            opcion = int( input("1.Encontrar mayor \n2.Recolectar insectos\n3.Salir\nTeclea tu opción"))   
        else:
            opcion = int( input ("La opción es incorrecta, elije otra opción:\n1.Encontrar mayor\n2.Recolectar insectos\n3.Salir\nTeclea tu opción"))
    
    if opcion == 3:
        print (" ")
        
def contarInsectos (ni, dia):
    print ("Después de %i día(s) de recolección has acumulado %i insecto(s)" % (dia,ni))
    
    while ni < 30:
        f = 30-ni
        print ("Te hace falta recolectar %i insecto(s)" % f)
            
        dia = dia +1
        n2i = int( input("Insectos recolectados hoy"))
        ni = ni+n2i
        
        print ("Después de %i día(s) de recolección has acumulado %i insecto(s)" % (dia,ni))
        
    if ni >= 30:
        if ni == 30:
            f = 30-ni
            print ("Te hace falta recolectar %i insecto(s)" % f)
            
        else:
            s = ni - 30
            print ("Te has pasado con %i insecto(s)" % s)
            
        print ("Felicidades has llegado a la meta.")         
         
    return (ni,dia)
    
    
def recibirNumeros (n):
    while n != -1:
        n2 = int( input("Teclea un número"))
        if n2 == -1:
            print ("El número mayor es", n)
            n = -1
        elif n < n2 and n != -1:
            n = n2
        elif n >= n2 and n != -1:
            n = n
   
        
    return n
    
main ()
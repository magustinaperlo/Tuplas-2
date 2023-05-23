

#Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y
#muestra los valores de la tupla.
#RESUELVE el caso en que no exista ese índice en la tupla.

tuplDefinida = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
indiceIngresado = input("Inserta un número, este número va a corresponder a un lugar en la tupla y devolverte ese valor: ")
while not indiceIngresado.isdigit() or int(indiceIngresado) >= len(tuplDefinida):
    tamañoTupla = len(tuplDefinida)
    print("El número ingresado no es válido, por favor ingresa un número entre [0:" + str(tamañoTupla - 1) + "]")
    indiceIngresado = input("Inserta un número, este número va a corresponder a un lugar en la tupla y devolverte ese valor: ")
indiceIngresado = int(indiceIngresado)
if indiceIngresado < len(tuplDefinida):
    numeroTupla = tuplDefinida[indiceIngresado]
    print("En el índice " + str(indiceIngresado) + " se encuentra el número " + str(numeroTupla))
else:
    print("El índice ingresado está fuera de rango.")



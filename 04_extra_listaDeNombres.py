#4 Escribe un programa que solicite al usuario que ingrese una lista de nombres. El
#programa debe crear una tupla a partir de la lista y luego imprimir los nombres que
#comienzan con la letra 'A'.
nombresConA=()
listaNombres=[]
msj=""
nombre=""
c=0
b=1
msj="Ingresa una lista de nombres."
while c!=10:
    print(f"Ingrese en {b}° nombre") 
    nombre= str(input())
    nombre=(nombre.lower())
    c+= 1
    b+= 1
    listaNombres.append(nombre)
tuplaDeNombres = tuple(listaNombres)
print(f"Los nombres ingresados son: {tuplaDeNombres}")
for nombre in tuplaDeNombres:
    if nombre[0][0] == "a":
        nombresConA=list(nombresConA)
        nombresConA.append(nombre)
        nombresConA=tuple(nombresConA)
print(f"la tupla de los nombres que cominezan con la letra A : {nombresConA}")


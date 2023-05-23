
import funcionesTuplas

#1 Escribe un programa que solicite al usuario que ingrese una lista de números enteros.
#El programa debe crear una tupla a partir de la lista y luego imprimir la tupla en orden
#inverso.
msj=""
num=0
c=0
listaNum=[]
listaNumRev=[]

msj="Ingresa 10 diferentes numeros para generar una lista"
print(msj)
while c!=10:
    num=(input())
    if num.isnumeric()==True:
        listaNum.append(num)
        c+=1
    else:
        msj="El programa solo acepta numeros enteros, por favor vuelve a iniciarlo"
        print(msj)
    break

print(f"La lista generada es: {listaNum}")
for num in reversed(listaNum):
    listaNumRev.append(num)
tuplListaNum=tuple(listaNumRev)
print(f"la tupla generada reversa es: {tuplListaNum}")



numerosIngresado=[]
msj=""
c=1

msj="Ingresa 4 numeros: "
print(msj)
while c<=4:
    num=input()
    c+=1
    numerosIngresado.append(num)
print(f"Los numeros ingresados son: {numerosIngresado}")
numerosIngresado=tuple(numerosIngresado)
tupla=numerosIngresado
funcionesTuplas.intercambiar_tupla(tupla)



tupInt=()
msj=""
c=1

msj="Ingresa 10 numeros: "
print(msj)
while c<=10:
    num=int(input())
    c+=1
    tupInt=list(tupInt)
    tupInt.append(num)

print(f"Los numeros ingresados son: {tupInt}")

funcionesTuplas.encontrar_pares_impares(tupInt)


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


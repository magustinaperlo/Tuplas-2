'''
#Escribe un programa que solicite al usuario que ingrese una lista de números enteros.
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
'''
import funcionesTuplas
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
tupla=numerosIngresado
funcionesTuplas.intercambiar_tupla(tupla)


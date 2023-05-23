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
numerosIngresado=tuple(numerosIngresado)
tupla=numerosIngresado
funcionesTuplas.intercambiar_tupla(tupla)
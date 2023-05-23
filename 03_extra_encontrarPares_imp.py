import funcionesTuplas
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
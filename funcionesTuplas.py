#2. Escribe una función llamada intercambiar_tupla que acepte una tupla como parámetro
#y devuelva una nueva tupla en la que el primer y el último elemento de la tupla
#original se intercambian. Por ejemplo, si la tupla original es (1, 2, 3, 4), la función
#debería devolver (4, 2, 3, 1).

def intercambiar_tupla(tupla):
    tupla=list(tupla)
    for elemento in tupla:
        num1=tupla[0]
        num2=tupla[-1]
    tupla[0]= num2
    tupla[-1]= num1
    tupla=tuple(tupla)
    print(f"La tupla generada donde el 1er numero se encuentra al ultimo y el el ultimo al incio es:  {tupla}")
    print(type(tupla))

  
#3Escribe una función llamada encontrar_pares_impares que acepte una tupla de
#números enteros como parámetro y devuelva una tupla que contenga dos listas: una
#lista de números pares y otra lista de números impares. Por ejemplo, si la tupla original
#es (1, 2, 3, 4, 5, 6, 7, 8, 9), la función debería devolver ([2, 4, 6, 8], [1, 3, 5, 7, 9]).

def encontrar_pares_impares(tupInt):
    numPares=[]
    numImpares=[]
    tupFinal=[]
    tupInt=list(tupInt)
    for num in tupInt:
        if num % 2 == 0:
            numPares.append(num)
        else:
            numImpares.append(num)
    print(f"Los numeros pares son: {numPares}")
    print(f"Los numeros impares son: {numImpares}")
    tupFinal.append(numImpares)
    tupFinal.append(numPares)
    tupFinal=tuple(tupFinal)
    print(f"La tupla final obtenida es: {tupFinal}")

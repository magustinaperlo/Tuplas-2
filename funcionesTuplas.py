#2. Escribe una función llamada intercambiar_tupla que acepte una tupla como parámetro
#y devuelva una nueva tupla en la que el primer y el último elemento de la tupla
#original se intercambian. Por ejemplo, si la tupla original es (1, 2, 3, 4), la función
#debería devolver (4, 2, 3, 1).

def intercambiar_tupla(tupla):
    for elemento in tupla:
        num1=tupla[0]
        num2=tupla[-1]
    tupla[0]= num2
    tupla[-1]= num1
    tupla=tuple(tupla)
    print(f"La tupla generada donde el 1er numero se encuentra al ultimo y el el ultimo al incio es:  {tupla}")
    print(type(tupla))
    
#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.
tuplNum2=(12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8)

numeroMaximo=0
numeroMinimo=0

for i in tuplNum2:
    numero= i
    if numeroMinimo == 0 and numeroMaximo==0:
        numeroMinimo = numero
        numeroMaximo = numero
    if numero < numeroMinimo:
        numeroMinimo=numero
    if numero > numeroMaximo:
        numeroMaximo=numero
print("El numero Maximo es: " + str(numeroMaximo))
print("El numero Minimo es: " + str(numeroMinimo))

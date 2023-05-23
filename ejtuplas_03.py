#Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se
#repite según lo halle en la tupla que has creado.
#RESUELVE validar los ingresos del usuario.

tuplNum = (12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8)

numeroIngresado = input("Inserta un número entre 0 y 15: ")
while not numeroIngresado.isdigit() or int(numeroIngresado) not in range(16):
    print("El número ingresado no es válido, por favor ingresa un número entre 0 y 15.")
    numeroIngresado = input("Inserta un número entre 0 y 15: ")

numeroIngresado = int(numeroIngresado)
repeticiones = tuplNum.count(numeroIngresado)
print(f"El número {numeroIngresado} aparece {repeticiones} veces en la tupla.")
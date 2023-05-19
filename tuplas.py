
razaBuscada = "siames"
listaProductos = [("toro", 300, 1, "pichichou"), ("gato", 1000, 2, "siames"), ("perro", 1050, 3, "shitzu"), ("vaca", 800, 4, "lechera")]
listaPedido = []
precioMaximo = 1000

print(listaProductos)
for i in listaProductos:
    (animal,precio,cantidad,raza)=i
    if raza==razaBuscada and precio<=precioMaximo:
        listaPedido.append(i)
print(listaPedido)  

#Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la
#longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de
#error.
#El programa termina cuando el usuario introduce un cero.

tuplaMeses=("enero","febrero","marzo","abril","mayo","junio","julio","septiembre","octubre","noviembre","diciembre")
mesSolicitado=[""]
print("inserta un numero entre 1 y 11 --> ")
numero=int(input())
numero=numero-1

if numero <= (len(tuplaMeses)):
    print(tuplaMeses[numero])
else:
    ("ingresa un numero comprendido ente 1 y 11")


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



tuplNum=(12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8)

print("Inserta un numero entre 0 y 15 -->")
numeroIngresado=int(input())

#Crea una tupla con números e indica el numero con mayor valor y el que menor tenga.
tuplNum2=(12, 13, 14, 15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 8)

numeroMaximo=0
numeroMinimo=0

for i in tuplNum:
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




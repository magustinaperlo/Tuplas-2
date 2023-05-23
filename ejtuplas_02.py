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
    #("ingresa un numero comprendido ente 1 y 11")
    #faltó el print para que el usuario vea el mensajito 4
    print("Error: ingresa un numero comprendido ente 1 y 11")

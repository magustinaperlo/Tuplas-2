
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

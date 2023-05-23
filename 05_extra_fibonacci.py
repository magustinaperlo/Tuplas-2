#5. Escribe un programa que cree una tupla que contenga los primeros diez números de la
#serie de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55) y luego imprima la tupla.
fibonacci = [1, 1]

for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])  
fibonacci_tupla = tuple(fibonacci)  
print(f"La tupla con los primeros 10 numeros: {fibonacci_tupla}")



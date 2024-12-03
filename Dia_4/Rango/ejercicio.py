# Crear la lista de números desde 2500 hasta 2585
mi_lista = list(range(2500, 2586))

# Imprimir la lista
print(mi_lista)

# Sumar mos cuadrados 
suma_cuadrados = 0

for numero in range (1, 16):
    cuadrado = numero ** 2 
    suma_cuadrados += cuadrado

print("La suma de los cuadrados de los números del 1 al 15 es:", suma_cuadrados)


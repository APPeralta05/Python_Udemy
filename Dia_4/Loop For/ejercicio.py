#Saludar a los alumnos
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for i in alumnos_clase:
    print(f'Hola {i}')

#Suma de numeros
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero

print('La suma de todos los numeros es:', suma_numeros)

#Suma par o impar
# Definir la lista de números
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

# Inicializar las variables suma_pares y suma_impares
suma_pares = 0
suma_impares = 0

# Calcular la suma de números pares e impares
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Imprimir los resultados de las sumas
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)


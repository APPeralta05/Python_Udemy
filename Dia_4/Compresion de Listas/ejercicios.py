#Elevados al cuadrado
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Crear una nueva lista con los cuadrados de los números en la lista valores
valores_cuadrado = [x**2 for x in valores]

print(valores_cuadrado)

#Numeros pares
valores = [1, 2, 3, 4, 5, 6, 9.5]

# Crear una nueva lista con los números pares de la lista valores
valores_pares = [x for x in valores if x % 2 == 0]

print(valores_pares)

#De farenheit a celcius
temperatura_fahrenheit = [32, 212, 275]

# Convertir las temperaturas de Fahrenheit a Celsius utilizando comprensión de listas
grados_celsius = [(f - 32) * (5/9) for f in temperatura_fahrenheit]

print(grados_celsius)

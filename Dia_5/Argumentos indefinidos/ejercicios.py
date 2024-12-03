#Suma de cuadrados 
def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += num ** 2
    return suma

# Ejemplo de uso:
resultado = suma_cuadrados(1, 2, 3)
print(resultado)  # Salida: 14

#Suma de absolutos
def suma_absolutos(*args):
    suma = 0
    for num in args:
        suma += abs(num)
    return suma

# Ejemplo de uso:
resultado = suma_absolutos(1, -2, 3, -4)
print(resultado)  # Salida: 10

#Numeros persona
def numeros_persona(nombre, *numeros):
    suma_numeros = sum(numeros)
    mensaje = f"{nombre}, la suma de tus números es {suma_numeros}"
    return mensaje

# Ejemplo de uso:
mensaje = numeros_persona("Juan", 1, 2, 3, 4)
print(mensaje)  # Salida: "Juan, la suma de tus números es 10"
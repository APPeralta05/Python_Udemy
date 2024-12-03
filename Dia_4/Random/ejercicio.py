#Numero random del 1 al 10 
import random

# Obtener un número entero aleatorio del 1 al 10
aleatorio = random.randint(1, 10)

print(f"Número entero aleatorio del 1 al 10: {aleatorio}")

#Numero decimal del 0 al 1
import random

# Obtener un número decimal aleatorio entre 0 y 1
aleatorio = random.random()

print(f"Número decimal aleatorio entre 0 y 1: {aleatorio}")

#Obtener un nombre al azar de la lista
import random

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

# Obtener un nombre al azar de la lista
sorteo = random.choice(nombres)

print(f"El nombre escogido es: {sorteo}")
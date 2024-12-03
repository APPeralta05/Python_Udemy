import random

# Preguntar al usuario su nombre
nombre = input("¿Cuál es tu nombre? ")

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número.")

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

while intentos < 8:
    try:
        # Pedir al usuario que elija un número
        numero_elegido = int(input("Ingresa un número entre 1 y 100: "))

        # Verificar si el número elegido está dentro del rango permitido
        if numero_elegido < 1 or numero_elegido > 100:
            print("Has elegido un número que no está permitido.")
            continue

        # Incrementar el contador de intentos
        intentos += 1

        # Verificar si el número elegido es igual al número secreto
        if numero_elegido == numero_secreto:
            print(f"¡Felicidades, {nombre}! Has acertado el número secreto en {intentos} intentos.")
            break
        elif numero_elegido < numero_secreto:
            print("Tu respuesta es incorrecta. Has elegido un número menor al número secreto.")
        else:
            print("Tu respuesta es incorrecta. Has elegido un número mayor al número secreto.")

        # Informar cuántos intentos le quedan al usuario
        print(f"Te quedan {8 - intentos} intentos.")

    except ValueError:
        print("Debes ingresar un número válido.")

# Si el usuario agota los intentos sin acertar
if intentos == 8:
    print(f"Lo siento, {nombre}. Has agotado tus 8 intentos. El número secreto era {numero_secreto}.")

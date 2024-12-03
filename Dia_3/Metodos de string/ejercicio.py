#IMPRIME EL TEXTO EN MAYUSCULAS(UPPER)

frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
frase_en_mayusculas = frase.upper()

print(frase_en_mayusculas)

#separa con un espacio

lista_palabras = ["La", "legibilidad", "cuenta."]
frase_unida = " ".join(lista_palabras)

print(frase_unida)

#remplaza por "mala" a "buena" y de "facil" a "dificil"

frase_original = "Si la implementación es difícil de explicar, puede que sea una mala idea."

# Creamos un diccionario con las palabras a reemplazar como clave y su reemplazo como valor
cambios = {
    "difícil": "fácil",
    "mala": "buena"
}

# Recorremos el diccionario para realizar las sustituciones
frase_modificada = frase_original
for palabra_original, palabra_nueva in cambios.items():
    frase_modificada = frase_modificada.replace(palabra_original, palabra_nueva)

# Imprimimos la frase modificada
print(frase_modificada)


# Ingresar texto y letras
texto = input("Ingrese un texto: ")
letras = input("Ingrese tres letras (sin espacios): ")

#Convertir texto y letras a minusculas para el analisis

texto = texto.lower()
letras = letras.lower()

#Contar apariciones de cada letra

apariciones = {letra: texto.count(letra) for letra in letras}

#Contar palabras en el texto

palabras = texto.split()
cantidad_palabras = len(palabras)

#Identificar primera y ultima letra

primer_letra = texto[0]
ultima_letra = texto[-1]

#Inverit el orden de las palabras 

texto_invertido = ' '.join(reversed(palabras))

#Verificar si 'Python' esta en el texto

contiene_python = 'python' in texto

#Mostrar los resultados

print(f"1. Apariciones de las letras: {apariciones}")
print(f"2. Cantidad de palabras: {cantidad_palabras}")
print(f"3. Primer letra: {primer_letra}, Ultima letra: {ultima_letra}")
print(f"4. Texto invertido: {texto_invertido}")
print(f"5. ¿Contiene la palabra 'Python'?: {'Si' if contiene_python else 'No'}")
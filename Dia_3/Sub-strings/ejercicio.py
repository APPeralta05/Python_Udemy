#EXTRAER PRIMER PALABRA 
frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[0:9]
print(fragmento)

#EXTRAER EL 3ER CARACTER DE CADA FRASE
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
extraer = frase[8::3]
print(extraer)

#Invierte la posición de todos los caracteres
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]  # Invertir la posición de todos los caracteres
print(resultado)
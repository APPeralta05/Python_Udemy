#ENCUENTRA LA LETRA "N"
palabra = "ordenador"
encontrar_letra = palabra[4]
print(encontrar_letra)

#ENCUENTRA LA PALABRA "PRACTICA"
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
palabra = frase.index("práctica")
print(palabra)

#ENCUENTRA LA PALABRA "PRACTICA" DE ATRAS PARA ADELANTE
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
palabra = frase.rindex("práctica")
print(palabra)
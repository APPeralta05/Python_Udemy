#Valor maximo 
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)

print(f"El valor máximo de la lista es: {valor_maximo}")

#Rango 
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numeros) - min(lista_numeros)

print(f"El rango de la lista es: {rango}")

#Obtener el valor de cada uno 
diccionario_edades = {
    "Carlos": 55, "María": 42, "Mabel": 78, "José": 44, "Lucas": 24,
    "Rocío": 35, "Sebastián": 19, "Catalina": 2, "Darío": 49
}

# Obtener el mínimo valor de las edades
edad_minima = min(diccionario_edades.values())

# Obtener el nombre que se ubica último en orden alfabético
ultimo_nombre = sorted(diccionario_edades.keys())[-1]

print(f"La edad mínima es: {edad_minima}")
print(f"El último nombre en orden alfabético es: {ultimo_nombre}")

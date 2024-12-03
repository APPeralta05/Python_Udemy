#Imprime frases
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate (lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#
cadena = "Python"

# Crear la lista de tuplas (índice, elemento) utilizando enumerate
lista_indices = [(indice, caracter) for indice, caracter in enumerate(cadena)]
# Imprimir la lista de tuplas
print(lista_indices)

# Definir la lista de nombres
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Imprimir los índices de los nombres que empiezan con "M"
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)

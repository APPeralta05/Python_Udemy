#contar la cantidad de veces que aparece el 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

# Contar la cantidad de veces que aparece el valor 2 en la tupla
cantidad = mi_tupla.count(2)

print(cantidad)

#modificar tuple a lista
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)

# Convertir la tupla a lista
mi_lista = list(mi_tupla)

print(mi_lista)

#extraer los elementos
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a)
print(b)
print(c)
print(d)
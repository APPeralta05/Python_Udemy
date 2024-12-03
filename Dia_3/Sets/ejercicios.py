#unir los sets

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)

print(mi_set_3)

#elimina un elemento al azar
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

#agraga damian 
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)
#crea un diccionario
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

print(mi_dic)

#imprimir el segungo item de points2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}

def print_second_item(dic):
    second_item = dic["puntos"]["points2"][1]
    print(second_item)

print_second_item(mi_dict)

#editar 
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

# Actualizar los valores de las claves existentes y agregar una nueva clave
mi_dic.update({
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 36,
    "ocupacion": "Editora",
    "pais": "Colombia"
})

print(mi_dic)

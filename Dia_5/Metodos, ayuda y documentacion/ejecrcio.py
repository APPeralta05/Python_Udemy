#Remueve los caracteres de la izquierda
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"))

#Añade un elemento al 4to
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")

#Verifica los sets
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)
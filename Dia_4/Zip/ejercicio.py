#Capitales
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")

# marcas

marcas = ["Nike", "Apple", "Samsung", "Adidas", "Sony"]
productos = ["Zapatillas", "iPhone", "Smartphone", "Ropa deportiva", "Televisor"]

mi_zip = zip(marcas, productos)

for marca, producto in mi_zip:
    print(f"La marca {marca} produce {producto}")

#Tradcciones de numeros
espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

mi_zip = zip(espanol, portugues, ingles)

numeros = list(mi_zip)

for traducciones in numeros:
    print(f"El idioma Español, su traduccion es: {traducciones[0]} ")
    print(f"El idioma Portuges, su traduccion es: {traducciones[1]}")
    print(f"El idioma Ingles, su traduccion es: {traducciones[2]}")
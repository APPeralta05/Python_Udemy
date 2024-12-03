#Lista de numeros positivos o negativos
def todos_positivos(lista):
    for numero in lista:
        if numero <= 0:
            return False
    return True
lista_numeros = [1, 2, -3, 4, -5]  
# Puedes asignar cualquier lista de números a esta variable

#Suma menores
def suma_menores(lista):
    suma = 0
    for numero in lista:
        if 0 < numero < 1000:
            suma += numero
    return suma
lista_numeros = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]  
# Puedes asignar cualquier lista de números a esta variable

#Cuente la cantidad de numeros
def cantidad_pares(lista):
    contador_de_pares = 0
    for numero in lista:
        if numero % 2 == 0:
            contador_de_pares += 1
    return contador_de_pares
lista_numeros = [2,4,6,5,3,1]
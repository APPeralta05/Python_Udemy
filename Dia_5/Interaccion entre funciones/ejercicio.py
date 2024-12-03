#Ejercicio de dados
import random

def lanzar_dados():
    resultado_uno = random.randint(1,6)
    resultado_dos = random.randint(1,6)
    return resultado_uno, resultado_dos
def evaluar_jugada(resultado_uno,resultado_dos):
    suma_dados = resultado_uno + resultado_dos
    
    if suma_dados <= 6:
        mensaje = f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        mensaje = f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    return mensaje

#Promedios y eliminar los duplicados
def reducir_lista(lista):
    #Eliminar los duplicados y valor mas elevado
    lista_sin_duplicados = list(set(lista))
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return lista_sin_duplicados
    
def promedio(lista):
    #Calcular el promedio
    if len(lista) == 0:
        return 0 #Devolver lista vacia
    else:
        return sum(lista) / len(lista)
#Crear la lista num 
lista_numeros = [1,2,3,4,5,5,5,6,6,67,2]

#Lanzar moneda
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif resultado_moneda == "Cruz":
        print("La lista fue salvada")
        return lista

# Crear la lista lista_numeros
lista_numeros = [1, 2, 3, 4, 5]

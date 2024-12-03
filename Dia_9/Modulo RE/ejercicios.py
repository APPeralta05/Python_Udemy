#1

import re
def verificar_email(email):
    # Definir el patrón de expresión regular
    patron = r'^[\w\.-]+@[\w\.-]+\.(com|com\.br)$'
    
    # Comprobar si el email coincide con el patrón
    if re.match(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

#2

import re

def verificar_saludo(frase):
    # Definir el patrón de expresión regular
    patron = r'^Hola'
    
    # Comprobar si la frase comienza con "Hola"
    if re.match(patron, frase):
        print("Ok")
    else:
        print("No has saludado")

#3

import re

def verificar_cp(codigo_postal):
    # Definir el patrón de expresión regular
    patron = r'^[A-Za-z0-9]{2}\d{4}$'
    
    # Comprobar si el código postal coincide con el patrón
    if re.match(patron, codigo_postal):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
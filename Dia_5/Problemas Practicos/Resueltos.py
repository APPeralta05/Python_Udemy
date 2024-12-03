## Problema 1 
def devolver_distintos(a, b, c):
    '''
    Esta función recibe 3 números enteros como parámetros.
    Si la suma de los 3 números es mayor a 15, devuelve el número mayor.
    Si la suma de los 3 números es menor a 10, devuelve el número menor.
    Si la suma de los 3 números es un valor entre 10 y 15 (incluidos), devuelve el número de valor intermedio.
    '''
    suma = a + b + c
    
    if suma > 15:
        return max(a, b, c)
    elif suma < 10:
        return min(a, b, c)
    else:
        return sorted([a, b, c])[1]

## Problema 2 
def letras_unicas_ordenadas(palabra):
    '''
    Esta función recibe una palabra como parámetro y devuelve una lista
    de las letras únicas de la palabra, ordenadas alfabéticamente.
    '''
    letras_unicas = set(palabra)
    return sorted(letras_unicas)


## Problema 3 
def cero_dos_veces_consecutivas(*args):
    '''
    Esta función recibe una cantidad indefinida de argumentos.
    Devuelve True si en algún momento se ha ingresado el número cero
    repetido dos veces consecutivas. De lo contrario, devuelve False.
    '''
    for i in range(len(args) - 1):
        if args[i] == 0 and args[i+1] == 0:
            return True
    return False



## Problema 4

def contar_primos(n):
    '''
    Esta función muestra en pantalla todos los números primos en el rango
    desde 0 hasta el número dado (incluido) y devuelve la cantidad de números primos encontrados.
    '''
    def es_primo(num):
        '''
        Función auxiliar para verificar si un número es primo.
        '''
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    cantidad_primos = 0
    for i in range(n + 1):
        if es_primo(i):
            print(i)
            cantidad_primos += 1
    
    return cantidad_primos

import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero, + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


declaracion = '''
prueba_for(10)

'''

mi_setup = '''

'''


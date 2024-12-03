'''
Esto es un turnero de una farmacia
'''


def numeros_perfumeria():
    '''
    Recore la cantidad de numeros y lo imprime
    '''
    for n in range(1, 10000):
        yield f'P - {n}'


def numeros_farmacia():
    for n in range(1, 10000):
        yield f'F - {n}'


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f'C - {n}'


p = numeros_perfumeria()

f = numeros_farmacia()

c = numeros_cosmetica()


def decorador(rubro):

    print('\n' + '*' * 23)
    print('Su numero es: ')
    if rubro == 'P':
        print(next(p))
    elif rubro == 'F':
        print(next(f))
    else:
        print(next(c))
    print(('Aguarde y será atendido'))
    print('*' * 23 + '\n')

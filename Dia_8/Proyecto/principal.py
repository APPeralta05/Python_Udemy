import numeros

def preguntar():

    print('Hola! Bienvenido a Farmacia Alejo')

    while True:

        print('[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética')
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ['P', 'F', 'C'].index(mi_rubro)
        except ValueError:

            print('Esa no es una opcion valida')
        else:

            break

    numeros.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()

        try:
            otro_turno = input('¿Quieres sacar otro turno? [S] [N]: ').upper()
            ['S', 'N'].index(otro_turno)

        except ValueError:
            print('Esa no es una opcion válida')

        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break

inicio()

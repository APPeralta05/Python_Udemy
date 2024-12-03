def suma():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1 + n2)
    print('Gracias por sumar')



try:
    #codigo de prueba
    suma()
except:
    print('Algo no ha salido bien')
    #codigo que se va a ejecutar si no hay error
else:
    print('Hiciste todo correcto')
    #codigo a ejecutar si no hay error
finally:
    print('Eso fue todo')
    #codigo que se va a ejecutar de todos modos 
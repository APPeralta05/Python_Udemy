##1
def suma(num1, num2):
    try:
        resultado = num1 + num2
        print(resultado)
    except Exception as e:
        print("Error inesperado")

##2

def cociente(num1, num2):
    try:
        resultado = num1 / num2
        print(resultado)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    except Exception as e:
        print("Error inesperado")

##3

def abrir_archivo(mi_texto):
    try:
        archivo = open(mi_texto, 'r')
        print("Abriendo exitosamente")
        # Aquí podrías añadir más código para trabajar con el archivo
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except Exception as e:
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")

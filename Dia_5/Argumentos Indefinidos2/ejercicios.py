def cantidad_atributos(**kwargs):
    """
    Esta función cuenta la cantidad de argumentos de palabra clave proporcionados.

    Args:
    **kwargs: Una cantidad variable de argumentos de palabra clave (nombre=valor).

    Returns:
        int: El número total de argumentos de palabra clave recibidos.
    """
    return len(kwargs)

# Ejemplo de uso:
resultado1 = cantidad_atributos(nombre="Alice", edad=30, ciudad="Madrid")
resultado2 = cantidad_atributos(x=5, y=10, z=15)

print(resultado1)  # Salida: 3
print(resultado2)  # Salida: 3

##2

def lista_atributos(**kwargs):
        return list(kwargs.values())

##3
def describir_persona(nombre, **kwargs):
    '''
    Esta función muestra en pantalla las características de una persona.
    Recibe como parámetros el nombre de la persona y una cantidad indeterminada de argumentos.
    '''
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
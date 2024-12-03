##1
def abrir_leer(nombre_archivo):
    """
    Abre un archivo especificado por 'nombre_archivo' y devuelve su contenido.
    
    Args:
        nombre_archivo (str): La ruta al archivo que se desea abrir.
        
    Returns:
        str: El contenido del archivo.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"El archivo '{nombre_archivo}' no se encontró."
    except IOError as e:
        return f"Error al leer el archivo: {e}"

# Ejemplo de uso
ruta_archivo = 'Día 6/practicas_path.py'
contenido = abrir_leer(ruta_archivo)
print(contenido)

##2
def sobrescribir(nombre_archivo):
    """
    Abre un archivo especificado por 'nombre_archivo' y sobrescribe su contenido con "contenido eliminado".
    
    Args:
        nombre_archivo (str): La ruta al archivo que se desea sobrescribir.
    """
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("contenido eliminado")
        print(f"El contenido del archivo '{nombre_archivo}' ha sido sobrescrito.")
    except IOError as e:
        print(f"Error al sobrescribir el archivo: {e}")

# Ejemplo de uso
ruta_archivo = 'Día 6/practicas_path.py'
sobrescribir(ruta_archivo)

##3 

def registro_error(archivo):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()
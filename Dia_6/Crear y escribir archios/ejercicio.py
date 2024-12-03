## 1 
# Abrir el archivo en modo escritura y escribir el nuevo texto
with open("mi_archivo.txt", "w") as archivo:
    archivo.write("Nuevo texto")

# Abrir el archivo en modo lectura y imprimir su contenido
with open("mi_archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    
##2
archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

##3

# Lista con los datos de la última sesión
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

# Convertir la lista en una cadena con tabuladores y añadir un salto de línea al final
registro_ultima_sesion = '\t'.join(registro_ultima_sesion) + '\n'

# Abrir el archivo en modo adición y escribir los datos
with open("registro.txt", "a") as archivo:
    archivo.write(registro_ultima_sesion)

# Abrir el archivo en modo lectura y imprimir su contenido
with open("registro.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
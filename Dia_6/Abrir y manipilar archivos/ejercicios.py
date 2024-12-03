mi_archivo = open('prueba.txt')

print(mi_archivo.read())

## 2 

mi_archivo = open('prueba.txt')

print(mi_archivo.readline())

##3

fichero = open("texto.txt")

for numero, linea in enumerate(fichero):
    if numero == 1:  # Segunda línea, pues la primera sería la numero 0
        break
fichero.close()
print(linea)
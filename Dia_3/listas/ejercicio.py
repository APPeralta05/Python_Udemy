#crea una lista con string booleano o numeros
mi_lista = [2, "hola", True, "alejo", 5]

#agrega motocicleta 
medios_transporte = ["avión", "auto", "barco", "bicicleta"]

# Agregar "motocicleta" al final de la lista
medios_transporte.append("motocicleta")

print(medios_transporte)

#elimina el tercer elemento de la lista
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]

# Elimina el tercer elemento (índice 2) y lo almacena en "eliminado"
eliminado = frutas.pop(2)

print(f"Elemento eliminado: {eliminado}")
print(f"Lista actualizada: {frutas}")

# Pedir al usuario su nombre y monto de ventas
nombre = input("Hola, ¿cuál es tu nombre? ")
monto_ventas_str = input("Hola {}, ¿cuánto has vendido este mes? ".format(nombre))

# Convertir el monto de ventas a un número de punto flotante (float)
monto_ventas = float(monto_ventas_str)

# Calcular la comisión (13% de las ventas)
comision = monto_ventas * 13 / 100

# Formatear el resultado para que tenga solo dos decimales
comision_formateada = "{:.2f}".format(comision)

# Mostrar la respuesta
print("Hola {}, este mes has vendido ${}. Tu comisión correspondiente es de ${}.".format(nombre, monto_ventas_str, comision_formateada))
# Solicitar al usuario que ingrese los valores de num1 y num2
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#Puede conducir?
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")

elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

elif edad >= 18 and not tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")

#Sabe python?

# Definir las habilidades del candidato
sabe_python = False
habla_ingles = True

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles != True and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles == True and sabe_python != True:
    print("Para postularte, necesitas saber programar en Python")
else:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
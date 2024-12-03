#Imprime del 10 al 0
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1

#Restar numero del 50 al 0 y mostrar si es divisible por 5
# Inicializar la variable numero con el valor 50
numero = 50

# Bucle while para restar de uno en uno desde 50 hasta 0
while numero >= 0:
    # Verificar si el número es divisible por 5
    if numero % 5 == 0:
        print(numero)
    
    # Restar 1 al número
    numero -= 1

#Imprime los positivos
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero <= 0:
        break
    else:
        print(numero)
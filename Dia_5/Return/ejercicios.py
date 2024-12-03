#Devuelve el numero que resuelve una potencia
def potencia(base,exponente):
    resultado = base ** exponente
    return resultado

#Conversion de moneda
def usd_a_eur(monto_usd):
    tasa_conversion = 0.90  # 1 USD = 0.90 EUR
    monto_eur = monto_usd * tasa_conversion
    return monto_eur
dolares = 100

#Invertir palabra
def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1]  # Invertir la palabra
    return palabra_invertida.upper()   # Convertir a mayúsculas y devolver

palabra = "Python"  # Puedes asignar cualquier palabra a esta variable
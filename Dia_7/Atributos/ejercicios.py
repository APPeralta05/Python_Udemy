#1

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco', 4)

#2

class Cubo:
    # Atributo de clase
    caras = 6

    def __init__(self, color):
        # Atributo de instancia
        self.color = color

# Crear una instancia de la clase Cubo
cubo_rojo = Cubo("rojo")

#3

class Personaje:
    real = False
    def __init__(self,especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

especie = 'Humano'
magico = True
edad = 17
harry_potter = Personaje(especie, magico, edad)
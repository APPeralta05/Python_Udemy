#1

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

#2

class Jugador:
    # Atributo de clase
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        
#3
class Personaje:
    def __init__(self,cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1

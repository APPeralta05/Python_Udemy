#1

class Perro:
    def ladrar(self):
        print(f'Guau!')

#2

class Mago:
    def lanzar_hechizo(self):
        print(f'¡Abracadabra!')

merlin = Mago()
merlin.lanzar_hechizo()

#3

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
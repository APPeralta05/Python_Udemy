##1

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for dato in [palabra, lista, tupla]:
    print(len(dato))

#2

class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        
arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero,mago,samurai]

for personaje in personajes:
    personaje.atacar()

##3

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()
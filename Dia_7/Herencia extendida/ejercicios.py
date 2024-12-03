#1

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    def trabajar(self):
        print("Trabajando en la Fiscalía")

##2

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    def poner_huevos(self):
        print("Ornitorrinco poniendo huevos")

# Crear una instancia de Ornitorrinco
ornitorrinco = Ornitorrinco()

# Verificar los atributos y métodos del ornitorrinco
print(f"Es vertebrado: {ornitorrinco.vertebrado}")
print(f"Tiene pico: {ornitorrinco.tiene_pico}")
print(f"Es venenoso: {ornitorrinco.venenoso}")

ornitorrinco.poner_huevos()
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()

## 3 

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
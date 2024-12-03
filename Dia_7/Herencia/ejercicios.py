##1
class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass
#2

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass

#3

class Vehiculo:
    def acelerar(self):
        pass  # Método en blanco, se puede implementar más tarde

    def frenar(self):
        pass  # Método en blanco, se puede implementar más tarde

class Automovil(Vehiculo):
    pass  # Hereda de Vehiculo, no necesita implementación adicional para este ejemplo

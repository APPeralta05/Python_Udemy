class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(self.nombre + ' dice muuuu')
    
class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beeee')


vaca1 = Vaca('Lola')
oveja1 = Oveja('Doly')

def animal_habla(animal):
    animal.hablar()
    

animal_habla(oveja1)
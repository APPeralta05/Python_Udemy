class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    
    
    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

cani = Pajaro(2, 'Azul')

print(cani.color)
class Pajaro:
    alas = True
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, de color {}'.format(self.color))
        
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')

alejin = Pajaro('azul', 'colibrii')
alejin.piar()
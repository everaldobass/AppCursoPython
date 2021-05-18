from FiguraGeometrica import *

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        FiguraGeometrica.__init__(self,"Triangulo")

        self.base = base 
        self.altura = altura
        

    def calcula_area(self):
        return (self.base * self.altura) / 2
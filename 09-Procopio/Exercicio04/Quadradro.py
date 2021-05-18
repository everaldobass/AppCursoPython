from FiguraGeometrica import *

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        FiguraGeometrica.__init__(self,"Quadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
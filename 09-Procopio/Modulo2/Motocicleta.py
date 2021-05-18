from Modulo2.Veiculo import *

class Motocicleta(Veiculo):
    def __init__(self, aro, marca, qtde_raios_roda):

        Veiculo.__init__(self, aro, marca)

        self.qtde_raios_roda = qtde_raios_roda

    def usarCapacete(self):
            print("\nUsando capacete")


    
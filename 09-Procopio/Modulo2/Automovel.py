from Modulo2.Veiculo import *

class Automovel(Veiculo):
    def __init__(self, aro, marca, volume_porta_mala):

        Veiculo.__init__(self, aro, marca)
        self.volume_porta_mala = volume_porta_mala

    def ligar_luiz_teto(self):
        print("\nLuiz ligada.")
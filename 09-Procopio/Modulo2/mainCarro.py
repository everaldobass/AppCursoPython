from Modulo2.Automovel import *
from Modulo2.Motocicleta import *

print("\n Instanciando um Carro")
carro = Automovel(17, "Honda", 500)
carro.ligar_luiz_teto()
carro.acelerar()
carro.frear()

print("\n Instanciando uma Moto")
moto = Motocicleta(14, "honda", 50)
moto.acelerar()
moto.frear()
moto.usarCapacete()
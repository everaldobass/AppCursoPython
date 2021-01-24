"""
10.3 - Métodos
Os métodos são funções intrínsecas aos objetos, que podem ser chamados de forma similar
aos atributos e definidos como se fossem funções. Continuando com o exemplo da classe
Caderno:
"""

class Carderno():
    cor = "preto"
    np = 10

    def Descrever(self):
        print("\n--------------------Método em Python-------------------------------")
        print("\nEste objeto é um caderno, que contém a cor e número de páginas")

cad1 = Carderno()
cad1.cor
cad1.np
cad1.Descrever()

print("\nCaderno de Cor: ",cad1.cor)
print("\nCaderno np: ",cad1.np)
print(cad1.Descrever) 
"""
Uma classe possui instância de atributos, instância de métodos e classes aninhadas.
Ou seja, um objeto irá possuir dentro dele alguns valores (atributos), algumas funções
(métodos) e algumas classes (aninhadas).


A definição de uma classe é por meio da palavra reservada class, uma classe vazia pode
ser definida como:

"""

class Vazia():
    pass

x = Vazia

"""

10.2 - Atributos
Os atributos são os valores que existem dentro do objeto. Por exemplo: uma classe Caderno
será criada, definindo dois atributos, cor e np (número de págias):

"""

class Caderno():
    cor = "Preto"
    np = 10


CaderNovo = Caderno()
CaderNovo.cor
CaderNovo.np

print(CaderNovo.cor)
print(CaderNovo.np)



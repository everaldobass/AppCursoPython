
# Importando a classe Idioma
from Idioma import *

class Portugues(Idioma):
     def __init__(self):
         Idioma.__init__(self)
         
     def saudar(self):
         print("Oi")
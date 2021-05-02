# POO: Aula 07 - Retorno de métodos
class Jogador:

    def __init__(self, nome):
        self.nome = nome
        self.gols = 0

    def marcar_gol(self):
        self.gols = self.gols + 1 # self.gols +=1

    def get_gols(self):
        return self.gols
        
    def __str__(self):
        pass
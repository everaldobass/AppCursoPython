# Declaração de classes
class Smartphone:
    # Aula 05 - Parametros
    def __init__(self, memoria, armazenamento, polegadas):
        # Aula 05 - Atributos e métodos 
        self.memoria       = memoria
        self.armazenamento = armazenamento
        self.polegadas     = polegadas

    # Aula 06 - Método str - Imprime os parametros 
    def __str__(self):
        print(f"Memmória: {self.memoria}\n"
              f"Armazenamento: {self.armazenamento} \n"
              f"Polegadas: {self.polegadas}")
    
    # Aula 04 - Métodos ou Ações da Classe
    def enviar_mensagem(self):
        return "Oi!!"
    def instalar_app(self):
        return "App instalado com sucesso! "

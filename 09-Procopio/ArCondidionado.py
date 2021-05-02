#POO: Aula 08 - O que é agregação?
class ArCondidionado:
    def __init__(self):
        self.temperatura = 25
        self.ligado      = False

    def ligar(self):
        if self.ligado == False:
           self.ligado = True
           print("Ar-condicionado ligado! ")

        else:
            print(" Erro: o ar-condicionado já está ligado!")

    def desligar(self):
        if self.ligado == True:
           self.ligado = False
           print("Ar-condicionado desligado! ")

        else:
            print(" Erro: o ar-condicionado já está desligado!")
    
    def aumentar_temperatura(self):
        if self.temperatura < 27:
            self.temperatura +=1
            print(f"Temperatura = {self.temperatura}")
        else:
            print("Ar-condicionado na temperatura máxima!!")

    def baxar_temperatura(self):
        if self.temperatura > 16:
            self.temperatura -=1
            print(f"Temperatura = {self.temperatura}")
        else:
            print("Ar-condicionado na temperatura minima!!")
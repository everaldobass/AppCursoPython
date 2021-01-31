from tkinter import *

app = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()

        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.geometry(width=800, heigth=400)
        
    

app.mainloop()
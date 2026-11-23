from tkinter import *

class App:
    def __init__(self):
        self.janela=Tk()
        self.janela.geometry("330x250")

        self.frame1 = Frame(self.janela, width=200, height=150, bg="lightblue")
        self.frame1.pack(pady=10)
        self.frame1.pack_propagate(False)

        self.frame1.bind('<Button-1>', self.tratadorDoEvento) # Botão esquerdo do mouse
        self.frame1.bind('<Button-2>', self.mudarParaVermelho) # Botão meio do mouse
        self.frame1.bind('<Button-3>', self.mudarParaAmarelo)
        
        self.janela.mainloop()

    def tratadorDoEvento (self, event):
        print('Você clicou na Posição', event.x, event.y) # Coordenadas do mouse

    def mudarParaVermelho (self, event):
        self.frame1.config(bg="red") # Mudar cor do frame

    def mudarParaAmarelo (self, event):
        self.frame1.config(bg="yellow") # Mudar cor do frame

aplicacao = App()
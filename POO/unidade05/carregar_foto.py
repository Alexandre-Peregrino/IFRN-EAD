from tkinter import *
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.janela = Tk()

        self.tamanho = 1
        self.imagemOriginal = Image.open('imagem1.png')
        self.figura1Carregada = ImageTk.PhotoImage(self.imagemOriginal)

        self.figura1 = Label(self.janela)
        self.figura1['image'] = self.figura1Carregada
        self.figura1.pack()

        self.botao1 = Button(self.janela, text='Muda Tamanho')
        self.botao1['command'] = self.mudar
        self.botao1.pack()

        self.janela.mainloop()

    def mudar(self):
        if self.tamanho == 1:
            nova = self.imagemOriginal.resize(
                (self.imagemOriginal.width // 2, self.imagemOriginal.height // 2)
            )
            self.tamanho = 2
        else:
            nova = self.imagemOriginal
            self.tamanho = 1

        self.figura1Carregada = ImageTk.PhotoImage(nova)
        self.figura1['image'] = self.figura1Carregada

aplicacao = App()
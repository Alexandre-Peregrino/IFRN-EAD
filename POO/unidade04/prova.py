from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()

        self.frame1 = Frame(self.janela)
        #self.frame1.pack()          # ← linha que falta

        self.botao1 = Button(self.frame1, text='Oi!')
        self.botao1.pack()

        self.janela.mainloop()

aplicacao = App()
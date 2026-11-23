from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("330x250")

        self.botao1 = Button(self.janela, text='Aperte')
        self.botao1.bind('<Return>', self.enter_apertado)
        self.botao1.bind('<Button-1>', self.click_mouse)
        self.botao1.focus()
        self.botao1.pack(expand=True)

        self.janela.mainloop()

    def enter_apertado(self, event):
            print('Tecla Enter Apertada.')

    def click_mouse(self, event):
            print('Eu disse apertar Enter!!! Não Clicar!!!')

aplicacao = App()
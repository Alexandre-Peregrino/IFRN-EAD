from tkinter import *

class App:

    def __init__(self):
        self.janela = Tk()
        self.janela.title('Botões com Imagens')

        self.figura1Carregada = PhotoImage(file='btn_ok.png')
        self.figura2Carregada =PhotoImage(file='btn_cancel.png')

        self.botao1 = Button(self.janela, text='OK')
        self.botao1['compound'] = 'left'
        self.botao1['image'] = self.figura1Carregada
        self.botao1['width'] = 100
        self.botao1.pack(side = LEFT, pady = 20, padx = 10)

        self.botao2 = Button(self.janela, text='Cancelar')
        self.botao2['compound'] = 'left'
        self.botao2['image'] = self.figura2Carregada
        self.botao2['width'] = 100
        self.botao2.pack(side = RIGHT, pady = 20, padx = 10)

        self.janela.mainloop()

aplicacao = App()

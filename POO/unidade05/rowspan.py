from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Uso do Grid')

        self.texto1 = Label(self.janela, text='Nome:')
        self.texto1.grid(row=0, column=0)

        self.caixa1 = Entry(self.janela)
        self.caixa1.grid(row=0, column=1, columnspan=2)

        self.botaoExibir = Button(self.janela, text='Exibir', command=self.exibir)
        self.botaoExibir.grid(row=1, column=1)

        self.textoResultado = Label(self.janela, text='Resultado', bg='black', fg='yellow')
        self.textoResultado.grid(row=2, column=1)

        self.janela.mainloop()

    def exibir(self):
        texto = self.caixa1.get().strip()
        if texto:
            self.textoResultado['text'] = texto
        else:
            self.textoResultado['text'] = 'Digite algo primeiro'

aplicacao = App()
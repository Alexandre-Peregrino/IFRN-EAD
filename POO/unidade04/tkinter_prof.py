from tkinter import *

class App:

    def __init__(self):
        self.janela = Tk()

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.texto1 = Label(self.frame1)
        self.texto1['text'] = 'Roberto Carlos'
        self.texto1['bg'] = 'black'
        self.texto1['fg'] = 'white'
        self.texto1['font'] = ('Arial', '20', 'bold')
        self.texto1.pack()

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.texto2 = Label(self.frame2, text='None: ')
        self.texto2.pack(side = LEFT)

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(side = RIGHT)

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.texto3 = Label(self.frame3, text='Telefone: ')
        self.texto3.pack(side = LEFT)

        self.caixa3 = Entry(self.frame3)
        self.caixa3.pack(side = RIGHT)
        



        self.janela.mainloop()

aplicacao=App()
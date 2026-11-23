from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry('300x200')
        self.janela.bind('<KeyPress>', self.teclaPressionada)

        self.texto1 = Label(self.janela, text='Pressione uma Tecla')
        self.texto1.pack(pady=30)

        self.janela.mainloop()

    def teclaPressionada(self, event):
        self.texto1['text'] = 'Tecla Pressionada: '+event.char

aplicacao=App()
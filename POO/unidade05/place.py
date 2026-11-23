from tkinter import *

class App():

    def __init__(self):

        self.janela = Tk()
        self.janela.title('Uso do Place')
        self.janela.geometry('280x200')

        self.label1 = Label(self.janela, text = 'Nota1')
        self.label1.place(x = 10, y=10)

        self.entrada1 = Entry(self.janela, bd = 5)
        self.entrada1.place(x = 60, y = 10)

        self.label2 = Label(self.janela, text = 'Nota2')
        self.label2.place(x = 10, y=50)

        self.entrada2 = Entry(self.janela, bd = 5)
        self.entrada2.place(x = 60, y = 50)

        self.label3 = Label(self.janela, text = 'Media')
        self.label3.place(x = 10, y=150)

        self.resultado = Label(self.janela, bd = 5)
        self.resultado.place(x = 70, y = 150)

        self.botao = Button(self.janela, text= "Calcular", command=self.calcular)
        self.botao.place(x = 100, y = 100)

        self.janela.mainloop()

    def calcular(self):
        try:
            nota1 = float(self.entrada1.get())
            nota2 = float(self.entrada2.get())
        except ValueError:
            self.resultado.delete(0, END)
            self.resultado.insert(0, 'Valor inválido')
            return

        media = (nota1 + nota2) / 2
        self.resultado.delete(0, END)
        self.resultado.insert(0, media)
    

aplicacao=App()

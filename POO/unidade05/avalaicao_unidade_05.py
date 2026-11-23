from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Agenda')
        self.janela.geometry('280x200')

        self.agenda = {}   # dicionário nome -> telefone

        self.label1 = Label(self.janela, text='Insira Contatos na Agenda')
        self.label1.grid(row=0, column=0, columnspan=2, pady=10)

        self.label2 = Label(self.janela, text='Nome')
        self.label2.grid(row=1, column=0, sticky='e', padx=5, pady=5)

        self.entrada1 = Entry(self.janela, bd=5)
        self.entrada1.grid(row=1, column=1, padx=5, pady=5)

        self.label3 = Label(self.janela, text='Telefone')
        self.label3.grid(row=2, column=0, sticky='e', padx=5, pady=5)

        self.entrada2 = Entry(self.janela, bd=5)
        self.entrada2.grid(row=2, column=1, padx=5, pady=5)

        self.botao = Button(self.janela, text="Inserir", command=self.inserir)
        self.botao.grid(row=3, column=0, columnspan=2, pady=10)

        self.janela.mainloop()

    def inserir(self):
        nome = self.entrada1.get().strip()
        telefone = self.entrada2.get().strip()

        if not nome or not telefone:
            print('Preencha nome e telefone.')
            return

        self.agenda[nome] = telefone
        print(self.agenda)

        self.entrada1.delete(0, END)
        self.entrada2.delete(0, END)

aplicacao = App()
from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk() # Classe com todas as funções Tkinter
        self.janela.title("Minha Janela") # Título da janela
        self.janela.geometry("400x300") # Área da janela
        self.criar_widgets()

    def criar_widgets(self):
        Label(self.janela, text="Olá, mundo!").pack()

        self.frameA = Frame(self.janela, bg="lightgreen", width=400, height=300, bd=2, relief="solid") # Criando o container
        self.frameA.pack(pady=10) #Controle da posição do frame
        self.frameA.pack_propagate(False)

        self.widgetA = Label(self.frameA, text="Dentro do frame")
        self.widgetA.pack(pady=20)

        # Botão
        self.botao1 = Button(
            self.frameA,
            text='OK',
            height=1,
            width=5,
            fg='blue',
            bg='yellow',
            font=('verdana', 12, 'bold', 'italic'),
            command=self.ao_clicar
        )
        self.botao1.pack(pady=10)

        # Label 
        self.texto1 = Label(
            self.frameA,
            text='TSI - IFRN/ZL',
            fg='yellow',
            bg='black',
            font=('Arial', 20, 'bold')
        )
        self.texto1.pack(pady=30)

        # Input - entrada do usuário
        self.frameEntrada = Frame(self.frameA, bg="lightgreen")
        self.frameEntrada.pack(pady=10)

        Label(self.frameEntrada, text="Digite:", bg="lightgreen").pack(side=LEFT, padx=5)
        self.caixa1 = Entry(self.frameEntrada, width=20)
        self.caixa1.pack(side=LEFT)


    def ao_clicar(self):
        self.widgetA.config(text="Botão clicado!")

    def executar(self):
        self.janela.mainloop()

aplicacao = App()
aplicacao.executar()
from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.frame1 = Frame(self.janela, width=300, height=150, bg="black")
        self.frame1.pack(pady=10)
        self.frame1.pack_propagate(False)   # agora os 300x150 valem de verdade
        self.frame1.bind('<Enter>', self.mudarParaAmarelo)
        self.frame1.bind('<Leave>', self.mudarParaAzul)
        self.frame1.bind('<Button-1>', self.mudarParaVermelho)
        self.frame1.bind('<Button-2>', self.fecharJanela)
        

        self.janela.mainloop()


    def mudarParaAmarelo(self, event):
        self.frame1.config(bg="yellow")

    def mudarParaAzul(self, event):
        self.frame1.config(bg="Blue")

    def mudarParaVermelho(self, event):
        self.frame1.config(bg="Red")

    def fecharJanela(self, event):
        self.janela.destroy()

aplicacao = App()
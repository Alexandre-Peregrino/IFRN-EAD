class ClasseA:
    def ver(self):
        print('Estou na classe A')

class ClasseB:
    def mostrar(self):
        print('Estou na classe B')

class ClasseC(ClasseA, ClasseB):
    def exibir(self):
        print('Estou na classe C')

teste = ClasseC()
teste.ver()
teste.mostrar()
teste.exibir()
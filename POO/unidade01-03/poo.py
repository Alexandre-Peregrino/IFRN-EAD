class Animal:
    def __init__(self, nome):
        self. __nome = nome

    def comer(self):
        print(f'{self. __nome} está comendo')

class Gato(Animal):
    def __init__(self, nome):
        super() .__init__(nome)

gato = Gato('Tom')
gato.comer()
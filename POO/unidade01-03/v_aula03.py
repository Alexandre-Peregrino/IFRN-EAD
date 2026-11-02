class Amigo:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def insere_telefone(self, numero):
        self.telefones.append(Telefone(numero))

    def lista_telefones(self):
        for telefone in self.telefones:
            print(telefone.numero)

class Telefone:
    def __init__(self, numero):
        self.numero = numero

amigo1 = Amigo('joão')
amigo1.insere_telefone(123456789)
amigo1.insere_telefone(987654321)
print(amigo1.lista_telefones())
print(amigo1.telefones[0].numero)
print(amigo1.telefones[1].numero)

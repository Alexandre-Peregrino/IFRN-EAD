class Triangulo:
    nome_classe = 'Classe Triângulo'
    def __init__(self, ladoa, ladob, ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc

    def existencia(self):
        ab = self.ladoa + self.ladob
        ac = self.ladoa + self.ladoc
        bc = self.ladob + self.ladoc
        if (ab <= self.ladoc) or (ac <= self.ladob) or (bc <= self.ladoa):
            print('Triângulo impossível por condições de existência')
            return False
        return True

    def perimetro(self):
        return self.ladoa + self.ladob + self.ladoc

    def maior_lado(self):
        lados = [self.ladoa, self.ladob, self.ladoc]
        tamanho = 0
        for comp in lados:
            if comp > tamanho:
                tamanho = comp
        return tamanho

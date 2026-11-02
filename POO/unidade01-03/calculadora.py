class calculadora():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def soma(self):
        return self.x + self.y
    def multiplicacao(self):
        return self.x * self.y

calc1 = calculadora(4, 5)
print(calc1.soma())
print(calc1.multiplicacao())

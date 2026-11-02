class Animal:
    quemsoueu = 'Sou um Animal'
    def som(self):
        return "Som genérico"

class Gato(Animal):
    def som(self):
        return "Miau"

class Cachorro(Animal):
    def som(self):
        return "Auau"
    
bicho_01 = Animal()
print(bicho_01.quemsoueu + '|' + bicho_01.som())
bicho_02 = Gato()
print(bicho_02.quemsoueu + '|' + bicho_02.som())
bicho_03 = Cachorro()
print(bicho_03.quemsoueu + '|' + bicho_03.som())
from triangulo import Triangulo

def main():
    # Programa principal: quem conversa com o usuário
    a = int(input('Informe o primeiro lado: '))
    b = int(input('Informe o segundo lado: '))
    c = int(input('Informe o terceiro lado: '))

    t = Triangulo(a, b, c)

    if t.existencia():
        print(f'Perímetro: {t.perimetro()}')
        print(f'Maior lado: {t.maior_lado()}')

    print(f'Nome da Classe = {Triangulo.nome_classe}')
    Triangulo.nome_classe = 'Quadrado'
    print(f'Nome da Classe = {Triangulo.nome_classe}')  

if __name__ == "__main__":
    main()
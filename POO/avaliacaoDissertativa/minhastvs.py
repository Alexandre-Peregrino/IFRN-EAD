# minhastvs.py
from eletrodomesticos import Televisao

# TV da sala: instancia, atribui o nome e altera tamanho e marca
tv_sala = Televisao()
tv_sala.nome = 'tv_sala'
tv_sala.tamanho = 32
tv_sala.marca = 'Filipys'

# TV do quarto: instancia, atribui o nome e altera marca e estado
tv_quarto = Televisao()
tv_quarto.nome = 'tv_quarto'
tv_quarto.marca = 'Xilco'
tv_quarto.ligada = True

# Exibe a configuração das duas TVs
print('Nome | Canal Atual | Tamanho | Marca | Ligada (S/N)?')
print(f'{tv_sala.nome} | {tv_sala.canal} | {tv_sala.tamanho} | {tv_sala.marca} | {"S" if tv_sala.ligada else "N"}')
print(f'{tv_quarto.nome} | {tv_quarto.canal} | {tv_quarto.tamanho} | {tv_quarto.marca} | {"S" if tv_quarto.ligada else "N"}')
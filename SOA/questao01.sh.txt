#!/bin/bash
# Questão 01 - Conta quantos processos estão em execução na máquina

# ps -e        -> lista TODOS os processos do sistema
# --no-headers -> remove a linha de cabeçalho, que não é um processo
# wc -l        -> conta as linhas; cada linha = um processo
total=$(ps -e --no-headers | wc -l)

echo "O número total de processos em execução é: $total"
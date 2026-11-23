#!/bin/bash

HOJE=$(date)
echo "Hello, $USER!"
echo "Hoje é $HOJE"

total_arquivos=$(ls | wc -l)
echo "Total de arquivos no diretório atual: $total_arquivos"

echo "Digite o valor de uma variável: "
read variavel
echo "O valor da variável é: $variavel"

echo "O nome deste script é: $0"
echo "Recebidos $# argumentos: $*"
echo "O primeiro argumento é: $1"
echo "O segundo argumento é: $2"

echo "Digite 1 ou 2 para escolher uma opção: "
read opcao
case $opcao in
    1)
        echo "Você escolheu a opção 1"
        ;;
    2)
        echo "Você escolheu a opção 2"
        ;;
    *)
        echo "Opção inválida"
        ;;
esac
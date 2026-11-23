#!/bin/bash
# Questão 03 - Igual à 02, mas aceita VÁRIOS nomes

# -eq 0 = exige ao menos um nome
if [ $# -eq 0 ]; then
    echo "Uso: $0 <nome1> [nome2] [nome3] ..."
    exit 1
fi

# "$@" expande todos os argumentos, um por vez, preservando espaços
for usuario in "$@"; do
    echo "----------------------------------------"

    if grep -q "^$usuario:" /etc/passwd; then
        echo "O usuário '$usuario' existe no sistema."

        home=$(grep "^$usuario:" /etc/passwd | cut -d: -f6)
        echo "Diretório home: $home"

        validade=$(sudo grep "^$usuario:" /etc/shadow | cut -d: -f8)

        if [ -z "$validade" ]; then
            echo "Validade da senha: sem expiração definida"
        else
            data_exp=$(date -d "1970-01-01 + $validade days" +%d/%m/%Y)
            echo "Validade da senha: $data_exp"
        fi
    else
        echo "O usuário '$usuario' NÃO existe no sistema."
    fi
done
echo "----------------------------------------"
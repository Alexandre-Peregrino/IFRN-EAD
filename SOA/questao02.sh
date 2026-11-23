#!/bin/bash
# Questão 02 - Verifica se UM usuário existe e mostra home + validade da senha

# Para rodar este script faça ./questao02.sh <nome_do_usuario>

# $# é a quantidade de argumentos. -ne 1 = "diferente de 1"
if [ $# -ne 1 ]; then
    echo "Uso: $0 <nome_do_usuario>"
    exit 1
fi

usuario=$1

# ^ ancora no início da linha e : garante o campo exato
# (sem isso, "ana" encontraria "angeliana")
if grep -q "^$usuario:" /etc/passwd; then
    echo "O usuário '$usuario' existe no sistema."

    # 6º campo do /etc/passwd = diretório home
    home=$(grep "^$usuario:" /etc/passwd | cut -d: -f6)
    echo "Diretório home: $home"

    # 8º campo do /etc/shadow = validade da senha (dias desde 1970)
    # sudo é necessário porque só o root lê o /etc/shadow
    validade=$(sudo grep "^$usuario:" /etc/shadow | cut -d: -f8)

    # -z testa se a string está vazia = senha sem expiração
    if [ -z "$validade" ]; then
        echo "Validade da senha: sem expiração definida"
    else
        # Converte os dias desde 1970 em data legível
        data_exp=$(date -d "1970-01-01 + $validade days" +%d/%m/%Y)
        echo "Validade da senha: $data_exp"
    fi
else
    echo "O usuário '$usuario' NÃO existe no sistema."
fi
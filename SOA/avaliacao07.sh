#!/bin/bash
# Questão 01 - Conta quantos processos estão em execução na máquina

# ps -e        -> lista TODOS os processos do sistema
# --no-headers -> remove a linha de cabeçalho, que não é um processo
# wc -l        -> conta as linhas; cada linha = um processo
total=$(ps -e --no-headers | wc -l)

echo "O número total de processos em execução é: $total"



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



#!/bin/bash
# Questão 04 - Backup de arquivos/diretórios para /tmp/AnoMesDia-HoraMinuto

if [ $# -eq 0 ]; then
    echo "Uso: $0 <arquivo_ou_diretorio> [...]"
    exit 1
fi

# date +%Y%m%d-%H%M gera o formato pedido: 20261123-1818
destino="/tmp/$(date +%Y%m%d-%H%M)"

# -p cria a pasta e não dá erro se ela já existir
mkdir -p "$destino"

for item in "$@"; do
    # -e testa se o caminho existe (serve para arquivo e diretório)
    if [ -e "$item" ]; then
        # -r é obrigatório para copiar diretórios
        cp -r "$item" "$destino"/
        echo "Copiado: $item"
    else
        echo "Aviso: '$item' não existe — ignorado."
    fi
done

echo "Backup concluído em: $destino"
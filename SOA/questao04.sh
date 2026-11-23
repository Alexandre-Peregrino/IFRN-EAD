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
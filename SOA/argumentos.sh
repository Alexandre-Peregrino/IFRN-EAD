#!/bin/bash
echo "Total de argumentos passados para o script: $#"

while [[ $# -gt 0 ]]; do
    echo "Nome: $1" - Idade: $2
    shift 2
done
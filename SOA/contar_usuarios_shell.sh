#!/bin/bash
# Conta quantos usuários usam cada shell

echo "Usuários por shell:"
echo "-------------------"

cut -d: -f7 /etc/passwd | sort | uniq -c | sort -rn
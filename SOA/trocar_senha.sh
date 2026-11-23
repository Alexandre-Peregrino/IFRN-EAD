#!/bin/bash

dias=$(echo $(($(date +%s)/60/60/24)))

#echo $dias

#cria uma iteração para cada usuário
for i in $(awk -F: '($3 >=1000) {print $1}' /etc/passwd | sed 1d)
do
   tempo=$(grep $i /etc/shadow | awk -F: '{print '$dias' - $3}')

   if [ $tempo -lt 90 ]
   then
      echo "A senha do usuário $i foi alterada há $tempo dias"
   else
      echo "A senha do usuário $i foi alterada há $tempo dias e precisa ser alterada no proximo login"
   fi
done
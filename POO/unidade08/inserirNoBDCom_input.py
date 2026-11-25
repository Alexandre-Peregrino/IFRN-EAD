import sqlite3

con = sqlite3.connect('banco.db')
sql = con.cursor()

nome = input('Digite um Nome: ')
telefone = input('Digite um Telefone: ')
sql.execute("INSERT INTO teste (nome, telefone) VALUES (?, ?)", (nome, telefone))


con.commit()
con.close()
